import sys
import os


def create_folder_files_map(path_to_folder):
    files_list = {}
    for dir_path, dirs, dir_files in os.walk(path_to_folder):
        for filename in dir_files:
            path_to_file = os.path.join(dir_path, filename)
            file_size = os.path.getsize(path_to_file)
            try:
                files_list[(filename, file_size)] += [path_to_file]
            except KeyError:
                files_list[(filename, file_size)] = [path_to_file]
    return files_list


def get_list_of_duplicates(folder_files_map):
    return [files for files in folder_files_map.values() if len(files) > 1]


def print_duplicates(duplicate_lists):
    if duplicate_lists:
        print('Found following duplicates in {}'.format(path_to_folder))
        for duplicate_list in duplicate_lists:
            for duplicate in duplicate_list:
                print(duplicate)
    else:
        print('There is no duplicates in {}'.format(path_to_folder))


if __name__ == '__main__':
    try:
        path_to_folder = sys.argv[1]
    except IndexError:
        sys.exit('You should pass folder')

    if not os.path.isdir(path_to_folder):
        sys.exit('Please, pass folder not file')

folder_files_map = create_folder_files_map(path_to_folder)
duplicates = get_list_of_duplicates(folder_files_map)
print(duplicates)
