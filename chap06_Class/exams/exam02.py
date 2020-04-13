'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자  : 객체 + 동적멤버 생성
        
        분산 함수(var_func)
            var = sum((x - mu)**2) / n - 1
        
        표준편차 함수(std_func)
            std = sqrt(var)
        
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]
class Scattering:
    tot = 0
    def __init__(self, x):
        self.x = x # 동적 멤버변수 생성

    def var_func(self):
        for i in self.x:
            self.tot += ((i - mean(self.x))) ** 2
        self.var = self.tot / (len(self.x) - 1)
        self.std_func()
        self.info()


    def std_func(self):
        self.std = sqrt(self.var)

    def info(self):
        print("분산 :", self.var)
        print("표준편차 :", self.std)

obj = Scattering(x)
obj.var_func()
# obj.var : 멤버변수는 멤버메서드를 통해 계산 후에 멤버변수 생성 후 호출 가능!!!!
    
    



