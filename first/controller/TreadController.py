from flask import Blueprint, jsonify, request

from first.service.TreadService import TreadService

tread_controller = Blueprint(name='tread_controller', import_name=__name__)

db = []

@tread_controller.route("/")
def index():
    return jsonify(
        {
            "msg": "Hello world!"
        }
    ), 200


@tread_controller.route("/create_tread_on_board/<board_id>", methods=['POST'])
def create_post(board_id):
    name = request.json.get("name")
    TreadService.create_tread(name, board_id)
    return jsonify({
        "msg": "Tread created"
    }), 201


