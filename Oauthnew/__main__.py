from flask import Flask, request, render_template, redirect, session
from oauth import Oauth
import webbrowser


app = Flask(__name__)


@app.route("/",methods = ["get"])
def index():
    return redirect(Oauth.discord_login_url)

@app.route("/index.html",methods = ["get"])
def login():
    code = request.args.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    username = user_json.get("id")
    if username == "564250827959566359":
        url = "https://jhcplace.github.io/saucalito/saucalitowebsite/notice.html"
        webbrowser.open(url)
        return "✅ 승인됨"
    return """⛔ 로그인 실패
    이유: 관리자 계정이 아님"""
    url = "https://jhcplace.github.io/saucalito/saucalitowebsite/notice.html"
    webbrowser.open(url)


if(__name__ == "__main__"):
    app.run(debug=True)