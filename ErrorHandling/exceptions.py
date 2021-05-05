class Error(Exception):
    pass


class BadRequestError(Error):
    pass

class InvalidInput(Error):
    pass