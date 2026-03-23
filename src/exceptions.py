import sys 
import logging 

def error_message_detail(error, error_detail:sys):
    
    exc_type, exc_value, exc_traceback = error_detail.exc_info() # exc_info is used to retrieve details about the error currently being handled
    
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_traceback.tb_lineno, str(error)
    )
    
    
    return error_message
    
class CustomError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, error_message, error_detail:sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)
        
    def __str__(self):
        return self.error_message
    
               