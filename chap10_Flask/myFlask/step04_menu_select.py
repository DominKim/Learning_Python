'''
get vs post
 - 파라미터 전송 방식
 - get : url에 노출(소량)
 - post : body에 포함되어 전송(대량)

 <작업순서>
 1. index 페이지 : 메뉴 선택(radio or select)
 2. flask server 파라미터 받기(메뉴 번호)
 3. 메뉴 번호 따라서 각 페이지 이동
 '''

# db 연결 객체 생성 함수
def db_conn():
    import cx_Oracle
    # db 연결 객체 생성
    conn = cx_Oracle.connect("scott/tiger@localhost:32769/xe")
    # SQL 실행 객체 생성
    cursor = conn.cursor()
    return conn, cursor

def select_func():
    sql = "select * from goods"
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
    return render_template("/app04/index.html")

@app.route("/select", methods = ["GET", "POST"])
def select():
    if request.method == 'GET':
        menu = int(request.args.get("menu"))
        # name = request.args.get("name")
        print("menu :", menu)

    if menu == 1: # 전체 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data = data, size = size)

    if menu == 2: # 레코드 추가
        return render_template("/app04/insert_form.html")

    if menu == 3:
        return render_template("/app04/update_form.html")
    # delete_form(code) -> get -> flask server(파라미터) -> delete
    if menu == 4:
        return render_template("/app04/delete_form.html")

@app.route("/insert", methods = ["GET", "POST"])
def insert():
    try:
        if request.method == 'POST':
            code = int(request.form["code"])
            name = request.form["name"]
            su = int(request.form["su"])
            dan = int(request.form["dan"])

            # 레코드 삽입
            conn, cursor = db_conn()
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()
            cursor.close();conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", e_info = e)

@app.route("/update", methods=["POST", "GET"])
def update():
    try:
        if request.method == 'POST':
            code = int(request.form["code"])
            # name = request.form["name"]
            su = int(request.form["su"])
            dan = int(request.form["dan"])

            # 레코드 삽입
            conn, cursor = db_conn()
            sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close();conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", e_info = e)

@app.route("/delete", methods = ["POST", "GET"])
def delete():
    try:
        if request.method == "GET":
            code = int(request.args.get("code"))
            conn, cursor = db_conn()
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close();conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data = data, size=size)

    except Exception as e:
        return render_template("/app04/error.html", e_info = e)

if __name__ == "__main__":
    app.run()
