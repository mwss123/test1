import sys

if len(sys.argv) !=2 :
    print(f"#usage : python {sys.argv[0]} [num]")
    sys.exit()

try :
    num = int(sys.argv[1])
    print(10/num)
except ValueError :
    print("input not valid")
    sys.exit()                         # sys exit ha mun, try kka ji an nae-ryo-gam

except  ZeroDivisionError:
    print("Error because num is 0")
    sys.exit()

