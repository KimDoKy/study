# 외부 어떤 API
class OutsideAPI:
    def do_something(self):
        return '외부 API로 어떠한 처리를 실행한 결과'

# 단위 테스트를 하려는 처리
def my_processing():
    api = OutsideAPI()
    return api.do_something() + '를 사용하여 무엇인가를 하고 있다.'

if __name__ == "__main__":
    print(my_processing())
