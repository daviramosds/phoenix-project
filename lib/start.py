from dotenv import load_dotenv
import os, glob

def remove_tmp_files():
    for filename in glob.glob("audio/tmp/test*"):
        os.remove(filename)

def load_env():
    env_file_path = '.env.local'
    load_dotenv(dotenv_path=env_file_path)