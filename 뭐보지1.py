from random import *
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# 드라마 데이터 - 파일
Cdrama = pd.read_csv('Cdrama.csv')

# 장르: Type1
Type1 = Cdrama['장르'].str.split(',')
Type1 = Type1.apply(lambda x: pd.Series(x))
Type1 = Type1.stack()
Type1 = Type1.drop_duplicates()
Type1 = list(Type1)
Type1 = [i.replace(' ', '') for i in Type1]

print(f"골라주세요 => {Type1}")
print()
genre = input("오늘 끌리는 장르는? => ")
print()

# food 입력 오류
if genre not in Type1:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 배우 : Type2
Type2 = Cdrama['배우'].str.split(',')
Type2 = Type2.apply(lambda x: pd.Series(x))
Type2 = Type2.stack()
Type2 = Type2.drop_duplicates()
Type2 = list(Type2)
Type2 = [i.replace(' ', '') for i in Type2]

print()
print(f"골라주세요 => {Type2}")
print()
actor = input("배우는? => ")
print()

# spicy 입력 오류
if actor not in Type2:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 추천 코드
def drama(g, a):

    if g in genre:
        genres = Cdrama['장르'].str.contains(g)
        genres = Cdrama[genres]['제목'].values
        genres = set(genres)

        if a in actor:
            actors = Cdrama['배우'].str.contains(a)
            actors = Cdrama[actors]['제목'].values
            actors = set(actors)

            dlist = (genres & actors)

            if dlist & genres:

                if dlist & actors:
                    print(f'📺 {g} 드라마는 \n 👉 {list(genres)}')
                    print()
                    print(f'❤️ {a} 배우가 출연한 드라마는 \n 👉 {list(actors)}')
                    print()
                    print(f'👑 추천 드라마 \n 👉 {choice(list(dlist))}')

            else:
                print(f'😵‍💫 {g} 드라마에 {a} 배우가 나온 드라마를 찾지 못했어요')
                print()
                print(f'👇 {g} 드라마와 {a} 배우가 출연한 드라마를 알려드릴게요')
                print()
                print(f'📺 {g} 드라마는 \n 👉 {list(genres)}')
                print()
                print(f'❤️ {a} 배우가 출연한 드라마는 \n 👉 {list(actors)}')

drama(genre, actor)