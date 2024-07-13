import logging
import os 
import sys


format="[[%(asctime)s:] *** %(message)s:***%(levelname)s:%(module)s]"


log_dir='logs'
log_filepath=os.path.join(log_dir,'running_log.logs')

os .makedirs(log_dir,exist_ok=True)

logging.basicConfig(format=format,
                    level=logging.INFO,
                    
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)]
                    
                    )

