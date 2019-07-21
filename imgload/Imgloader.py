import requests

from imgload.img_hosts import available_hosts


class ImgLoader():

    def __init__(self):
        self.session = None
        self.hosters = available_hosts

    def check_session(self):
        if self.session is None:
            self.session = requests.sesssion()

    def get_image_as_bytes(self, url):
        pass

    def get_image_as_pil(self, url):
        pass
