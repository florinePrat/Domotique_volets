from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['temp']
  p = result['etatVolet']
  subprocess.Popen("python3 templates/main_ASAIoT.py "+n+" "+p, shell=True)
  return render_template("resultat.html", temp=n, etatVolet=p)

app.run(debug=True)
