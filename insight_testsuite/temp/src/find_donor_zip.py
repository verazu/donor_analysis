from collections import defaultdict
import numpy as np
import re


def main():
    write_zip_file("./output/medianvals_by_zip.txt")


# This function writes in a txt file
def write_zip_file(path):
    with open(path, "w") as medianvals_by_zip:
        find_zip_data(medianvals_by_zip)


# This function takes the lines of a txt file one at a time and return a string
def find_zip_data(filename):
    d = defaultdict(list)  # automatically initializes the first value
    with open("./input/itcont.txt", "r") as infile:
        while True:  # the while loop is used to deal with streaming entries
            line = infile.readline().strip()
            if line == "":
                break
            else:
                row = line.split("|")
                CMTE_ID, ZIP_CODE, TRANSACTION_AMT, OTHER_ID = (row[0],
                                                                row[10][:5],
                                                                row[14],
                                                                row[15])
                if check_zip_format(OTHER_ID, CMTE_ID, TRANSACTION_AMT,
                                    ZIP_CODE):
                    d[(CMTE_ID, ZIP_CODE)].append([TRANSACTION_AMT])
                    # change list to numpy array to speed up the calculations
                    data = np.array(d[(CMTE_ID, ZIP_CODE)], dtype=int)
                    filename.write(CMTE_ID + "|" + ZIP_CODE + "|" +
                                   str(int(np.median(data).round())) + "|" +
                                   str(data.size) + "|" + str(data.sum()) +
                                   "\n")


# This function checks the string format of each entry using regular expression
def check_zip_format(OTHER_ID, CMTE_ID, TRANSACTION_AMT, ZIP_CODE):
    zip_check = re.compile("^\d{5}")
    if ((OTHER_ID == "") and (CMTE_ID != "") and (TRANSACTION_AMT != "") and
       (zip_check.match(ZIP_CODE) is not None)):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
