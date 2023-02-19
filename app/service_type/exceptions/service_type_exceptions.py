class ServiceTypeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class ServiceTypeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code