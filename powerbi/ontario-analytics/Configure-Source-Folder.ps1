$root = $PSScriptRoot
$path = Join-Path $root 'Ontario.SemanticModel\model.bim'
$model = Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
$dataFolder = (Join-Path $root 'input') + '\'
$expression = $model.model.expressions | Where-Object { $_.name -eq 'SourceFolder' }
$expression.expression = '"' + $dataFolder.Replace('"','""') + '" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]'
$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, ($model | ConvertTo-Json -Depth 100), $utf8)
Write-Output 'Source folder configured. Open Ontario.pbip in Power BI Desktop and select Refresh.'
