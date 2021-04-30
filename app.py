from flask import Flask,redirect,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import pyttsx3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretct'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
admin = Admin(app)
engine = pyttsx3.init()

class posts(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    sub_title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False,default=datetime.now())
    img = db.Column(db.String(30), nullable=False)
    comments = db.Column(db.String(30), nullable=False)
admin.add_view(ModelView(posts,db.session)) 
@app.route('/create',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        category = request.form['category']
        sub_title = request.form['sub_title']
        new_post = posts(title=title , content=content,sub_title=sub_title,author=author,category=category, date_posted = datetime.now(),img = 'jjjj',comments='jfk')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    else:
        all_posts = posts.query.all()

        return render_template('index.html',posts = all_posts)
@app.route('/')
def home():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('home.html', posts = all_posts)  
@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.query.filter_by(id=post_id).one()

    return render_template('post.html', post = post)
@app.route('/movies', methods = ['GET','POST']) 
def movies():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('movies.html', posts = all_posts) 

@app.route('/tech') 
def tech():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('tech.html', posts = all_posts) 
@app.route('/Entertainment') 
def entertainment():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('entertainment.html', posts = all_posts) 
@app.route('/Sports') 
def sports():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('sports.html', posts = all_posts) 
@app.route('/News') 
def news():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('news.html', posts = all_posts) 
@app.route('/Music') 
def music():
    all_posts = posts.query.order_by(posts.date_posted.desc()).all() 
    return render_template('music.html', posts = all_posts) 
if __name__ == "__main__":

    app.run(debug=True)
