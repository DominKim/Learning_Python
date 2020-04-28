from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/test.html")

@app.route("/search", methods = ["POST", "GET"])
def google():
    try:
        if request.method == "GET":
            search = request.args.get("search")
            if search:
                url = "http://google.com"
                return webbrowser.open(url)
            else:
                return ""

    except Exception as e:
        print("에러 발생 :", e)
    return "a"



if __name__ == "__main__":
    app.run()