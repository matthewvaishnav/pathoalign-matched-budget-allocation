$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex

Copy-Item main.pdf paired-acquisition-factorization-allocation.pdf -Force
Copy-Item main.pdf ..\paired-acquisition-factorization-allocation.pdf -Force
Write-Host "Built paper\paired-acquisition-factorization-allocation.pdf"
