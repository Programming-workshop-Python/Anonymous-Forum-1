from flask import Blueprint, jsonify, request

from first.service.BoardService import BoardService

board_controller = Blueprint(name='board_controller', import_name=__name__)

db = []

@board_controller.route("/")
def index():
    return jsonify(
        {
            "msg": "Hello world!"
        }
    ), 200


@board_controller.route("/create_board", methods=['POST'])
def create_board():
    name = request.json.get("name")
    BoardService.create_board(name)
    return jsonify({
        "msg": "Board created"
    }), 201


@board_controller.route("/get_all_boards", methods=['GET'])
def get_all_boards():
    return jsonify({
        "all_boards": BoardService.get_all_boards()
    }), 200


@board_controller.route("/get_board/<id>", methods=['GET'])
def get_board(id):
    return jsonify({
        "board": BoardService.get_board(id)
    }), 200


@board_controller.route("/edit_board/<id>", methods=['PUT'])
def edit_board(id):
    name = request.json.get("name")
    BoardService.edit_board(id, name)
    return jsonify({
        "msg": "Board edited"
    }), 201

