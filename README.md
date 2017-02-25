# CsvToTex
Convert csv file to tex table format.  
This program was created by <font color="Python3.5.1"></font>.
It does not run in <font color="Python2"></font>.

## Usage
`$python csvToTex.py inputTest.csv`  
As a result, "output.tex" is output.

```csv:inputTest.csv
Menu,Price(yen)
Rice,100
Bread,120
```  
```tex:output.tex
\documentclass{jarticle}

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
