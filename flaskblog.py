from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b31455a7ab8aa33bd8d6286450ac2362'

posts = [
    {
        'author': 'Corey Schefer',
        'title': 'First Blog Title',
        'content': 'First Blog Content',
        'date_posted': 'April 23, 2019'
    }, {
        'author': 'Suyog Shimpi',
        'title': 'Second Blog Title',
        'content': 'Second Blog Content',
        'date_posted': 'April 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Us')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'suyog@mail.com' and form.password.data == 'suyog':
            flash('You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please, check username or password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
