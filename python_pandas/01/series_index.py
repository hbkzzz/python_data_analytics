import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2020-11-09', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
print()

# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print()
print(val)