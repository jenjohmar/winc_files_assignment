__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os, shutil
from zipfile import ZipFile

#1: function checks parent folder for a child folder named 'cache' if it doesn't exist it creates it, if it does exist it deletes it

def clean_cache():
    
    directory = "cache"
    if not os.path.exists(directory):
        os.mkdir(directory)
    if os.path.exists(directory):
        shutil.rmtree(directory)
    
#2: function extracts the contents of a zipfile to cache folder

def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as zipObj:
        zipObj.extractall(cache_path)
    
#3: function return the absolute file paths of each item in the folder 'cache'

def cached_files():
    ziplist = os.listdir('cache')
    pathlist = []
    paadje = os.getcwd()+'\\cache'
    for file in ziplist:
        pathlist.append(os.path.join(paadje, file))
       
    return pathlist  

def find_password(lijst):
    for i in lijst:
        file = open(i, "r")
        for line in file:
            if "password" in line:
                password = line.split(sep=" ")[-1]
                return password
    
clean_cache()
cache_zip("data.zip", "cache")
cached_files()
print(find_password(cached_files()))    
