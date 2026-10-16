$root = $PSScriptRoot
$folder = (Join-Path $root 'input') + '\'
$modelPath = Join-Path $root 'Ontario.SemanticModel\model.bim'
$tmdlPath = Join-Path $root 'Ontario.SemanticModel\definition\expressions.tmdl'
$parameter = '"' + $folder.Replace('"','""') + '" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]'
$utf8 = New-Object System.Text.UTF8Encoding($false)
if (Test-Path -LiteralPath $tmdlPath) {
    $source = [System.IO.File]::ReadAllText($tmdlPath)
    $updated = [regex]::Replace($source, '(?m)^expression SourceFolder = .*$', [System.Text.RegularExpressions.MatchEvaluator]{ param($match) 'expression SourceFolder = ' + $parameter })
    [System.IO.File]::WriteAllText($tmdlPath, $updated, $utf8)
} elseif (Test-Path -LiteralPath $modelPath) {
    $model = Get-Content -LiteralPath $modelPath -Raw | ConvertFrom-Json
    ($model.model.expressions | Where-Object { $_.name -eq 'SourceFolder' }).expression = $parameter
    [System.IO.File]::WriteAllText($modelPath, ($model | ConvertTo-Json -Depth 100), $utf8)
} else { throw 'Semantic model not found. Keep the complete project folder together.' }
Write-Output 'SourceFolder configured. Open Ontario.pbip and select Refresh > Schema and data.'
