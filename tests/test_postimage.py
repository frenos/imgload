from unittest import TestCase

from requests_html import HTMLSession

from imgload.img_hosts.Postimg import PostimgCC

testing_url = 'https://postimg.cc/NyHVjkSZ'

host_instance = PostimgCC()


class TestPostimg(TestCase):

    def test_can_handle(self):
        result = host_instance.can_handle(testing_url)

        self.assertTrue(result)

    def test_cant_handle(self):
        result = host_instance.can_handle('http://www.google.de/')
        self.assertFalse(result)

    def test_cant_handle_base(self):
        result = host_instance.can_handle('https://postimg.cc/')
        self.assertFalse(result)

    def test_get_link(self):
        req_session = HTMLSession()

        result = host_instance.get_link(testing_url, req_session)
        self.assertIsNotNone(result)
        self.assertEqual('https://i.postimg.cc/FKWQGPZF/imgload.png', result)

    def test_get_bad_link(self):
        req_session = HTMLSession()

        this_testing_url = testing_url + 'A' * 20

        result = host_instance.get_link(this_testing_url, req_session)
        self.assertIsNone(result)
