from flask import Flask, render_template,request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.db'

db = SQLAlchemy(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    done = db.Column(db.Boolean)

    
@app.route('/')
def index():
    testeo = test.query.all()
    return render_template('index.html', testeo = testeo)


@app.route('/create-test', methods=['POST'])
def create():
    new_test = test(name=request.form['name'],email=request.form['email'],address=request.form['address'],phone=request.form['phone'], done= False)
    db.session.add(new_test)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    rowdel = test.query.filter_by(id=int(id)).first()
    rowdel.done = not(rowdel.done)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)