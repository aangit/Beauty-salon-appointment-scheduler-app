

class UserInvalidPassword(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserInvalidEmail(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserInvalidPassword(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserNotEmployee(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class UserNotClient(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class ClientNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class EmployeeNotFound(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code