from zipfile import ZipFile
import os


def zip_insert(name, extension):
    if len(os.listdir(os.getcwd())) == 0: #check whether the directory is empty
        return None
    with ZipFile(name, 'w') as testzip: # creating zip file
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(extension): #importing file into zip file according to extension
                    testzip.write(os.path.join(root, file))
    return testzip.filename


name = 'test.zip'
extension = '.odg'
print(zip_insert(name, extension))

