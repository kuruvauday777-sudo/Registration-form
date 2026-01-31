from flask import *
app = Flask(__name__)
@app.route('/')
def name():
    return render_template('rs.html')
if __name__ == '__main__' :
    app.run(debug=True)
  