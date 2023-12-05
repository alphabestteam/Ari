$outFile = "running_pods.txt"

kubectl get pods --all-namespaces --field-selector=status.phase=Running -o wide | Out-File -FilePath $outFile -Encoding utf8

Write-Host "added to the file"
