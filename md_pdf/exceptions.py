class BaseException(Exception):
    pass


class PrematureExit(BaseException):
    pass


class ConfigValidationException(BaseException):
    pass


class PDFRenderException(BaseException):
    pass
