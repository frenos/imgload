import re

from imgload.img_hosts import ImageHost


class ImgurCom(ImageHost):

    def __init__(self):
        super(ImageHost, self).__init__()
        self.base_url = "imgur.com"
        self.regex = r'\A(http*(s)://imgur.com/)+'

    def can_handle(self, link):
        result = re.search(self.regex, link)
        if result is None:
            return False
        return True
