#!/usr/bin/python3
"""The states module"""
from api.v1.views import app_views
from flask import jsonify, Flask, abort, request
from models import storage
from models.state import State


@app_views.route("/states", methods=['GET'], strict_slashes=False)
def all_states():
    """To return json"""
    for state in storage.all(State).values():
        all_state = state.to_dict()
    return jsonify(all_state)


@app_views.route("/states/<string:state_id>", methods=['GET'],
                 strict_slashes=False)
def all_states_by_id(state_id):
    """To return json"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    return jsonify(abort(404))


@app_views.route("/states/<string:state_id>", methods=['DELETE'],
                 strict_slashes=False)
def del_states_by_id(state_id):
    """To return json"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(abort(404))
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route("/states", methods=['POST'], strict_slashes=False)
def post_states():
    """To return json"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 404)
    state = request.get_json()
    st = State(**state)
    st.save()
    return jsonify(st.to_dict()), 201


@app_views.route("/states/<string:state_id>", methods=['PUT'],
                 strict_slashes=False)
def put_states_by_id(state_id):
    """To return json"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(abort(404))
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict())