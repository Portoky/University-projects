class RepositoryExceptions(Exception):
    def __init__(self, exception_message):
        self._exception_message = exception_message

    @property
    def exception_message(self):
        return self._exception_message

    def __str__(self):
        return self._exception_message
