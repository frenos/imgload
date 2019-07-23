from unittest import TestCase

from requests_html import HTMLSession

from imgload.img_hosts.Imagevenue import ImagevenueCom

testing_url = 'http://img28105.imagevenue.com/img.php?image=900245278_imgload_122_965lo.jpg'

host_instance = ImagevenueCom()


class TestImagevenue(TestCase):

    def test_can_handle(self):
        result = host_instance.can_handle(testing_url)

        self.assertTrue(result)

    def test_cant_handle(self):
        result = host_instance.can_handle('http://www.google.de/')
        self.assertFalse(result)

    def test_cant_handle_base(self):
        result = host_instance.can_handle('https://www.imagevenue.com/')
        self.assertFalse(result)

    def test_get_link(self):
        req_session = HTMLSession()

        result = host_instance.get_link(testing_url, req_session)
        self.assertIsNotNone(result)
        self.assertEqual('http://img28105.imagevenue.com/aAfkjfp01fo1i-3407/loc965/900245278_imgload_122_965lo.jpg',
                         result)

    def test_get_bad_link(self):
        req_session = HTMLSession()

        this_testing_url = testing_url + 'A' * 20

        result = host_instance.get_link(this_testing_url, req_session)
        self.assertIsNone(result)
