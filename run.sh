#!/bin/sh
echo "Solve ODD TORUS UPPER BOUND, for Theorem 1.4 \n" 
python3 odd_torus.py
wait
echo "Solve EVEN TORUS UPPER BOUND, for Theorem 1.2 \n" 
python3 even_torus.py
wait
echo "Solve REGULAR BOARD UPPER BOUND, for Theorem 1.5 \n" 
python3 regular_board.py
