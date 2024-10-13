#!/bin/bash

python3 prog.py < check/1.in > check/1.out
python3 prog.py < check/2.in > check/2.out
python3 prog.py < check/3.in > check/3.out

python3 prog.py < check/3.in | diff - check/3.out
python3 prog.py < check/2.in | diff - check/2.out
python3 prog.py < check/1.in | diff - check/1.out
