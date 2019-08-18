import io

from PIL import Image
from requests_html import HTMLSession

from imgload.img_hosts.Fastpic import FastpicRu
from imgload.img_hosts.Imagebam import ImagebamCom
from imgload.img_hosts.Imagevenue import ImagevenueCom
from imgload.img_hosts.Imgur import ImgurCom
from imgload.img_hosts.Postimg import PostimgCC


class ImgLoader():

    def __init__(self):
        self.session = None
        self.available_hosts = list()
        self.__init_available_hosts__()

    def __init_available_hosts__(self):
        self.available_hosts.append(FastpicRu())
        self.available_hosts.append(ImagebamCom())
        self.available_hosts.append(ImagevenueCom())
        self.available_hosts.append(ImgurCom())
        self.available_hosts.append(PostimgCC())


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

    def get_image_direct_link(self, url):
        correct_host_module = self.__get_correct_host__(url)

        if correct_host_module is None:
            return None
        self.__check_session__()
        direct_download_link = correct_host_module.get_link(link=url, session=self.session)
        return direct_download_link

    def get_image_as_bytes(self, url):
        direct_download_link = self.get_image_direct_link(url)
        if direct_download_link is None:
            return None
        img_bytes = self.__download_link_as_bytes__(direct_download_link)
        return img_bytes

    def get_image_as_pil(self, url):
        image_bytes = self.get_image_as_bytes(url)
        if image_bytes is None:
            return None
        img_bytes_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(img_bytes_stream)
        return pil_image
