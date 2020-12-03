import os;
import shutil;
from os import path;

cache_paths =[path.expandvars(r'%LOCALAPPDATA%\NVIDIA Corporation\NV_Cache'), 
              path.expandvars(r'%LOCALAPPDATA%\D3DSCache')];

def clear_path(dir):
    for root, dirs, files in os.walk(dir):
        try:
            for file in files:
                os.unlink(path.join(root, file));
            for folder in dirs:
                shutil.rmtree(path.join(root, folder));
        except Exception as ex:
            print('{0}\n'.format(ex.args));

for cache_path in cache_paths:
    if (path.exists(cache_path)):
        print('Clearing: {0}\n'.format(cache_path));
        clear_path(cache_path);    
        
print('Done Clearing, You Can Close The Program Now.\n');

while True:
    pass;