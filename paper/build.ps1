$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (Get-Command latexmk -ErrorAction SilentlyContinue) {
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
} else {
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
}

Copy-Item main.pdf pathoalign-matched-budget-allocation.pdf -Force
Write-Host "Built paper\pathoalign-matched-budget-allocation.pdf"
