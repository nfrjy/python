import re
pattern=re.compile(r'\| (\d+) \| (\d+) \|')
numset = set()
all='''
| 29266795 | 533 |
| 29370116 | 533 |
| 29467495 | 533 |
| 29500404 | 533 |
| 29500622 | 533 |
| 29515964 | 530 |
| 29516015 | 530 |
| 29520954 | 530 |
| 29520960 | 530 |
| 29525346 | 530 |
| 29525351 | 530 |
| 29525365 | 530 |
'''
matches=pattern.findall(all)
for did,dt in matches:
    numset.add(did)
print numset
