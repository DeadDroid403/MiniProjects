<#******************************************************************************************
This is a Days, Months and Years Calculating Script...
It Takes Input Of Your Date of Birth and Gives You how Many days, Months and Years You Lived
********************************************************************************************
Made  BY  :-- DeadDroid
******************************************************************************************#>


# Taking User Input From User
[int]$Birthdate = Read-Host -Prompt "Enter Your Day of Birth Here  "
[int]$Birthmonth = Read-Host -Prompt "Enter Your Month of Birth Here  "
[int]$Birthyear = Read-Host -Prompt "Enter Your Year of Birth Here  "

# Fetching Current Date
$Currentdate = get-date
$Currentday = $Currentdate.Date.day
$Currentmonth = $Currentdate.Date.month
$Currentyear = $Currentdate.Date.year

# Fetching TotalDays Lived By Years
if ($Birthyear -eq 2024 -or $Birthyear -eq 2023) {
    Write-Warning 'Oops ! Sorry :(  Only Works For People Born Before 2022'
    exit 1
}
$Years = ($Currentyear - $Birthyear)
$Years2 = $Years - 1
[int]$additionaldays = $Years / 4
$Totalyeardays = ($years2 * 365) + $additionaldays


# Fetching TotalDays Lived By Months
$monthdays1 = 0
$monthdays2 = 0
if ($Birthmonth -gt 12 -or $Birthmonth -lt 1) {
    Write-Warning 'Oops ! `_`  Invalid Value For Month of Birth'
    exit 1
}
$monthnames = @(31,28,31,30,31,30,31,31,30,31,30,31)
for ($i = $Birthmonth;$i -lt 12;$i++) {
    $monthdays1 += $monthnames[$i]
}
for ($i = 0;$i -lt ($Currentmonth - 1);$i++) {
    $monthdays2 += $monthnames[$i]
}
$totalmonthdays = $monthdays1 + $monthdays2

# Fetching TotalDays Lived By Days of Month
if ($Birthdate -lt 1 -or $Birthdate -gt 31) {
    Write-Warning 'Oops ! `_`  Invalid Value For Date of Birth'
    exit 1
}
$i1 = $Birthmonth - 1
$daysinBM = $monthnames[$i1] - $Birthdate
$totaldaysofM = $daysinBM + $Currentday

# Fetching Final Total Days You Lived Till Now
$totalDayULived = $totaldaysofM + $totalmonthdays + $Totalyeardays
if (($Birthyear % 4) -eq 0) {
    $totalDayULived += 1   
}
cls

Write-Host "****************************************************************************" -ForegroundColor Cyan
Write-Host "Your Date of Birth is - $Birthdate/$Birthmonth/$Birthyear" -ForegroundColor Yellow
write-host "You Have Lived - $totalDayULived Days in Your Life " -ForegroundColor Yellow 
Write-Host ""
Write-Host "Thanks For Using This Script And Feel Free To Share Your Thoughts  :D" -ForegroundColor Green
Write-Host "****************************************************************************" -ForegroundColor Cyan


