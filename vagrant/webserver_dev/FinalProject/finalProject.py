from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



#Default app route
#Routes to all restaurants page
@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    return render_template('restaurants.html',restaurants=restaurants)

#Routes to add restaurant page
@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('newrestaurant.html')

#Routes to edit restaurant page
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('editrestaurant.html',restaurant_id=restaurant_id,restaurant=restaurant)

#Routes to delete restaurant page
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    if request.method == 'POST':
        return render_template('restaurants.html',restaurants=restaurants)
    else:
        return render_template('deleterestaurant.html',restaurant_id=restaurant_id,restaurant=restaurant)


#Default restaurant menu route
#Routes to the restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return render_template('menu.html',restaurant = restaurant, items = items)


#Routes to add menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('newmenuitem.html',restaurant_id = restaurant_id)

#Routes to edit menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('editmenuitem.html',restaurant_id=restaurant_id,item=item, menu_id=menu_id)


#Routes to delete menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        return render_template('menu.html',restaurant = restaurant, items = items)
    else:
        return render_template('deletemenuitem.html',restaurant_id=restaurant_id,item=item, menu_id=menu_id)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000 )
