from functools import partial
from lazy_connection import LazyConnection

conn = LazyConnection(('www.python.org', 80))

with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET / HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
