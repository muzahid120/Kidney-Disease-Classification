import sys

from src.cnnClassifier._m_logging import logging


def error_message_details(error,err_details:sys):

    _,_,ex_tb=err_details.exc_info()

    file_name=ex_tb.tb_frame.f_code.co_filename
    file_no=ex_tb.tb_lineno
    error_messgae=f"Error Occured in python Sript File name:[{0}] number:[{1}] error message:[{2}]".format(file_name,file_no,str(error))

    return error_messgae

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)

        self.erro_messgae=error_message_details(error_message,error_details)

    def __str__(self):
        return self.erro_messgae