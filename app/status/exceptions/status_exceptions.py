class StatusNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class StatusExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code