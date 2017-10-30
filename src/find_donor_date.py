from collections import defaultdict
import numpy as np
import re


def check_date_format(OTHER_ID, CMTE_ID, TRANSACTION_AMT, TRANSACTION_DT):
    date_check = re.compile("^\d{8}$")
    if ((OTHER_ID == "") and (CMTE_ID != "") and (TRANSACTION_AMT != "") and
    (date_check.match(TRANSACTION_DT) is not None)):
        return True
    else:
        return False

def find_date_data(filename):
    d = defaultdict(list)
    with open("./input/itcont.txt", "r") as infile:
        for line in infile:
            row = line.split("|")
            CMTE_ID, TRANSACTION_DT, TRANSACTION_AMT,  OTHER_ID = (row[0], row[13],
                                                            int(row[14]), row[15])
            if check_date_format(OTHER_ID, CMTE_ID, TRANSACTION_AMT, TRANSACTION_DT):
                d[(CMTE_ID, TRANSACTION_DT)].append(TRANSACTION_AMT)
        for k in sorted(d.keys(), key=lambda element: (element[0], element[1])):
            data = np.array(d[k], dtype=int)
            filename.write(k[0]+"|"+k[1]+"|"+
                        str(int(np.median(data).round()))+
                        "|"+str(data.size)+"|"+str(data.sum())+"\n")

def write_date_file(path):
    with open(path, "w") as medianvals_by_date:
        find_date_data(medianvals_by_date)

write_date_file("./output/medianvals_by_date.txt")
