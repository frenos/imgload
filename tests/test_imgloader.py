from unittest import TestCase

from imgload.Imgloader import ImgLoader


class TestImgLoader(TestCase):

    def setUp(self) -> None:
        self.imgloader = ImgLoader()

    def testdl(self):
        result = self.imgloader.__download_link_as_bytes__('https://i.imgur.com/W0Cu3zE.png')

        self.assertIsNotNone(result)

    def testdl_fail(self):
        result = self.imgloader.__download_link_as_bytes__('https://i.imgur.com/' + ('A' * 20) + 'W0Cu3zE.png')

        self.assertIsNone(result)

    def testdl_no_image(self):
        result = self.imgloader.__download_link_as_bytes__('https://imgur.com/a/jpwwwq6')

        self.assertIsNone(result)
