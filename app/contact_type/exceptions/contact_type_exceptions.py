class ContactTypeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class ContactTypeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code