import sys

f = sys.argv[1]
print(f)
d = {}

if len(sys.argv) != 2 :               # preventing error
    print(f"#usage: python {sys.argv}[0] [fasta]")
    sys.exit

with open (f, 'r') as f1 :
    for line in f1 :
        if line.startswith(">") :
            continue
        for i in line.strip() :
            if i in d :
                d[i] += 1
            else :
                d[i] = 1

print(d)

total = 0
for k, v in d.items() :         # Checking total yumgi sut-ja
    total += v

print(total)

with open("result.txt", 'w') as handle :
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
