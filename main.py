from first import app


def register_blueprints(app):
    from first.controller.BoardController import board_controller
    app.register_blueprint(board_controller, url_prefix='/board')
    from first.controller.TreadController import tread_controller
    app.register_blueprint(tread_controller, url_prefix='/tread')
    from first.controller.MessageController import message_controller
    app.register_blueprint(message_controller, url_prefix='/message')


register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='localhost')
