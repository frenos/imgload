import inspect

from .ImageHost import ImageHost

available_hosts = []
host_modules = [obj() for obj in ImageHost.__subclasses__()]
for hoster in host_modules:
    for clazz in inspect.getmembers(hoster, inspect.isclass):
        available_hosts.append(clazz[1]())
