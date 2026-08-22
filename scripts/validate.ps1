[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$skillFiles = Get-ChildItem -Path (Join-Path $repoRoot 'skills') -Filter 'SKILL.md' -Recurse
$ownedSkillCount = $skillFiles.Count
if ($ownedSkillCount -eq 0) { throw 'No local SKILL.md files found.' }
$ownedSkillNames = @{}

foreach ($skillFile in $skillFiles) {
    $content = Get-Content -Raw -Encoding UTF8 -Path $skillFile.FullName
    if (-not $content.StartsWith('---')) { throw "Missing YAML frontmatter: $($skillFile.FullName)" }
    if ($content -notmatch '(?m)^name:\s*.+$') { throw "Missing name: $($skillFile.FullName)" }
    if ($content -notmatch '(?m)^description:\s*.+$') { throw "Missing description: $($skillFile.FullName)" }

    $skillName = ([regex]::Match($content, '(?m)^name:\s*(.+)$')).Groups[1].Value.Trim()
    $skillDirectory = Split-Path -Parent $skillFile.FullName
    if ((Split-Path -Leaf $skillDirectory) -ne $skillName) {
        throw "Skill directory and name differ: $skillDirectory"
    }
    if ($ownedSkillNames.ContainsKey($skillName)) {
        throw "Duplicate local Skill name: $skillName"
    }
    $ownedSkillNames[$skillName] = $true

    $evalPath = Join-Path $skillDirectory 'evals\evals.json'
    if (-not (Test-Path $evalPath)) { throw "Missing evals: $skillDirectory" }

    $evalDocument = Get-Content -Raw -Encoding UTF8 -Path $evalPath | ConvertFrom-Json
    if ($evalDocument.skill_name -ne $skillName) {
        throw "Eval skill_name does not match Skill name: $evalPath"
    }
    if (-not $evalDocument.evals -or $evalDocument.evals.Count -eq 0) {
        throw "Eval document has no cases: $evalPath"
    }
    foreach ($evalCase in $evalDocument.evals) {
        foreach ($field in @('id', 'prompt', 'expected_output', 'expectations')) {
            if (-not $evalCase.PSObject.Properties[$field] -or [string]::IsNullOrWhiteSpace([string]$evalCase.$field)) {
                throw "Eval case is missing ${field}: $evalPath"
            }
        }
        if (@($evalCase.expectations).Count -eq 0) {
            throw "Eval case has no expectations: $evalPath"
        }
    }
}

Get-ChildItem -Path (Join-Path $repoRoot 'manifests') -Filter '*.json' | ForEach-Object {
    $manifest = Get-Content -Raw -Encoding UTF8 -Path $_.FullName | ConvertFrom-Json
    if (-not $manifest.packages -or $manifest.packages.Count -eq 0) { throw "Manifest has no packages: $($_.FullName)" }
    foreach ($package in $manifest.packages) {
        if (-not $package.source -or -not $package.skills -or $package.skills.Count -eq 0) {
            throw "Incomplete manifest package: $($_.FullName)"
        }
    }
}

$recommendedManifest = Get-Content -Raw -Encoding UTF8 -Path (Join-Path $repoRoot 'manifests\recommended.json') | ConvertFrom-Json
$allManifest = Get-Content -Raw -Encoding UTF8 -Path (Join-Path $repoRoot 'manifests\all-used.json') | ConvertFrom-Json
$allUpstreamNames = @($allManifest.packages | ForEach-Object { @($_.skills) })
if ($allUpstreamNames.Count -ne (@($allUpstreamNames | Select-Object -Unique)).Count) {
    throw 'All-tier manifest contains duplicate upstream Skill names.'
}
$recommendedUpstreamCount = @($recommendedManifest.packages | ForEach-Object { @($_.skills).Count } | Measure-Object -Sum).Sum
$allUpstreamCount = @($allManifest.packages | ForEach-Object { @($_.skills).Count } | Measure-Object -Sum).Sum
$recommendedTotal = $ownedSkillCount + $recommendedUpstreamCount
$allTotal = $ownedSkillCount + $allUpstreamCount

$allDescription = [string]$allManifest.description
if ($allDescription -notmatch "${allUpstreamCount} upstream Skills plus ${ownedSkillCount} owned Skills") {
    throw "All-tier manifest description count does not match its package list: $allUpstreamCount upstream, $ownedSkillCount owned."
}

Write-Host "Validation passed: $ownedSkillCount local skills, $ownedSkillCount eval documents, $recommendedTotal recommended skills, and $allTotal all-tier skills."
