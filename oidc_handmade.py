from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route("/openid-configuration")
def metadata():
    f = open("metadata.txt", "r")
    return f.read()

@app.route("/authorize")
def authorize():
    args = request.args
    redirect_uri = args.get("redirect_uri")
    state = args.get("state")
    oidc_login_url = redirect_uri + '?code=2GTUT79agtpkR6M7EM-WQPbL55kmeMTsrZTRp18snd8&state=' + state
    return redirect(oidc_login_url, code=302)


@app.route("/token", methods = ['POST'])
def token():
    f = open("token.txt", "r")
    return f.read()
    
@app.route("/userinfo")
def userinfo():
    f = open("userinfo.txt", "r")
    return f.read()
    