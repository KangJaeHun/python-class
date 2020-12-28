file = open('basic.txt', 'w')

file.write('Hello Python Programming...!!!')
file.close()

with open('basic.txt', 'w') as file:
    file.write('Hell Python Programmin....~!!!')

with open('basic.txt', 'r') as file:
    contents = file.read()

print(contents)


import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
    for i in range(1000):

        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.radrange(40,100)
        height = random.randrange(140 , 200)

        file.write("{},{},{}\n".format(name,weight,height))
        