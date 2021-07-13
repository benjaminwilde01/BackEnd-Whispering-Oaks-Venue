from flask import Blueprint, jsonify, request
import models
from playhouse.shortcuts import model_to_dict
from peewee import IntegrityError

visitor = Blueprint('whispering_oaks', 'visitor')


@visitor.route('/', methods=['GET'])
def get_all_visitors():
    try:
        db_whispering_oaks = models.Visitor.select()
        visitors = []

        for visitor in db_whispering_oaks:
            visitors.append(model_to_dict(visitor))

        return jsonify(data=visitors, status={'code': 200, 'message': 'Success'})

    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resource'})


@visitor.route('/', methods=['POST'])
def create_visitor():
    payload = request.get_json()

    try:
        visitor = models.Visitor.create(
            name=payload['name'], number=payload['number'], email=payload['email'], date=payload['date'], message=payload['message'])

        return jsonify(data=model_to_dict(visitor), status={'code': 201, 'message': 'Success'})

    except IntegrityError:
        print('Invalid Schema was sent')

        return jsonify(data={}, status={'code': 401, 'message': 'Invalid visitor schema'})
