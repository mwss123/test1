
f = open('./017.txt', 'w')

for i in range(10) :
    data = '{0} line'.format(i)
    f.write(f"{data}\n")

f.close()
