from socket import socket, AF_INET, SOCK_STREAM
from utils import convert_request_to_dict
import datetime
import platform


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

def build_body(content_type):
    body = '<html lang="en">'\
            '<head>'\
            '<meta charset="UTF-8">'\
            '<meta http-equiv="X-UA-Compatible" content="IE=edge">' \
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">' \
            '<title>Document</title>' \
            '</head>' \
            '<body>' \
            '<h1>Welcome to my web server :D </h1>' \
            '</body>' \
           '</html>' \
            
    return body            

print('Your web server have started!')


def handle_request(client_requisition_socket):
    raw_data = client_requisition_socket.recv(2048).decode('utf-8')
    content_type='text/html'
    status='200 OK'
    
    raw_response = build_headers(content_type=content_type, status=status) + build_body(content_type=content_type)
    response = raw_response.encode()
    client_requisition_socket.send(response)
    client_requisition_socket.close()

while True:
    client_requisition_socket, client_address = server.accept()    
    handle_request(client_requisition_socket)

    
