'''
step2 관련 문제 

A형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가하고, vector의 크기를 출력하시오.

          
<출력 예시>
vector 수 : 3
4
2
5
vector 크기 : 3
     
B형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가한다. 
          이후 vector에서 찾을 값을 키보드로 입력한 후 
          해당 값이 vector에 있으면 "YES",  없으면 "NO"를 출력하시오. 
          
<출력 예시>
vector 수 : 5
1
2
3
4
5
3
YES

vector 수 : 3
1
2
4
3
NO
'''

# A형 문제
dataset = []
size = int(input('vector 수 : ')) # vector 크기 입력
for i in range(size):
    dataset.append(i + 1)
print("vector의 수는 %d이고, 크기는 %d이다." % (size, len(dataset)))


'''
B형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가한다. 
          이후 vector에서 찾을 값을 키보드로 입력한 후 
          해당 값이 vector에 있으면 "YES",  없으면 "NO"를 출력하시오. 
'''
dataset = []
size = int(input('vector 수 : ')) # vector 크기 입력
for i in range(size):
    dataset.append(i + 1)
print("vector의 수는 %d이고, 크기는 %d이다." % (size, len(dataset)))
search = int(input("찾을 수 입력 : "))
if search in dataset:
    print("YES")
else:
    print("NO")
while True:
    dataset = []
    size = int(input("vector 수 : "))
    for i in range(size):
        dataset.append(int(input("숫자 입력 : ")))
    print("vector 수 : 3")
    for i in dataset:
        print(i)
    while True:
        search = int(input("찾을 수 입력 : "))
        if search in dataset:
            print("YES")
            break
        else:
            print("NO")
    break