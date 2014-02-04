'''Stubs for urllib3'''

from httplib2 import HTTPConnectionWithTimeout, HTTPSConnectionWithTimeout
from ..stubs import VCRHTTPConnection, VCRHTTPSConnection


class VCRHTTPConnectionWithTimeout(VCRHTTPConnection,
                                   HTTPConnectionWithTimeout):
    _baseclass = HTTPConnectionWithTimeout

    def __init__(self, *args, **kwargs):
        if 'proxy_info' in kwargs:
            del kwargs['proxy_info']
        VCRHTTPConnection.__init__(self, *args, **kwargs)


class VCRHTTPSConnectionWithTimeout(VCRHTTPSConnection,
                                    HTTPSConnectionWithTimeout):
    _baseclass = HTTPSConnectionWithTimeout

    def __init__(self, *args, **kwargs):
        if 'proxy_info' in kwargs:
            del kwargs['proxy_info']
        VCRHTTPSConnection.__init__(self, *args, **kwargs)
