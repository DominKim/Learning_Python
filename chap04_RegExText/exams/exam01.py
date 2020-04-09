'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
# for 문 이용
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
from re import findall
names = []
for i in emp:
    names.append(findall("[가-힣]{3}", i)[0])

print(names)

# list + for문 이용 대량의 데이터 처리 시 빠르게 처리 가능! : [실행문 for 변수 in 열거형객체]
names2 = [findall("[가-힣]{3}", e)[0] for e in emp]
print(names2)