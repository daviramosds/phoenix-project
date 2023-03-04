import os, glob

def remove_tmp_files():
    for filename in glob.glob("audio/tmp/test*"):
        os.remove(filename) 