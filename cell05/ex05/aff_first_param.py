import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")

"""
cd cell05/ex05
python aff_first_param.py
python aff_first_param.py "Code Ninja" "Numerique" "42"
"""