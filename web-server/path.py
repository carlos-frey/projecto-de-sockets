import os
import mimetypes

def convert_to_os_path(path):
    current_directory = os.getcwd() 
    complete_path = f"{current_directory}/root{path}"        
    return complete_path

def path_exists(path):
    path = convert_to_os_path(path)
    return os.path.exists(path)

def is_file(path):
    path = convert_to_os_path(path)
    return os.path.isfile(path)

def is_folder(path):
    path = convert_to_os_path(path)
    return os.path.isdir(path)

def open_pathfile_and_parse_data(path):
    filepath = convert_to_os_path(path)
    with open(filepath, 'r') as f:
        content = f.read()  
        f.close()          
    return content


def is_index_html_inside_folder(path):
   pass
     

def get_binary_index_html_in_current_folder(path):
    pass

if __name__ == '__main__':
    pass