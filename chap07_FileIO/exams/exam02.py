'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

# [우편번호]tab[도/시]tab[구]tab[동]
# 135-806	서울	강남구	개포1동 경남아파트		1
# [우편번호]tab[도/시]tab[구]tab[동]tab[세부주소]
# 135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
try :
    file = open("./chap07_FileIO/data/zipcode.txt", mode='r', encoding='utf-8')
    lines = file.readline() # 첫줄 읽기 
    dong = [] # 서울시 동 저장 list

    # 내용채우기
    while lines:
        addr = lines.split("\t")
        if addr[1] == "서울":
            dong.append(addr[3].split(sep= " ")[0])
        lines = file.readline()

    dong2 = set(dong)
    final_dong = list(dong2)
    final_dong.sort(reverse= False)
    print("서울시 전체 동 개수 =", len(final_dong))
    for i in range(len(final_dong)):
        print("[" + final_dong[i] + "]", end="")
        if i % 10 == 0 and i != 0:
            print()
    
except Exception as e :
    print('예외발생 :', e)
    

final_dong
