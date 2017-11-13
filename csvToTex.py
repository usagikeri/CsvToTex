# -*- coding: utf-8 -*-
#　This program was created　by Python 3.5.1

import sys
import csv

class CsvToTex():
    def __init__(self):
        self.begin = "\documentclass{jarticle}\n\n"+ \
                      "\\begin{document}\n\n"+ \
                      "\\begin{table}[htbp]\n"+ \
                      "\t\caption{}\n"+ \
                      "\t\label{}\n"+ \
                      "\t\centering\n"

        self.end = "\t\end{tabular}\n"+ \
                    "\end{table}\n\n"+ \
                    "\end{document}"

    def spchar_escape(self,txt):
        if isinstance(txt,str) == True:
            spchar_dict = str.maketrans({"#":"\#",
                                         "%":"\%",
                                         "$":"\$",
                                         "&":"\&",
                                         "_":"\_",
                                         "{":"\{",
                                         "}":"\}",
                                         "<":"\\textless",
                                         ">":"\\textgreater",
                                         "^":"\\textasciicircum",
                                         "~":"\\textasciitilde",
                                         "\\":"\\textbackslash",
                                         "|":"\\textbar"})
            return txt.translate(spchar_dict)
        else:
            print("Type Error!!")

    def convert(self,txt):
        return self.spchar_escape(txt).replace(","," & ")

    def r_and_w(self,filename):
        stdout = []
        with open("output.tex","w") as texfile:
            texfile.write(self.begin)
            stdout.append("{}".format(self.begin))
            with open(filename,"r") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)

                texfile.write("\t"+"\\begin{tabular}{|"+str("c|" * len(header))+"} \hline\n")
                stdout.append("{}".format("\t"+"\\begin{tabular}{|"+str("c|" * len(header))+"} \hline\n"))
                header = ','.join(header)
                texfile.write("\t"+self.convert(header)+" \\\\ \hline\n")
                stdout.append("{}".format("\t"+self.convert(header)+" \\\\ \hline\n"))

                for line in reader:
                    line = ','.join(line)
                    value = self.convert(line)
                    texfile.write("\t"+value.rstrip()+" \\\\ \hline\n")
                    stdout.append("{}".format("\t"+value.rstrip()+" \\\\ \hline\n"))
            texfile.write(self.end)
            stdout.append("{}".format(self.end))

        return stdout

if __name__ == '__main__':
    args = sys.argv
    filename = args[1]
    ctt = CsvToTex()
    print("".join(ctt.r_and_w(filename)))
