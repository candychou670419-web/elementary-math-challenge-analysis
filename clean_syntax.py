# -*- coding: utf-8 -*-
import sys

for fname in ['add_jump4_part1.py', 'add_jump4_part2.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('"\n        "solution":', '",\n        "solution":')
    content = content.replace('"\r\n        "solution":', '",\r\n        "solution":')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print('Successfully added missing commas before solution in part1 and part2!')
