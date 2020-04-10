'''
 문4) 패토리얼(Factorial) 계산 함수를 정의하시오.
     예) 5! -> 5*4*3*2*1 : 120
'''

def Factorial(n):
    if n == 1:
        return 1
    else:
        result = n * Factorial(n - 1)
        return result

    
result_fact = Factorial(5)  
print()  
print('패토리얼 결과:', result_fact) #  패토리얼 결과: 120
a = [1, 2 ,3 ,4]
a[:-1]

b= [7, 69, 2, 221, 8974]
print(tot2, tot1)

my_id = "1234"
my_money = 0
bal = bal + insert