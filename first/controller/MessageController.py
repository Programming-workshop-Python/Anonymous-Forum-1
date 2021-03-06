from flask import Blueprint, jsonify, request

from first.service.MessageService import MessageService

message_controller = Blueprint(name='message_controller', import_name=__name__)


db = []

@message_controller.route("/")
def index():
    return jsonify(
        {
            "msg": "Hello world!"
        }
    ), 200


@message_controller.route("/create_message_on_tread/<tread_id>", methods=['POST'])
def create_message(tread_id):
    author = request.json.get("author")
    text = request.json.get("text")
    MessageService.create_message(author, text, tread_id)
    return jsonify({
        "msg": "Message created"
    }), 201


@message_controller.route("/get_messages_on_tread/<tread_id>", methods=['GET'])
def get_messages_on_tread(tread_id):
    return jsonify({
        "messages": MessageService.get_messages_by_tread(tread_id)
    }), 200


@message_controller.route("/get_message/<id>", methods=['GET'])
def get_message(id):
    return jsonify({
        "message": MessageService.get_message(id)
    }), 200


@message_controller.route("/delete_message/<id>", methods=['DELETE'])
def delete_message(id):
    MessageService.delete_message(id)
    return jsonify({
        "msg": "Message deleted"
    }), 200




