# my_exception.py
import traceback

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: Exception):
        super().__init__(error_message)
        self.error_message = self.error_message_details(error_message, error_details)

    def error_message_details(self, error_message: str, error_details: Exception) -> str:
        _, _, ex_tb = traceback.exc_info()
        error_message += f" | Traceback: {''.join(traceback.format_exception(etype=type(error_details), value=error_details, tb=ex_tb))}"
        return error_message
