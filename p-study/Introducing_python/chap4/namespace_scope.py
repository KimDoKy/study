animal = 'cat'

def change_local():
    animal = 'dog'
    print('locals:', locals())

print(animal)
print()
print(change_local())
print()
print('globals: ', globals())
print()
print(animal)
