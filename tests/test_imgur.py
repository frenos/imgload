from unittest import TestCase

from imgload.img_hosts.Imgur import ImgurCom

testing_url = 'https://imgur.com/a/jpwwwq6'

host_instance = ImgurCom()


class TestImgur(TestCase):

    def test_can_handle(self):
        result = host_instance.can_handle(testing_url)

        self.assertTrue(result)

    def test_cant_handle(self):
        result = host_instance.can_handle('http://www.google.de/')
        self.assertFalse(result)

    def test_cant_handle_base(self):
        result = host_instance.can_handle('https://www.imgur.com/')
        self.assertFalse(result)
