class ContactTypeNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class ContactTypeExists(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code