from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Default route
@app.route('/')
@app.route('/category')
def defaultCatalog():
    categories = session.query(Category).all()
    return render_template('category.html', categories = categories)


#Routes to add new category
@app.route('/category/new' , methods=['GET','POST'])
def newCategory():
    if request.method == 'POST':
        newCat = Category(name =  request.form['name'])
        session.add(newCat)
        session.commit()
        flash('Category Created')
        allCategories = session.query(Category).all()
        return render_template('category.html',categories = allCategories)
    else:
        return render_template('newCategory.html')

#Routes to edit category page
@app.route('/category/<int:category_id>/edit', methods=['GET','POST'])
def editRestaurant(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).all()
    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
            session.add(category)
            session.commit()
            flash('Category Successfully Editted')
            categories = session.query(Restaurant).all()
        return render_template('categories.html',categories=categories)
    else:
        return render_template('editcategory.html',category_id=category_id,category=category)

#Routes to delete category page
@app.route('/category/<int:category_id>/delete', methods=['GET','POST'])
def deleteRestaurant(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).all()
    if request.method == 'POST':
        session.delete(category)
        session.commit()
        flash('Category Successfully Deleted')
        categories = session.query(Category).all()
        return render_template('categories.html',categories=categories)
    else:
        return render_template('deletecategory.html',category_id=category_id,category=category)

#launching the application
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0',port=8001)
