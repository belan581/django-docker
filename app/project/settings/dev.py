from ._base import *

DEBUG = True

INSTALLED_APPS += [
    "debug_toolbar",
]

if DEBUG:
    # import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]