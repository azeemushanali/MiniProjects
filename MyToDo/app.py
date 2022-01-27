from flask import Flask, redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@dns/database'
db = SQLAlchemy(app)

class ToDo(db.Model):
    
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    
    allTodo = ToDo.query.all()
    print(allTodo)
    return render_template("index.html",allTodo = allTodo)
    #return "Hello World"

@app.route('/testadd')
def testAdd():
    todo = ToDo(title="Test1",desc="Started testing")
    db.session.add(todo)
    db.session.commit()
    return "Adding Successfull"

@app.route('/update_<int:sno>',methods=["POST","GET"])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        description = request.form['desc']
        todo = ToDo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = description
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = ToDo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo = todo)

@app.route('/delete_<int:sno>')
def delete(sno):
    todo = ToDo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)