import sys

class CustomException(Exception):
    """Custom exception for handling specific errors in the application."""
    def __init__(self, message: str, error_dtail: Exception = None):
        self.message = self.get_error_details(message, error_dtail) if error_dtail else message
        super().__init__(message)
        

    @staticmethod
    def get_error_details(message, error) -> str:
        _, _, exec_tb = sys.exc_info()
        file_name = exec_tb.tb_frame.f_code.co_filename if exec_tb else "Unknown"   
        line_number = exec_tb.tb_lineno if exec_tb else "Unknown"
        return f"Error: {message}, File: {file_name}, Line: {line_number}, Original Error: {error}"
    def __str__(self):
        return f"CustomException: {self.message}"