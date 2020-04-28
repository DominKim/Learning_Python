'''

'''
def db_conn():
    import cx_Oracle
    # db 연결 객체 생성
    conn = cx_Oracle.connect("scott/tiger@localhost:32769/xe")
    # SQL 실행 객체 생성
    cursor = conn.cursor()
    return conn, cursor

def select_func():
    sql = "select * from doctors"
    conn, cursor = db_conn() # db 연동 객체
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close(); conn.close()
    return data

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app05/main.html")

@app.route("/docForm")
def docForm():
    return render_template("/app05/docForm.html")

@app.route("/docPro", methods = ["GET", "POST"])
def docPro():

    if request.method == "POST":
        doc_id = int(request.form["id"])
        major = request.form["major"]

        conn, cursor = db_conn()
        sql = f"select * from doctors where doc_id = {doc_id} and major_treat = '{major}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row: # login 성공 -> 진료정보
            # print("login 성공") : 601, '내과'
            sql = f"""select d.doc_id, t.pat_id, TREAT_CONTENTS, TREAD_DATE
            from doctors d inner join treatments t 
            on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                size = len(data)
            return render_template("/app05/docPro.html", dataset = data, size = size)
        else: # login 실패
            print("login 실패")
            return render_template("/app05/error.html", info = "id 또는 진료과목 확인")

@app.route("/nurseForm")
def nurseForm():
    return render_template("/app05/nurseForm.html")

@app.route("/nursePro", methods = ["POST", "GET"])
def nursePro():
    # 파라미터(id) 받기 -> id 유무 파악 -> 있으면 : 간호사 환자 조인
    # 없으면 : error.html
    if request.method == "POST":
        nur_id = int(request.form["id"])
        conn, curosr = db_conn()
        sql = f"select * from nurses where nur_id = {nur_id}"
        curosr.execute(sql)
        row = curosr.fetchone()
        if row:
            sql = f"""select n.nur_id, p.doc_id, p.pat_name, p.pat_phone 
            from nurses n inner join patients p
            on n.nur_id = p.nur_id and n.nur_id = {nur_id}"""
            curosr.execute(sql)
            data = curosr.fetchall()
            if data:
                size = len(data)
            else:
                size = 0
            return render_template("/app05/nursePro.html", dataset = data, size = size)
        else:
            return render_template("/app05/error.html", info="id 확인")


# 프로그램 시작점
if __name__ == "__main__":
    app.run()
