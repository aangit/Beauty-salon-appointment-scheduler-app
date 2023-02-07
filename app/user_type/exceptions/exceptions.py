class UserTypeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserTypeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code