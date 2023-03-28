import time,os,shutil

path = "path_of_directory" 
days = 30 

seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            ctime = os.stat(full_path).st_ctime
            if ctime < seconds:
                if os.path.isfile(full_path):
                    os.remove(full_path)
                else:
                    shutil.rmtree(full_path)
else:
    print("Path not found")
