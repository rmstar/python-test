from enum import Enum, unique

class Host(Enum):
    HOST1 = {'ip': '10.0.0.1', 'port': 80}
    HOST2 = {'ip': '10.0.0.2', 'port': 443}
    HOST3 = {'ip': '10.0.0.3', 'port': 80}

    def __init__(self, kwargs):
        self.ip = kwargs['ip']
        self.port = kwargs['port']

    def __str__(self):
        return 'IP: %s port: %d' % (self.ip, self.port)

    @property
    def url(self):
        return 'http://{}:{}'.format(self.ip, self.port)

first_host = None
for host in Host:
    if first_host is None:
        first_host = host.value
    print(host.name, host.value, host.url)

print(Host['HOST3'])
print(Host(first_host))
