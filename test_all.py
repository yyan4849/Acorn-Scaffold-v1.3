"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

import subprocess
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_init_position import run_tests as test_init_position

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_grid()
test_parser()
test_init_position()

print("\n")
# Run the e2e script
subprocess.call(['./test_e2e.sh'])
