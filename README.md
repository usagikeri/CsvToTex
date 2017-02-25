# CsvToTex
Convert csv file to tex table format.  
This program was created by Python3.5.1.
It does not run in Python2.

## Usage
`$python csvToTex.py input.csv`  
As a result, "output.tex" is output.

input.csv
```
Menu,Price(yen)
Rice,100
Bread,120
```
output.tex
```
\documentclass{article}

\begin{document}

\begin{table}[htbp]
	\caption{}
	\label{}
	\centering
	\begin{tabular}{|c|c|} \hline
	Menue & Price(yen) \\ \hline
	Rice & 100 \\ \hline
	Bread & 120 \\ \hline
	\end{tabular}
\end{table}

\end{document}
```
