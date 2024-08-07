from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="John Doe")

if __name__ == '__main__':
    app.run(debug=True)
  <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <h1>Welcome, {{ name }}</h1>
  </body>
</html>
