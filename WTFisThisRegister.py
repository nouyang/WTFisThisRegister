# all the imports
import sqlite3, os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
try:
    from databaseconfig import secretkey, username, password
    SECRET_KEY, USERNAME, PASSWORD  = secretkey, username, password
    DEBUG = True
except ImportError: #we are running foreman or on heroku
    SECRET_KEY = os.environ.get('SECRETKEY') 
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    DEBUG = False

# configuration
DATABASE = '/tmp/flaskr.db'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_search():
  return render_template('search.html')

@app.route('/search', methods=['POST'])
def search_entries():
    keyword = request.form['searchterm']
    cur = g.db.execute('select helptext from entries where keyword = ?',
                 [keyword])
    result = [dict(keyword=keyword, helptext=row[0]) for row in cur.fetchall()]
    return render_template('search.html', result=result)

@app.route('/entries')
def show_entries():
    cur = g.db.execute('select keyword, helptext from entries order by id desc')
    entries = [dict(keyword=row[0], helptext=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (keyword, helptext) values (?, ?)',
                 [request.form['keyword'], request.form['helptext']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/delete', methods=['POST'])
def delete_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('delete from entries where keyword = ?', [request.form['entry_to_delete']])
    g.db.commit()
    flash('Entry was successfully removed')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_search'))



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


