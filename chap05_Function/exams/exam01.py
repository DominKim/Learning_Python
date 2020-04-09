'''
문1) Start counter 문제  

height : 3 <- 키보드 입력 
*
**
***
start 개수 : 6 
'''

# 함수 정의
def StarCount(height):
    
    s_cnt = 0 # 별 개수 카운트
    
    for i in list(range(1, height + 1)):
        s_cnt += i
        print("*"*i)
    
    return s_cnt

# 키보드 입력 
height = int(input('height : ')) # 층 수 입력 

# 함수 호출 및 start 개수 출력  
print('start 개수 : %d'%StarCount(height))