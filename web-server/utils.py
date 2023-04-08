

def convert_request_to_dict(request):
    lines = request.split('\r\n')
    headers = {}
    for line in lines[1:]:
        if line:
            header, value = line.split(': ')
            headers[header] = value
    
    return headers

    