'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경 
text_lst = [text.lower() for text in texts]
print(text_lst)

# 2. 숫자 제거
text_lst2 = [sub("[0-9]", "", text) for text in text_lst]
print(text_lst2)

# 3. 문장부호 제거
pun_sub = "[,.:;!?]"
text_lst3 = [sub(pun_sub, "", text) for text in text_lst2]
print(text_lst3)

# 4. 영문자 제거
text_lst4 = [sub("[a-z]", "", text) for text in text_lst3]
print(text_lst4)

# 5. 특수문자 제거
spec_sub = "[@#$%^&*()]"
text_lst5 = [sub(spec_sub, "", text) for text in text_lst4]
print(text_lst5)

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)
text_lst6 = [" ".join(text.split()) for text in text_lst5]
print(text_lst6)

