import socket
import sys

# Create socket

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999