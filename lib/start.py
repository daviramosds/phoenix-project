from dotenv import load_dotenv
from glob import glob
from os import remove, path, getenv, mkdir

def load_env():
    env_file_path = '.env.local'
    load_dotenv(dotenv_path=env_file_path)

def handle_tmp_files():
    TMP_FILE_PATH = getenv('TMP_FILE_PATH')
    if path.exists(TMP_FILE_PATH) == False:
        mkdir(TMP_FILE_PATH)
    else:
        for filename in glob(f'{TMP_FILE_PATH}*'):
            remove(filename)