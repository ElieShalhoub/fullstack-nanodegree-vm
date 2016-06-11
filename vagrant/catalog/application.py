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
    category = session.query(Category).first()
    return render_template('category.html', category = category)
 

@app.route('/category/new' , methods=['GET','POST'])
def newCatalog():
	#if request.method == 'POST':
		newCat = Category(name = "Football")
		session.add(newCat)
		session.commit()
		#flash('New category [%s] inserted' %category.name)
		#return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
		return "added successfully"
	#else:
	#return render_template('newmenuitem.html',restaurant_id=restaurant_id
	#	return "___"


#launching the application
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0',port=8001)