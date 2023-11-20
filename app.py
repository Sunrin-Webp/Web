from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do_the_login()
        flash('Login requested for user {}, remember_me={}'.format(
            request.form['username'], request.form['remember_me']))
        return redirect(url_for('index'))
    else:
        return render_template('login.html')
    
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(debug=True, port=5000)