from first.repository.BoardRepository import BoardRepository


class BoardService:
    @staticmethod
    def create_board(name):
        BoardRepository.create_board(name)

    @staticmethod
    def get_all_boards():
        posts = BoardRepository.get_all_boards()
        return posts
