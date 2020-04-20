'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  600000 <- 수량, 단가 수정
4 HDTV 2 1500000  <- 수량 수정
전체 레코드 수 : 4
'''
import sqlite3

try :
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")
    cursor = conn.cursor()
    '''
    # 전자레인지 수량, 단가 수정
    su = int(input("전자레인 수량 수정 : "))
    dan = int(input("전자레인 단가 수정 : "))
    sql = f"update goods set su = {su}, dan = {dan} where code = 3"
    cursor.execute(sql)
    conn.commit()

    # HDTV 수량수정
    su = int(input("HDTV 수량 수정 : "))
    sql = f"update goods set su = {su} where code = 4"
    cursor.execute(sql)
    conn.commit()
    '''

    # 테이블 출력
    cursor.execute("select * from goods")
    dataset = cursor.fetchall()
    print("\t [ goods 테이블 현황]")
    for row in dataset:
        print("%d\t%s\t%d\t%d" %(row))

except Exception as e :
    print("예외발생", e)

finally:
    cursor.close()
    conn.close()



