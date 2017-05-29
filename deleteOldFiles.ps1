# Delete files older than $Days days in $Dir
# Put it in a weekly Scheduled task
# You need to: Set-ExecutionPolicy bypass
# and: Set-ExecutionPolicy Unrestricted

# CONFIG

$Days = "30"
$Dir = "D:\Users"

# END CONFIG

Get-ChildItem -Path $Dir -Recurse -exclude *.mds | where {$_.LastWriteTime -le $(get-date).AddDays(-$Days)} | Remove-Item -Recurse
