import sys

if len(sys.argv) != 2 :
    print(f"usage: python {sys.argv[0]} [txt]")
    sys.exit()

f = sys.argv[1]

# try-except  ---> when occuring error, we want to let them know why error occur.
try :
    with open(f, 'r') as f1 :
        read = f1.readlines()       # list ro jojang
except FileNotFoundError:
    print(f"{f} not found.... please check..")
    sys.exit()

print(read)
