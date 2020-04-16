#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문단 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
import os
print(os.getcwd())
try:
    file = open("./chap07_FileIO/data/ftest.txt", mode = 'r')
    row = []
    text = []
    for i in file.readlines():
        row.append(i.strip())
        for r in i.strip().split(sep= " "):
            text.append(r)
    print("문단내용\n", row, "\n문단수 :", len(row), "\n")
    print("단어내용\n", text, "\n단어 수 :", len(text))

except Exception as e:
    print("예외 발생 : ", e)
finally:
    print("~~종료~~")
    file.close()



