from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

#Default route
@app.route('/')
@app.route('/catalog')
def defaultCatalog():
    #restaurant = session.query(Restaurant).first()
    #items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return "catalog home" 

#launching the application
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0',port=8001)