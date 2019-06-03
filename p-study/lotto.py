from random import shuffle
from time import sleep

game_count = input('숫자를 입력하세요')

for i in range(int(game_count)):
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print(f'로또번호[{i+1}] : ')
    print(ret)
    sleep(1)
