"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secrecy"

connect_db(app)

@app.route('/api/cupcakes', methods=['GET'])
def list_cupcakes():
    """Get data about all cupcakes and respond with JSON"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    """get data about a single cupcake and respond with JSON - raise 404 if cupcake cannot be found"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

