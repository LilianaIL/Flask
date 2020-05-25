from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/about')
def about():
    name='lili'
    return render_template('about.html', user=name)


app.run()