def to_print(data):
    for i in range(len(data)):
        print(data[i])
    print()

d = []
with open('mbox.txt') as f:
    line = f.readline()
    while line:
        if line.startswith('From '):
            item = []
            string = line.split(' ')
            d.append(string[1])
            item.append(string[3:])
        if line.startswith('Subject:'):
            k = 0
            subj_array = []
            while line != '\n':
                subj_array.append(line)
                line = f.readline()
            item.append(subj_array)
            d.append(item)
        line = f.readline()

j = 0
quantity = {}
while j < len(d):
    k = d.count(d[j])
    quantity[d[j]] = k
    j += 2

to_print(d)

for i in quantity:
    res = 'From %s quantity is %d' % (i, quantity[i])
    print(res)

