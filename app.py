from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pytesser


app = Flask(__name__)

app.secret_key = 'hi'

@app.route("/")
def main():
    return s

if __name__ == '__main__':
    app.debug = True
    app.run()
    
