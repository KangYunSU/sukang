from random import *
import pandas as pd

# 드라마 데이터 - 파일
df = pd.read_csv('Cdrama.csv')
df = pd.DataFrame(df)
# df = df.set_index('제목')

# 컬럼을 리스트로
cols = list(df.columns)

for c in cols:
    # < 보기 >
    Type1 = df[c].astype(str).str.split(',')
    Type1 = Type1.apply(lambda x: pd.Series(x))
    Type1 = Type1.stack()
    Type1 = Type1.drop_duplicates()
    Type1 = [i.replace(" ", "") for i in Type1]
    Type1 = list(set(Type1))

    print(f"{c}(을/를) 골라주세요 => {Type1}")
    print()

    # input 및 입력 오류
    if c == '장르':
        genre = input("오늘 끌리는 장르는? => ")

        if genre not in Type1:
            print('잘 못 입력했습니다. 다시 실행해주세요')
            exit()

    if c == '배우':
        actor = input("배우는? => ")

        if actor not in Type1:
            print('잘 못 입력했습니다. 다시 실행해주세요')
            exit()

    if c == 'OTT':
        OTT = input("OTT는? => ")

        if OTT not in Type1:
            print('잘 못 입력했습니다. 다시 실행해주세요')
            exit()

    if c == '연도':
        year = input("연도는? => ")

        if year not in Type1:
            print('잘 못 입력했습니다. 다시 실행해주세요')
            exit()

# 추천 코드
def drama(g, a, y, o):

    if g in genre:
        genres = df['장르'].str.contains(g)
        genres = df[genres]['제목'].values
        genres = set(genres)

        if a in actor:
            actors = df['배우'].str.contains(a)
            actors = df[actors]['제목'].values
            actors = set(actors)

            if y in year:
                years = (df['연도'] == int(y))
                years = df[years]['제목'].values
                years = set(list(years))

                if o in OTT:
                    OTTs = df['OTT'].str.contains(o)
                    OTTs = df[OTTs]['제목'].values
                    OTTs = set(OTTs)

                    dlist = (genres & actors & years & OTTs)

                    if dlist:
                        print(f'📺 {g} 드라마는 \n 👉 {list(genres)}')
                        print()
                        print(f'❤️ {a} 배우가 출연한 드라마는 \n 👉 {list(actors)}')
                        print()
                        print(f'📅 {y}에 나온 드라마는 \n 👉 {list(years)}')
                        print()
                        print(f'🎬 {o}에 있는 드라마는 \n 👉 {list(OTTs)}')
                        print()
                        print(f'👑 추천 드라마 \n 👉 {choice(list(dlist))}')

                    else:
                        print(f"""
                        😵‍💫 드라마를 찾지 못했어요 \n
                        👇 관련 드라마 리스트를 보여드릴게요 \n
                        📺 {g} 드라마는 
                        👉 {list(genres)} \n
                        ❤️ {a} 배우가 출연한 드라마는  
                        👉 {list(actors)} \n
                        📅 {y}에 나온 드라마는  
                        👉 {list(years)} \n
                        🎬 {o}에 있는 드라마는 
                        👉 {list(OTTs)}
                        """)

drama(genre, actor, year, OTT)