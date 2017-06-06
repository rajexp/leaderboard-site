from flask import Flask, render_template, request, redirect, url_for, abort, session
# from flask.ext.assets import Environment, Bundle
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34DD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from . import models as m
@app.route('/')
def home():
    users = m.User.query.order_by(m.User.score.desc(),m.User.guesses).all()[:10]
    #return render_template('message.html', username=user.username,message=user.message)
    return render_template('index.html', users=users)
@app.route('/update', methods=['POST'])
def signup():
    user=m.User(request.form['username'],request.form['score'],request.form['guesses'],request.form['country'])
    m.db.session.add(user)
    m.db.session.commit()
    return request.form['username']
    
@app.route('/search',methods=['POST'])
def search():
    users = m.User.query.filter_by(username=request.form['term']).order_by(m.User.score.desc(),m.User.guesses).all()
    return render_template('search.html', users=users)
    
@app.route('/download')
def download():
    return render_template('download.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/leaderboard/<int:i>',methods=['GET','POST'])
def leader(i=1):
    print (i)
    _offset=10*(i-1)
    print(_offset)
    users = m.User.query.order_by(m.User.score.desc(),m.User.guesses).offset(_offset).all()[:10]
    if (_offset==0):
        return render_template('index.html', users=users)
    else:
        return render_template('leaderboard.html',users=users, _offset= _offset,i=i)
    #return render_template('message.html', username=user.username,message=user.message)
if __name__ == '__main__':
    app.debug=True
    app.run()