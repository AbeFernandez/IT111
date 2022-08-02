from flask import Flask, render_template, request

app = Flask(__name__)

solution = "grocery"
word = [char for char in solution]
word = list(dict.fromkeys(word))


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)  
