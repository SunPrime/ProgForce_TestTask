def to_print(data):
    for key in data.keys():
        print(key)
        for value in data.values():
            print(value)
        print()

emails = {}

with open('mbox.txt') as input_file:
    line = input_file.readline()
    item = {}
    while line:
        if line.startswith('From '):
            item = {}
            string = line.split(' ')
            if emails.get(string[1]) == None:
                emails[string[1]] = []
            item['date'] = string[3:]
        if line.startswith('Subject:'):
            subj_array = []
            while line != '\n':
                subj_array.append(line)
                line = input_file.readline()
            item['subj'] = subj_array
            emails[string[1]].append(item)
        line = input_file.readline()

#output from (date): subject
to_print(emails)

# output "from: quantity"
for key, value in emails.items():
    res = '%s: %d' % (key, len(value))
    print(res)