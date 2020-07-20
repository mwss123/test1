
"""

f = open('read_sample.txt', 'r')
print(f.read())

"""

with open('read_sample.txt', 'r') as handle :
    for line in handle :
        if line.startswith(">") :      # if > ga po ham daen line eun except hae ra
            continue
        print(line.strip())     # enter delete ha gi we hae seo strip!
