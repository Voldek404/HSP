import os


def get_list(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(os.path.join(path, f)):
            if flag:
                results = get_list(os.path.join(path, f))
                for item in results:
                    os.remove(file_path)
    os.rmdir(path)

    return True


print(get_list('test_dir'))
