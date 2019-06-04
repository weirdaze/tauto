f = open("/Users/castillo/Documents/TCPDUMPNOKIA5301118A.log", "r")

y = 0
lines = []
for x in f:
    lines.append(x)

parsed = []
sub = []
section = True
for line in lines:
    if 'oui Arista Networks' in line:
        section = True
        print(line.split(',')[2].split('tos')[1])

    if 'vni' in line:
        print(line.split(','))