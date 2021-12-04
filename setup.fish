#!/bin/fish

mkdir "day-$argv"
touch "day-$argv/soln1.py"
touch "day-$argv/sample.txt"
touch "day-$argv/soln2.py"
python 'sel.py' $argv