import random

moodfile = open('moods.txt', 'r')
moods = []
for line in moodfile:
    line = line.rstrip()
    moods.append(line)

nounfile = open('nouns.txt', 'r')
nouns = []
for line in nounfile:
    line = line.rstrip()
    nouns = line.split(',')


mood = random.choice(moods)
noun = random.choice(nouns)

password = mood + noun

for i in range(random.randint(1,4)):
    number = str(random.randint(0,9))
    password += number

print(password)
