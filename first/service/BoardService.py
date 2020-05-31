from first.repository.BoardRepository import BoardRepository


class BoardService:
    @staticmethod
    def create_board(name):
        BoardRepository.create_board(name)


    @staticmethod
    def get_all_boards():
        boards = BoardRepository.get_all_boards()
        return boards


    @staticmethod
    def get_board(id):
        board = BoardRepository.get_board(id)
        return board


    @staticmethod
    def edit_board(id, name):
        BoardRepository.edit_board(id, name)
