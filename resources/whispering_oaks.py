from flask import Blueprint, jsonify, request

import models

from playhouse.shortcuts import model_to_dict


visitor = Blueprint('whispering_oaks', 'visitor')


@visitor.route('/', methods=['GET'])
def get_all_visitors():
    try:
        db_whispering_oaks = models.Visitor.select()
        visitors = []

        for visitor in db_whispering_oaks:
            visitors.append(model_to_dict(visitor))
        
        print(visitors)
        return jsonify(data=visitors, status={'code': 200, 'message': 'Success'})
    
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resource'})

