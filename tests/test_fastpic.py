from unittest import TestCase

from requests_html import HTMLSession

from imgload.img_hosts.Fastpic import FastpicRu

testing_url = 'https://fastpic.ru/view/90/2019/0722/ded5ab5242cd6fcac507cfec2090699c.png.html'

host_instance = FastpicRu()


class TestFastpic(TestCase):

    def test_can_handle(self):
        result = host_instance.can_handle(testing_url)

        self.assertTrue(result)

    def test_cant_handle(self):
        result = host_instance.can_handle('http://www.google.de/')
        self.assertFalse(result)

    def test_cant_handle_base(self):
        result = host_instance.can_handle('https://fastpic.ru/')
        self.assertFalse(result)

    def test_get_link(self):
        req_session = HTMLSession()

        result = host_instance.get_link(testing_url, req_session)
        self.assertIsNotNone(result)
        self.assertEqual('https://i90.fastpic.ru/big/2019/0722/9c/ded5ab5242cd6fcac507cfec2090699c.png', result)

    def test_get_bad_link(self):
        req_session = HTMLSession()

        this_testing_url = testing_url + 'A' * 20

        result = host_instance.get_link(this_testing_url, req_session)
        self.assertIsNone(result)
