import random
import os

path = os.path.dirname( os.path.abspath( __file__ ) )
f = open(path+"\\sentence.txt","r",encoding='utf-8')

# 문장구분용 %
flag = True
# 문장 입력모드 활성화 여부
savemode = False
# 첫번째줄 확인여부
first = True
# 현재 문장번호
nowNum = 0

while True:
    # 파일 첫 문장에 있는 총 명언의 갯수 = total
    if first:
        total = f.readline()
        total = int(total.strip())
        # 랜덤으로 1 ~ total 까지 번호 하나 뽑음
        lottory_num = random.randint(1,total)
        # 출력할 명언을 담을 빈문장 변수
        result = ''
        # 파일 첫문장 입력완료
        first = False
        continue

    line = f.readline()
    # 파일 다 읽는경우 (사실 사용할 일 없음)
    if not line: break

    # 문장 구분자 % 를 통해 다른줄 같은문장인지 다른줄 다른문장인지 구분 
    # %이 있으면 새로운 문장 시작 및 기존문장의 끝
    if line[0] == '%':
        flag = True
        nowNum+=1
        # savemode = True 인경우 출력해야하는 문장임으로 더이상 탐색할필요 없이 반복문 빠져나옴
        if savemode:
            break
        continue

    if flag:
        # 현재 문장번호랑 앞에서 랜덤으로 뽑아둔 번호랑 같은경우 savemode = True
        if nowNum==lottory_num:
            savemode = True
        flag = False
    # 출력해야하는 문장이기때문에 문장 result에 저장
    if savemode:
        result+=line
# 출력
print(result.strip())
f.close()
# 지연용
# a = int(input())
