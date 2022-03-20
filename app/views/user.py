from app import app
from flask import request, jsonify
from app.services.user import UserService
import logging

logger = logging.getLogger(__name__)

class UserRoutes:

    @app.route('/api/v1/users', methods=['GET', 'POST'])
    def users():
        """ gets and creates users """
        try:
            if request.method == 'GET':
                return jsonify({"users":UserService.get_users()}),200
            else:
                received_json_data = request.get_json()
                if received_json_data:
                    return jsonify({"user":UserService.create_user(received_json_data)}),200
                else:
                    return jsonify({"error":"request has no body."}),400
        except Exception as e:
            logger.exception(f"An error has occured: {str(e)}")
            return jsonify({"error":f"An error has occured: {str(e)}"}),400


            