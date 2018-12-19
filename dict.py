"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")

print("답은 {}".format((iu_score['수학']+iu_score['국어']+iu_score['음악'])/len(iu_score)))

'''
강사님 답
totla_score = 0
for score in iu_score:

'''

score = list(iu_score.values())
print(sum(score)/len(score))


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")

iu = list(score['iu'].values())
iu_result = sum(iu)/len(iu)

ui = list(score['iu'].values())
ui_result = sum(iu)/len(ui)

print(iu_result,ui_result)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 2],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")

chh = list(city.values())
s =[]
for i in range(len(city)):
    s.append(round(sum(chh[i])/len(chh[i]),2))

print("서울 : {sa[0]} \n대전 : {sa[1]} \n광주 : {sa[2]} \n부산 : {sa[3]}".format(sa = s))

# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

maxt = city['서울'][0]
mint = city['서울'][0]
maxCity = ""
minCity = ""

cityList = list(city.values())

for i in range(len(cityList)):
    if maxt < max(cityList[i]):
        maxt = max(cityList[i])
        maxCity = i
    
print(maxCity)
print(cityList)
print(maxt)



# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")

cnt = 0
for i in range(0,3):
    if city['서울'][i] == 2:
        print("네")
        cnt += 1
        break;
        
if cnt == 0:
    print("아니오")