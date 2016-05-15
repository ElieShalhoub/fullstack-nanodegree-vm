from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#Default app route
#Routes to all restaurants page
@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    return "This page will show all my restaurants"

#Routes to add restaurant page
@app.route('/restaurant/new')
def newRestaurant():
    return "This page will be for making a new restaurant"

#Routes to edit restaurant page
@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will be for editing restaurant %s" %restaurant_id

#Routes to delete restaurant page
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will be for deleting restaurant %s" %restaurant_id

#Default restaurant menu route
#Routes to the restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page is the menu for restaurant %s" %restaurant_id

#Routes to add menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page is for making a new menu item for restaurant %s" %restaurant_id

#Routes to edit menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page is for editing menu item %s" %menu_id

#Routes to delete menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "This page is for deleting menu item %s" %menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000 )
