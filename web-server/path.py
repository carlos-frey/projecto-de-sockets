import os
from jinja2 import FileSystemLoader, Environment


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
    try:
        with open(filepath, 'tr') as f:
            content = f.read()  
            f.close()  
            return content
    except:
        with open(filepath, 'rb') as f:
            content = f.read()
            f.close()
            return content
                  

def is_index_html_inside_folder(path):
    filepath = convert_to_os_path(path)
    files_and_folders = os.listdir(filepath)
    for item in files_and_folders:
        if item == 'index.html':
            return True 

def get_items_inside_folder(path):
    folderpath = convert_to_os_path(path)
    files_and_folders = os.listdir(folderpath)
    files_and_folders_with_label = []

    for item in files_and_folders:
        if os.path.isfile(f'{folderpath}/{item}'):
            files_and_folders_with_label.append({"name": item, "type": "file"})
        else:
            files_and_folders_with_label.append({"name": item, "type": "folder"})
    return files_and_folders_with_label


def is_folder_empty(path):
    filepath = convert_to_os_path(path)
    files_and_folders = os.listdir(filepath)
    return len(files_and_folders) == 0

def test_jinja():
    loader = FileSystemLoader('templates')        
    env = Environment(loader=loader)
    template = env.get_template('folder.html')
    file = open('pages/folder.html', 'w')
    render = template.render(name='Henrique is my name')
    file.write(render)
    file.close()    

if __name__ == '__main__':
    print(get_items_inside_folder('/'))