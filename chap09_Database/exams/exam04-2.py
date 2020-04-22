'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더) : emp_table(no(int), name(varchar(20)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd
import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}
# 칼럼 단위 읽기 
emp = pd.read_csv("./chap09_Database/data/emp.csv", encoding='utf-8')
print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    '''
    sql = """ create or replace table emp_table(
    no int(3) primary key,
    name varchar(20) not null,
    pay int(30))
    """
    cursor.execute(sql)
    print("1. 테이블 생서 완료")
    
    for i in range(len(no)):
        sql = f"insert into emp_table values({no[i]}, '{name[i]}', {pay[i]})"
        cursor.execute(sql)
        conn.commit()
    '''
    check_name = input("조회할 사원 이름 : ")
    sql = f"select * from emp_table where name like '%{check_name}%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for row in data:
            print(" %d  %s  %d" % row)
    else:
        print("조회한 사원이 없습니다.")


except Exception as e:
    print("에러 발생 :", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
    
    
    











