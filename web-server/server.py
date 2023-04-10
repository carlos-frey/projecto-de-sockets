from socket import socket, AF_INET, SOCK_STREAM
import datetime
import platform
import path
import mimetypes
from jinja2 import FileSystemLoader, Environment


server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 9696))
server.listen()


HTTP_SUPPORTED_VERSION = 'HTTP/1.1'
SERVER_NAME = 'Awesome Webserver'
SERVER_VERSION = '1.0'

def provide_current_datetime():
    current_date_time = datetime.datetime.utcnow()
    return current_date_time.strftime('%a, %d %b %Y %H:%M:%S GMT')

def provide_server_informations(): 
    operating_system = platform.system()
    return f'{SERVER_NAME}/{SERVER_VERSION} ({operating_system})'

def build_headers(content_type, status):
    current_date_time = provide_current_datetime()
    server = provide_server_informations()
    http_version_and_status = f'{HTTP_SUPPORTED_VERSION} {status}'
    
    header= f'{http_version_and_status} \r\n' \
    f'Date: {current_date_time}\r\n' \
    f'Server: {server}\r\n' \
    f'Content-Type: {content_type}\r\n' \
    '\r\n'
    return header

print('Your web server have started!')


def handle_request(client_requisition_socket):
    request = client_requisition_socket.recv(2048).decode('utf-8')
    url_path = request.split()[1]

    handle_path_and_return_binary_html(url_path, client_requisition_socket)
    

    # text_file = path.open_pathfile_and_convert_to_binary()
    # content_type='text/plain'
    # status='200 OK'
    
    # raw_response = build_headers(content_type=content_type, status=status) + text_file
    # response = raw_response.encode()
    # client_requisition_socket.send(response)
    # client_requisition_socket.close()

def handle_path_and_return_binary_html(url_path, client_requisition_socket):
    if path.path_exists(url_path) and path.is_file(url_path):
        mime_type, encoding = mimetypes.guess_type(url_path)
        file_body = path.open_pathfile_and_parse_data(url_path)
        content_type = mime_type     
        status='200 OK'
        raw_response = build_headers(content_type=content_type, status=status) 
        if type(file_body) == str:
            file_body = file_body.encode()
        
        response_bytes = raw_response.encode() 
        response = response_bytes + file_body
        client_requisition_socket.send(response)
        client_requisition_socket.close()
    elif path.path_exists(url_path) and path.is_folder(url_path) and path.is_index_html_inside_folder(url_path):
        mime_type, encoding = mimetypes.guess_type(url_path)
        file_body = path.open_pathfile_and_parse_data(f"{url_path}/index.html")
        content_type = mime_type     
        status='200 OK'
        raw_response = build_headers(content_type=content_type, status=status) 
        if type(file_body) == str:
            file_body = file_body.encode()
        response_bytes = raw_response.encode() 
        response = response_bytes + file_body
        client_requisition_socket.send(response)
        client_requisition_socket.close()
    elif path.path_exists(url_path):
        os_path = path.convert_to_os_path(url_path)
        items = path.get_items_inside_folder(os_path)
        # loader = FileSystemLoader('templates')        
        # env = Environment(loader=loader)
        # template = env.get_template('folder.html')
        # file = open('pages/folder.html', 'w')
        # render = template.render(name='Carlos is my name')
        # file.write(render)
        # file.close()     
        
    # if path.is_folder(url_path) and path.is_index_html_inside_folder(url_path):
    #     mime_type, encoding = mimetypes.guess_type(url_path)
    #     file_body = path.open_pathfile_and_parse_data(url_path)
    #     content_type = mime_type     
    #     status='200 OK'
    #     raw_response = build_headers(content_type=content_type, status=status) 
    #     if type(file_body) == str:
    #         file_body.encode()
        
    #     response = raw_response.encode() + file_body
    #     client_requisition_socket.send(response)
    #     client_requisition_socket.close() 
    # else:
    #     content_type = 'text/plain'     
    #     status='200 OK'
    #     raw_response = build_headers(content_type=content_type, status=status) + "didn't work, sorry"
    #     response = raw_response.encode()
    #     client_requisition_socket.send(response)
    #     client_requisition_socket.close()








while True:
    client_requisition_socket, client_address = server.accept()    
    handle_request(client_requisition_socket)

    
