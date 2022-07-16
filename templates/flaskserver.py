from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def main():
    tex=""
    for line in open("Filename","r").readlines:
        tex+=line
    return tex