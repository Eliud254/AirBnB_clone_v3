#!/usr/bin/python3
"""
Starts Flask web application
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Display  status response"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
# This code has the advantage of not returning non-existing objects
def stats():
    """Display  number of each objects by type"""
    all_classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
                   "Review": "reviews", "State": "states", "User": "users"}
    return jsonify({v: storage.count(k) for k, v in all_classes.items()
                    if storage.count(k)})
