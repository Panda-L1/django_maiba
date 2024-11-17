class Result:
    def __init__(self, code=200, message="Success", data=None):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data,
        }
