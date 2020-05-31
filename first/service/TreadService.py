from first.repository.TreadRepository import TreadRepository


class TreadService:
    @staticmethod
    def create_tread(name, board_id):
        TreadRepository.create_tread(name, board_id)

