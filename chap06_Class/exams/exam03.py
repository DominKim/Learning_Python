'''
문2) 이름, 성별, 나이를 갖는 Person 클래스를 다음과 같이 작성하시오.
 <처리조건>
1. 멤버 변수 : 이름(name), 성별(gender), 나이(age)
  2. 생성자 :  객체 생성 + 이름, 성별, 나이 초기화  
  3. 멤버 함수 : display(이름, 성별, 나이 출력 기능) 
  4. 기타 나머지는 출력 예시 참조         
   
    << 출력 예시 >>  
 이름 입력 : 유관순        
 나이 입력 : 35
 성별(male/female) 입력 : female
 =========================
 이름 : 유관순, 성별 : 여자
 나이 : 35
 =========================
'''

class Person :

    # 생성자 메서드
    def __init__(self, age, name, gender): # 인수 1개 이상 필요
        self.Age = age
        self.Name = name
        self.Gender = gender

    def display(self):
        if self.Gender == "male":
            self.Gender = "남자"
        else:
            self.Gender = "여자"
        print("=" * 10)
        print("이름 : %s, 성별 : %s \n나이 : %d" % (self.Name, self.Gender, self.Age))
        print("=" * 10)
        
# 키보드 입력 
name = input('이름 : ')
age = int(input('나이 : '))
gender = input('성별(male/female) : ')

# 객체 생성과 메서드 호출 
p = Person(age, name, gender) # 생성자 이용 전역변수 초기화 
p.display()

