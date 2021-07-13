from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "helloWorld"


@app.route('/playground')  
def play1():

    return render_template('index.html', box=3, color="#9fc5f8")


@app.route('/playground/<x>')
def play2(x):

    return render_template('index.html', box=int(x), color="#9fc5f8")



@app.route('/playground/<x>/<color>')
def play2_color(x, color):
    
    return render_template('index.html', box=int(x), color=color)


if __name__ == '__main__':   
    app.run(debug=True)    

