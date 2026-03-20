from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# DASHBOARDS MAIN PAGE
@app.route('/dashboards')
def dashboards():
    return render_template('dashboards.html')


@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html')

@app.route('/dashboard4')
def dashboard4():
    return render_template('dashboard4.html')

@app.route('/dashboard5')
def dashboard5():
    return render_template('dashboard5.html')

@app.route('/dashboard6')
def dashboard6():
    return render_template('dashboard6.html')


# STORIES
@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/story2')
def story2():
    return render_template('story2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
