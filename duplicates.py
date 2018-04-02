import sys
import os
import glob


def create_folder_files_map(path_to_folder):
    files_list = {}
    for dir_path, dirs, dir_files in os.walk(path_to_folder):
        for filename in dir_files:
            path_to_file = os.path.join(dir_path, filename)
            file_size = os.path.getsize(path_to_file)
            files_list[path_to_file] = [filename, file_size] 
    return files_list


def get_list_of_duplicates(folder_map):
    dublicates = []
    pass


if __name__ == '__main__':
    try:
        path_to_folder = sys.argv[1]
    except IndexError:
        sys.exit('You should pass folder to file')
    except FileNotFoundError:
        sys.exit('There is no such folder')

map = create_folder_files_map(path_to_folder)
print(map)
get_list_of_duplicates(map)