# TODO: function explainers

import os

def files2list(path, file_extension):
    """
    Return a list of found files with that extension from the given path

    :param path: The folder to read from
    :param file_extension: The type of file to read
    """
    files=[]
    for file in os.listdir(path):
        if file.endswith(file_extension):
            files.append(file)
    return files

def list2file(file, arr, path):
    with open(file, 'w') as oFile:
        for item in arr:
            oFile.write(path)
            oFile.write(f"/{item}\n")
