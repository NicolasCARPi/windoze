# Delete files older than $Days days in $Dir
# Put it in a weekly Scheduled task

# CONFIG

$Days = "30"
$Dir = "D:\Users"

# END CONFIG

Get-ChildItem -Path $Dir -Recurse | where {$_.LastWriteTime -le $(get-date).AddDays(-$Days)} | Remove-Item
