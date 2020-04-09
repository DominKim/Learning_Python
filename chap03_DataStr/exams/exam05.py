'''
step04, 05 문제 

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict  
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']
position2 = set(position)
position3 = list(position2)
print(position3)

# 문2)
dataset = {}
for i in position3:
    cnt = 0
    for k in range(len(position)):
        if i == position[k]:
            cnt += 1
    dataset[i] = cnt
print(dataset)

posi_wc = {}
for i in position:
    if i in wc:
        wc[i] +=1
    else:
        wc[i] = 1
print(wc)

posi_wc2 = {}
for i in position:
    posi_wc2[i] = posi_wc2.get(i, 0) + 1
print(posi_wc2)