from random import *
import pandas as pd

# 음식 데이터 - 파일
fooddata = pd.read_excel('오늘 뭐 먹지\FoodData2.xlsx')

# 나라별: Type1
Type1 = fooddata.drop_duplicates(['음식종류'])
Type1 = Type1['음식종류'].values

print(f"골라주세요 => {Type1}")
print()
food = input("오늘 끌리는 음식 종류는? => ")
print()

# food 입력 오류
if food not in Type1:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 맵기 정도: Type2
Type2 = fooddata.drop_duplicates(['맵기'])
Type2 = Type2['맵기'].values

print()
print(f"골라주세요 => {Type2}")
print()
spicy = input("매운 정도는? => ")
print()

# spicy 입력 오류
if spicy not in Type2:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 추천 코드
def type_choice(food1, spicy1):

    fs = ''

    fstype = fooddata.loc[(fooddata['맵기'] == spicy1) & (fooddata['음식종류'] == food1)]
    fstype = fstype['음식이름'].values

    if fs not in fstype:
        fs += fstype
        
    if fs in fstype:
        fstype = choice(fstype)
        print(f'{fstype} 는/은 어때요?')

    else: 
        print("없어요ㅠ")

type_choice(food, spicy)