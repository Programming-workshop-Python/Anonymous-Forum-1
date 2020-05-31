from first.repository.TreadRepository import TreadRepository


class TreadService:
    @staticmethod
    def create_tread(name, board_id):
        TreadRepository.create_tread(name, board_id)

    @staticmethod
    def get_tread_by_board(board_id):
        treads = TreadRepository.get_tread_by_board(board_id)
        return treads



