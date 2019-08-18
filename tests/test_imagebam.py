from unittest import TestCase

from requests_html import HTMLSession

from imgload.img_hosts.Imagebam import ImagebamCom

testing_url = 'http://www.imagebam.com/image/294d3c1284036864'

host_instance = ImagebamCom()


class TestImagebam(TestCase):

    def test_can_handle(self):
        result = host_instance.can_handle(testing_url)

        self.assertTrue(result)

    def test_cant_handle(self):
        result = host_instance.can_handle('http://www.google.de/')
        self.assertFalse(result)

    def test_cant_handle_base(self):
        result = host_instance.can_handle('https://www.imagebam.com/')
        self.assertFalse(result)

    def test_get_link(self):
        req_session = HTMLSession()

        result = host_instance.get_link(testing_url, req_session)
        self.assertIsNotNone(result)
        self.assertEqual('https://images2.imagebam.com/a1/6e/55/294d3c1284036864.png',
                         result)
