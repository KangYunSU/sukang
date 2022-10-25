from random import *
import pandas as pd

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

# actor 입력 오류
if actor not in Type2:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 연도 : Type3
Type3 = Cdrama['연도']
Type3 = Type3.apply(lambda x: pd.Series(x))
Type3 = Type3.stack()
Type3 = Type3.drop_duplicates()
Type3 = list(Type3)

print()
print(f"골라주세요 => {Type3}")
print()
year = input("연도는? => ")
print()

# year 입력 오류
if int(year) not in Type3:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# OTT : Type4
Type4 = Cdrama['OTT']
Type4 = Cdrama['OTT'].str.split(',')
Type4 = Type4.apply(lambda x: pd.Series(x))
Type4 = Type4.stack()
Type4 = Type4.drop_duplicates()
Type4 = [i.replace(" ", "") for i in Type4]
Type4 = list(set(Type4))

print()
print(f"골라주세요 => {Type4}")
print()
OTT = input("OTT는? => ")
print()

# OTT 입력 오류
if OTT not in Type4:
    print('잘 못 입력했습니다. 다시 실행해주세요')
    exit()

# 추천 코드
def drama(g, a, y, o):

    if g in genre:
        genres = Cdrama['장르'].str.contains(g)
        genres = Cdrama[genres]['제목'].values
        genres = set(genres)

        if a in actor:
            actors = Cdrama['배우'].str.contains(a)
            actors = Cdrama[actors]['제목'].values
            actors = set(actors)

            if y in year:
                years = (Cdrama['연도'] == int(y))
                years = Cdrama[years]['제목'].values
                years = set(list(years))

                if o in OTT:
                    OTTs = Cdrama['OTT'].str.contains(o)
                    OTTs = Cdrama[OTTs]['제목'].values
                    OTTs = set(OTTs)

                    dlist = (genres & actors & years & OTTs)   

                    if dlist & genres:

                        if dlist & actors:
                        
                            if dlist & years:

                                if dlist & OTTs:
                                    print(f'📺 {g} 드라마는 \n 👉 {genres}')
                                    print()
                                    print(f'❤️ {a} 배우가 출연한 드라마는 \n 👉 {actors}')
                                    print()
                                    print(f'📅 {y}에 나온 드라마는 \n 👉 {years}')
                                    print()
                                    print(f'🎬 {o}에 있는 드라마는 \n 👉 {OTTs}')
                                    print()
                                    print(f'👑 추천 드라마 \n 👉 {choice(list(dlist))}')

                    else:
                        print(f'😵‍💫 드라마를 찾지 못했어요')
                        print()
                        print(f'👇 관련 드라마 리스트를 보여드릴게요')
                        print()
                        print(f'📺 {g} 드라마는 \n 👉 {genres}')
                        print()
                        print(f'❤️ {a} 배우가 출연한 드라마는 \n 👉 {actors}')
                        print()
                        print(f'📅 {y}에 나온 드라마는 \n 👉 {years}')
                        print()
                        print(f'🎬 {o}에 있는 드라마는 \n 👉 {OTTs}')

drama(genre, actor, year, OTT)