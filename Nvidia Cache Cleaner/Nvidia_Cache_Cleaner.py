import os
import shutil
from os import path

nvcache_path = path.expandvars(r"%LOCALAPPDATA%\NVIDIA Corporation\NV_Cache")

def clear_cache(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            os.unlink(path.join(root, file))
        for folder in dirs:
            shutil.rmtree(path.join(root, folder))

if (path.exists(nvcache_path)):
    clear_cache(nvcache_path)