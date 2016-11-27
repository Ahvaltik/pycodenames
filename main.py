__author__ = 'Pawel'

import random

word_file = open("word_list.txt")
word_text = word_file.read()
word_list = word_text.split("\n")

colors = ['red', 'blue']

word_table = []
role_table = []
places = []

for x in range(5):
    word_table.append([])
    role_table.append([])
    for y in range(5):
        word = random.choice(word_list)
        word_list.remove(word)
        word_table[x].append(word)
        role_table[x].append('white')
        places.append((x, y))

main_color = random.choice(colors)
colors.remove(main_color)
second_color = colors[0]

main_team = random.sample(places, 9)
map(lambda place: places.remove(place), main_team)
for place in main_team:
    role_table[place[0]][place[1]] = main_color

second_team = random.sample(places, 8)
map(lambda place: places.remove(place), second_team)
for place in second_team:
    role_table[place[0]][place[1]] = second_color
killer = random.choice(places)
role_table[killer[0]][killer[1]] = 'grey'

table = open('table.html', 'w')
boss_table = open('boss_table.html', 'w')
line = '<html><body><p>Team <font color=' + main_color + '>' + main_color + '</font> starts.</p><table>'
table.write(line)
boss_table.write(line)
for x in range(5):
    line = '<tr>'
    table.write(line)
    boss_table.write(line)
    for y in range(5):
        line = '<th'
        table.write(line)
        boss_table.write(line)

        color = role_table[x][y]
        line = ' style=\"background-color:' + color + '\" '
        boss_table.write(line)

        word = word_table[x][y]
        word_size = len(word)
        line = '>' + word + '</th>'
        table.write(line)
        boss_table.write(line)
    line = '</tr>'
    table.write(line)
    boss_table.write(line)
line = '</table></body></html>'
table.write(line)
boss_table.write(line)

table.flush()
table.close()

boss_table.flush()
boss_table.close()


