from flask import Flask, render_template, redirect, url_for, session, flash
from forms import LoginForm, AddBookForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a-hard-to-guess-random-string'

# Hardcoded credentials
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'books123'


BOOKS = [
    {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965},
    {'title': "Ender's Game", 'author': 'Orson Scott Card', 'year': 1985},
    {'title': 'The Martian', 'author': 'Andy Weir', 'year': 2011},
]

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('books'))

    form = LoginForm()

    if form.validate_on_submit():  # FlaskForm from Flask-WTF
        # Checking (hardcoded) credentials
        if form.username.data == VALID_USERNAME and form.password.data == VALID_PASSWORD:
            session['logged_in'] = True
            flash('Successfully logged in. Welcome!', 'success')
            return redirect(url_for('books'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html', form=form)


@app.route('/books', methods=['GET', 'POST'])
def books():
    # prevent access if not logged in
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    form = AddBookForm()

    # Handling the Add Book form
    if form.validate_on_submit():
        new_book = {
            'title': form.title.data,
            'author': form.author.data,
            'year': form.year.data
        }
        BOOKS.append(new_book)
        flash(f'"{new_book["title"]}" was added successfully!', 'success')

        return redirect(url_for('books'))

    return render_template('books.html', books=BOOKS, form=form)


@app.route('/logout')
def logout():
    session.clear()  # Removes 'logged_in' from session so session.get('logged_in') will return False
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)