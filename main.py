import os
files = [i for i in os.listdir() if i.endswith('.txt') if i != 'new_file.txt']
full_txt = {}

for name in files:
    with open(name, encoding='utf') as file:
        lines_list = file.readlines()
        full_txt.update({name: [len(lines_list), lines_list]})

full_txt = dict(sorted(full_txt.items(), key=lambda item: item[1][0]))
# print(full_txt)

with open('new_file.txt', 'w', encoding='utf-8') as f:
    for k, v in full_txt.items():
        s = open(k, encoding='utf-8').read()
        f.write(f'{k}\n')
        f.write(f'{str(v[0])}\n')
        for i in v[1]:
            f.write(f'{i}')
        f.write('\n')

