from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem
#connect to restaurant database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Fake Restaurants
#restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

#restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
#items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
#item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



#Default app route
#Routes to all restaurants page
@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html',restaurants=restaurants)

#Routes to add restaurant page
@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        restaurant = Restaurant(name = request.form['name'])
        session.add(restaurant)
        session.commit()
        restaurants = session.query(Restaurant).all()
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('newrestaurant.html')

#Routes to edit restaurant page
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    restaurants = session.query(Restaurant).all()
    if request.method == 'POST':
        if request.form['name']:
            restaurant.name = request.form['name']
            session.add(restaurant)
            session.commit()
            restaurants = session.query(Restaurant).all()
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('editrestaurant.html',restaurant_id=restaurant_id,restaurant=restaurant)

#Routes to delete restaurant page
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    restaurants = session.query(Restaurant).all()
    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        restaurants = session.query(Restaurant).all()
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('deleterestaurant.html',restaurant_id=restaurant_id,restaurant=restaurant)


#Default restaurant menu route
#Routes to the restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html',restaurant = restaurant, items = items)


#Routes to add menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        menuItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'] , course = request.form['course'],restaurant_id=restaurant_id)
        session.add(menuItem)
        session.commit()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('newmenuitem.html',restaurant_id = restaurant_id)

#Routes to edit menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
            item.description = request.form['description']
            item.price = request.form['price']
            item.course = request.form['course']
            session.add(item)
            session.commit()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('editmenuitem.html',restaurant_id=restaurant_id,item=item, menu_id=menu_id)


#Routes to delete menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('deletemenuitem.html',restaurant_id=restaurant_id,item=item, menu_id=menu_id)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000 )
