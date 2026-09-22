import sys

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = list(range(start, end + 1))
    print(result)
else:
    print("none")


"""
cd cell05/ex14
python free_range.py
python free_range.py 10 14

"""