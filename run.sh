#!/bin/bash

echo " Executing find_donor_zip.py"
python3 ./src/find_donor_zip.py ./input/itcont.txt ./output/medianvals_by_zip.txt

echo " Executing find_donor_date.py"
python3 ./src/find_donor_date.py ./input/itcont.txt ./output/medianvals_by_date.txt
