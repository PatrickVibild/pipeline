from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  <p> We have make some changes!!! YUPI YUPI YEIIIII !! </p>
  <p> Lets code this shit out </p>
  <p> hello DEMIRA its me PATRICK!!!! </p>
  <p> lets trigger the pipeline!!! </p>
  """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
