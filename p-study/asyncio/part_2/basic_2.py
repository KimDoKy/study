# 동기적 처리
import time

def sub_routine_1():
    print('서브루틴 1 시작')
    print('서브루틴 1 중단... 5초간 대기')
    time.sleep(5)
    print('서브루틴 1 종료')

def sub_routine_2():
    print('서브루틴 2 시작')
    print('서브루틴 2 중단... 4초간 대기')
    time.sleep(4)
    print('서브루틴 2 종료')

if __name__ == '__main__':

    sub_routines = [sub_routine_1, sub_routine_2]

    start = time.time()
    for i in range(2):
        sub_routines[i]()
    end = time.time()
    print(f'time taken: {end-start}')
