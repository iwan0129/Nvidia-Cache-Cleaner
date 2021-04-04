import os
import shutil
from os import path

cache_paths = [path.expandvars(r'%LOCALAPPDATA%\NVIDIA Corporation\NV_Cache'), 
              path.expandvars(r'%LOCALAPPDATA%\D3DSCache'),
              path.expandvars(r'%PROGRAMDATA%\NVIDIA Corporation\NV_Cache')]

def clear_path(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            try:
                os.unlink(path.join(root, file));
            except Exception as ex:
                print('{0}\n'.format(ex.args))
                continue;
            pass;
        for folder in dirs:
            try:
                shutil.rmtree(path.join(root, folder))
            except Exception as ex:
                print('{0}\n'.format(ex.args))
                continue;
            pass;
pass;
                
for cache_path in cache_paths:
    if (path.exists(cache_path)):
        print('Clearing: {0}\n'.format(cache_path));
        clear_path(cache_path);
pass;
        
print('Done Clearing, You Can Close The Program Now.\n');

while True:
   pass;