class CustomException(Exception):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(message)
        self.error = error
