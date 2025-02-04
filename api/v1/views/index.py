#!/usr/bin/python3
"""Holds  the index view for the API."""
from flask import jsonify

from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Returns status of the API"""
    return jsonify(status="OK")


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stat():
    """Returns number of all objects by type"""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    return jsonify(
        amenities=storage.count(Amenity),
        cities=storage.count(City),
        places=storage.count(Place),
        reviews=storage.count(Review),
        states=storage.count(State),
        users=storage.count(User),
    )