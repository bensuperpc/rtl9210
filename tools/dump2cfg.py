#!/usr/bin/python3

import sys
import re

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '<dump file>')
    exit(1)

kre = re.compile(r'^[A-Z_]+$')
fin = open(sys.argv[1], 'r')
fout = None

for line in fin:
    fields = line.split(':')
    if len(fields) < 2:
        continue

    key = fields[0].strip()
    val = fields[1].strip()

    if key == 'Device':
        if fout:
            fout.close()
        fout = open(val.strip('[]') + '.cfg', 'w')
        fout.write('; ' + val + ' : ' + fields[2].strip() + '\r\n')
    elif kre.match(key) and val != 'n/a':
        fout.write(key + ' = ' + val + '\r\n')

fout.close()
