import os


def get_list(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
    os.rmdir(path)
    return True


flag = True

print(get_list('test_dir'))
