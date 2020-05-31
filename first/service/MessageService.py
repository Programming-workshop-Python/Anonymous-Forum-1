from first.repository.MessageRepository import MessageRepository


class MessageService:
    @staticmethod
    def create_message(author, text, tread_id):
        MessageRepository.create_message(author, text, tread_id)


    @staticmethod
    def get_messages_by_tread(tread_id):
        messages = MessageRepository.get_messages_by_tread(tread_id)
        return messages


    @staticmethod
    def get_message(id):
        message = MessageRepository.get_message(id)
        return message


    @staticmethod
    def delete_message(id):
        MessageRepository.delete_message(id)


