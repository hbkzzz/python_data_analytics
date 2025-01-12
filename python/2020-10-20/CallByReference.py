# 서브 루틴 : func() 함수

def func(x) :
    x[0] = 100
    print('func() : x = ', x, ', id = ', id(x))

# 메인 루틴
x = [1, 2, 3]
print('메인 : x = ', x, ', id = ', id(x))
func(x)
print('메인 : x = ', x, ', id = ', id(x))

# 내장 함수 id()는 변수를 포함하는 모든 객체가 저장된 컴퓨터 메모리의 주소를 나타냄
# 객체를 구별하기 위한 일련번호라고 생각하면 됨 숫자로서 의미가 없음