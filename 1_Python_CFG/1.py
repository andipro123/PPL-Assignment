import random
sideone = ['Tiger', 'goat', 'grass']
sidetwo = []
present = True


def valid_check(side):
    if ('grass' in side) and ('goat' in side):
        return False
    elif ('goat' in side) and ('Tiger' in side):
        return False
    else:
        return True


count = 0
while(not(('goat' in sidetwo) and ('grass' in sidetwo) and ('Tiger' in sidetwo))):
    count +=1
    if(present == True):
        animal = random.choice(sideone)
        sideone.remove(animal)
        print("______", animal)
        if(valid_check(sideone) == False):
            sideone.append(animal)
        else:
            sidetwo.append(animal)
            present = False
    else:
        if(valid_check(sidetwo) == False):
            animal = sidetwo.pop(0)
            sideone.append(animal)
        present = True
    print("side: ", present)
    print("sideone: ", sideone)
    print("sidetwo: ", sidetwo)
    print("__" * 20)
print(count)