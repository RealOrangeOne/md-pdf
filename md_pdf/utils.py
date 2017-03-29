import shutil
import os


def remove_dir(dir):
    try:
        shutil.rmtree(dir)
        os.rmdir(dir)
    except FileNotFoundError:
        pass
