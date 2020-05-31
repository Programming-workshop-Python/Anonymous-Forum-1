from first.repository.MessageRepository import MessageRepository


class MessageService:
    @staticmethod
    def create_message(author, text, tread_id):
        MessageRepository.create_message(author, text, tread_id)
