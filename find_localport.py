#!/usr/bin/env python
"""Find a random available local port"""
import socket


def get_random_lport():
    """Find a random local port on our workstation that is not in use,
    so we can use it as the listening port# for a local SSH proxy."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    addr, localport = sock.getsockname()
    sock.close()
    return localport

print(get_random_lport())
