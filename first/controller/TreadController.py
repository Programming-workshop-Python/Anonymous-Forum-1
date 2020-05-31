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
def create_tread(board_id):
    name = request.json.get("name")
    TreadService.create_tread(name, board_id)
    return jsonify({
        "msg": "Tread created"
    }), 201


@tread_controller.route("/get_treads_on_board/<board_id>", methods=['GET'])
def get_treads_on_board(board_id):
    return jsonify({
        "treads": TreadService.get_tread_by_board(board_id)
    }), 200


@tread_controller.route("/get_tread/<id>", methods=['GET'])
def get_tread(id):
    return jsonify({
        "tread": TreadService.get_tread(id)
    }), 200


@tread_controller.route("/edit_tread/<id>", methods=['PUT'])
def edit_tread(id):
    name = request.json.get("name")
    board_id = request.json.get("board_id")
    TreadService.edit_tread(id, name, board_id)
    return jsonify({
        "msg": "Tread edited"
    }), 201





