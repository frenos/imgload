import inspect

from requests_html import HTMLSession


class ImgLoader():

    def __init__(self):
        self.session = None
        self.available_hosts = list()
        hoster_modules = [obj() for obj in ImageHost.ImageHost.__subclasses__()]
        for hoster in hoster_modules:
            for clazz in inspect.getmembers(hoster, inspect.isclass):
                self.available_hosts.append(clazz[1]())

    def __check_session__(self):
        if self.session is None:
            self.session = HTMLSession()

    def __get_correct_host__(self, url):
        for host in self.available_hosts:
            if host.can_handle(url):
                return host
        return None

    def __download_link_as_bytes__(self, url):
        self.__check_session__()
        response = self.session.get(url)
        if response.status_code is not 200:
            return None

        if 'image' in response.headers['Content-Type']:
            img_bytes = response.content
            return img_bytes

        return None

    def get_image_as_bytes(self, url):

        correct_host_module = self.__get_correct_host__(url)

        if correct_host_module is None:
            return None
        self.__check_session__()
        direct_download_link = correct_host_module.get_link(link=url, session=self.session)
        img_bytes = self.__download_link_as_bytes__(direct_download_link)
        return img_bytes

    def get_image_as_pil(self, url):
        pass
