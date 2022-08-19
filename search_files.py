# Author: Guilherme Mendes
# Search for all .extension files in directory and subdirectories

import os
import json
import os.path

def search_files(extension, directory):
    data = []
    try:
        for path, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    fullpath = os.path.join(path, file)
                    size = os.path.getsize(fullpath)
                    info = {
                        "path": fullpath,
                        "filename": file,
                        "extension": extension,
                        "size": size
                    }
                    data.append(info)
        size = len(data)
        return (json.dumps(data, indent = 4, sort_keys = True), size)
    except:
        raise Exception("> Error: Cannot search for files")
