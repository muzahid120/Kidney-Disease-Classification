import os
import json
from pathlib import Path
from box import ConfigBox
import yaml
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any
import joblib
import base64


from src.cnnClassifier._m_logging import logging
from src.cnnClassifier.my_exception import CustomException


@ ensure_annotations

def read_yaml (yaml_file_path:Path) -> ConfigBox:
    try:
       with open (yaml_file_path) as file :
          content=yaml.safe_load(file)
          logging.info(f" your yaml file successfully loeaded :{yaml_file_path}")

          return ConfigBox(content)
       
    except BoxValueError as e :
       raise ValueError (f" your yaml file is empty:{e}")
    
    except Exception as e:
       raise e
    

@ ensure_annotations
def create_directories(path_to_directories:list,verbose=True ):
   
   for path in path_to_directories:
      os.makedirs(path)
      if verbose:
         logging.info(f"create directory at :{path}")

@ensure_annotations
def save_json(path:Path,data:dict):
   
   
   with open(path,'w') as file :
      
      json.dump(data,file,indent=4)

   logging.info(f" your file saved at:{path} ")   



@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open (path) as f:
        content=json.load(f)
    logging.info(f'your file successfully load :{path}')
    return ConfigBox(content)    

@ensure_annotations
def save_bin(data:any,path:Path):
   
   joblib.dump(value=data,filename=path)

   logging.info(f"Binary file save at ;{path}")


@ensure_annotations
def load_bin(path:Path)->any:
   
   data=joblib.load(path)
   logging.info('your binary file load at :{path}')
   return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
   
   

   