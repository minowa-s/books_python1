from flask import Flask, render_template, request
import random
import db

app = Flask(__name__)

@app.route('/')
def menu_top():
    return render_template('index.html')

@app.route('/registerbook')
def regi_book():
    return render_template('regibook.html')

@app.route('/registerbook_exe', methods=['POST'])
def regi_book_exe():
    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    pages = request.form.get('pages')
    
    
    db.insert_book(title, author, publisher, pages)
    
    return render_template('regisucb.html')
    
@app.route('/disbook')
def dis_book():
    book_list = db.dis_all_book()
    return render_template('list.html', books=book_list)
    
@app.route('/editbook')
def edit_book():
    return render_template('editform.html')

@app.route('/editbook_exe', methods=['POST'])
def edit_book_exe():
    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    pages = request.form.get('pages')
    id = request.args.get('id')
    
    db.edit_book(title, author, publisher, pages,id )
    
    return render_template('editsucb.html')


if __name__ == "__main__":
    app.run(debug=True)
    
    