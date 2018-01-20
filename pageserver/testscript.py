
STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"

import os


def url_check(file_url):

    illegal = ["~", "//", ".."]

    if not file_url[0] in illegal:
        if not file_url[0:1] in illegal:
            return True

    print(STATUS_FORBIDDEN)
    return False

for filename in os.listdir('.././pages'):
    print()