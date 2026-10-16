// SourceFolder
"C:\PowerBI\Ontario\input\" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]

// SourcePHO
let
    W = Excel.Workbook(File.Contents(SourceFolder & "PHO_Chronic_Disease_Inc_Prev_Snapshot_2014_2023.xlsx"), [UseHeaders=false, DelayTypes=true, InferSheetDimensions=true]),
    S = W{[Item="Chron Dis Inc Prev Data",Kind="Sheet"]}[Data],
    H = Table.PromoteHeaders(Table.Skip(S,2),[PromoteAllScalars=true]),
    R = Table.RenameColumns(H,{{Table.ColumnNames(H){9},"SuppressionFlag"},{"95% Confidence Interval","ConfidenceInterval"}}),
    C = Table.TransformColumns(R,{{"Geography",Text.Trim,type text},{"Indicator",Text.Trim,type text},{"Year",each Int64.From(_),Int64.Type},{"Rate",each try Number.From(_) otherwise null,type nullable number},{"SuppressionFlag",each if _ = null then "" else Text.Trim(Text.From(_)),type text}}),
    V = Table.AddColumn(C,"ValidRate",each if [SuppressionFlag] = "" then [Rate] else null,type nullable number),
    D = Table.RemoveColumns(V,{"Rate"}),
    F = Table.RenameColumns(D,{{"ValidRate","Rate"}})
in F

// SourceCIHI
let
    W = Excel.Workbook(File.Contents(SourceFolder & "CIHI_Wait_Times_Priority_Procedures_2025.xlsx"),[UseHeaders=false, DelayTypes=true, InferSheetDimensions=true]),
    S = W{[Item="Table 1",Kind="Sheet"]}[Data],
    N = Table.SelectColumns(S,List.FirstN(Table.ColumnNames(S),8)),
    H = Table.PromoteHeaders(Table.Skip(N,1),[PromoteAllScalars=true]),
    C = Table.SelectColumns(H,{"Reporting level","Province","Region","Indicator","Metric","Data year","Unit of measurement","Indicator result"}),
    O = Table.SelectRows(C,each [Province]="Ontario"),
    R = Table.RenameColumns(O,{{"Reporting level","ReportingLevel"},{"Indicator","Procedure"},{"Data year","ReportingPeriod"},{"Unit of measurement","Unit"},{"Indicator result","ValueRaw"}}),
    T = Table.TransformColumns(R,{{"ReportingPeriod",each Text.From(_),type text},{"Metric",each Text.Lower(Text.Trim(_)),type text},{"Region",each if _="n/a" then "Ontario" else Text.Trim(_),type text}}),
    Y = Table.AddColumn(T,"Year",each Int64.From(Text.Start([ReportingPeriod],4)),Int64.Type),
    P = Table.AddColumn(Y,"PeriodType",each if Text.EndsWith([ReportingPeriod],"FY") then "Fiscal year" else if Text.EndsWith([ReportingPeriod],"Q3Q4") then "October–March" else "April–September",type text),
    V = Table.AddColumn(P,"Value",each try Number.From([ValueRaw]) otherwise null,type nullable number)
in V

// CIHIWide
let
    S = Table.SelectRows(SourceCIHI,each [PeriodType]="April–September"),
    M = Table.AddColumn(S,"MetricKey",each if [Metric]="50th percentile" then "MedianDays" else if [Metric]="90th percentile" then "P90Days" else if [Metric]="% meeting benchmark" then "BenchmarkPct" else if [Metric]="volume" then "Volume" else error "Unexpected CIHI metric",type text),
    C = Table.SelectColumns(M,{"ReportingLevel","Region","Procedure","Year","MetricKey","Value"}),
    P = Table.Pivot(C,{"MedianDays","P90Days","BenchmarkPct","Volume"},"MetricKey","Value")
in P

// DimIndicator
let S = Table.Distinct(Table.SelectColumns(FactPHO,{"Indicator"})), D = Table.AddColumn(S,"Disease",each if Text.Contains([Indicator],"asthma") then "Asthma" else if Text.Contains([Indicator],"COPD") then "COPD" else if Text.Contains([Indicator],"diabetes") then "Diabetes" else if Text.Contains([Indicator],"hypertension") then "Hypertension" else error "Unknown indicator",type text), T = Table.AddColumn(D,"Statistic",each if Text.StartsWith([Indicator],"Prevalence") then "Prevalence" else "Incidence",type text) in T

// DimPHU
Table.Distinct(Table.SelectColumns(FactPHO,{"Geography"}))

// DimProcedure
Table.Distinct(Table.SelectColumns(FactWaitProvince,{"Procedure"}))

// DimWaitRegion
Table.Distinct(Table.SelectColumns(FactWaitRegion,{"Region"}))

// DimYear
let Y = List.Combine({FactPHO[Year],FactWaitProvince[Year],FactWaitRegion[Year]}), T = Table.FromList(List.Numbers(List.Min(Y),List.Max(Y)-List.Min(Y)+1),Splitter.SplitByNothing(),{"Year"}), R = Table.TransformColumnTypes(T,{{"Year",Int64.Type}}) in R

// FactOntario
let S = Table.SelectRows(SourcePHO,each [Measure]="Age-standardized rate (both sexes)" and [Geography]="Ontario"), R = Table.SelectColumns(S,{"Indicator","Year","Rate","ConfidenceInterval","SuppressionFlag"}) in R

// FactPHO
let S = Table.SelectRows(SourcePHO,each [Measure]="Age-standardized rate (both sexes)" and not List.Contains({"Central East","Central West","East","North East","North West","South West","Toronto","Ontario"},[Geography])), R = Table.SelectColumns(S,{"Indicator","Year","Geography","Rate","ConfidenceInterval","SuppressionFlag"}) in R

// FactWaitProvince
Table.RemoveColumns(Table.SelectRows(CIHIWide,each [ReportingLevel]="Provincial"),{"ReportingLevel"})

// FactWaitRegion
Table.RemoveColumns(Table.SelectRows(CIHIWide,each [ReportingLevel]="Regional"),{"ReportingLevel"})

// SelectCIHIYear
let S = Table.Distinct(Table.SelectColumns(FactWaitProvince,{"Year"})), R = Table.Sort(S,{{"Year",Order.Descending}}) in R

// SelectPHOYear
let S = Table.Distinct(Table.SelectColumns(FactPHO,{"Year"})), R = Table.Sort(S,{{"Year",Order.Descending}}) in R
