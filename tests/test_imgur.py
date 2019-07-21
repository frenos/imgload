from unittest import TestCase

from requests_html import HTMLSession

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

    def test_get_link(self):
        req_session = HTMLSession()

        result = host_instance.get_link(testing_url, req_session)
        self.assertIsNotNone(result)
        self.assertEqual('https://i.imgur.com/W0Cu3zE.png', result)

    def test_get_bad_link(self):
        req_session = HTMLSession()

        this_testing_url = testing_url + 'A' * 20

        result = host_instance.get_link(this_testing_url, req_session)
        self.assertIsNone(result)
