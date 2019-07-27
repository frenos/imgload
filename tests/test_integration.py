from unittest import TestCase

from imgload.Imgloader import ImgLoader


class TestIntegration(TestCase):

    def test_downloading_image(self):
        with open('tests/testdata/imgload.png', 'rb') as img_file:
            sample_img_bytes = img_file.read()
        my_image_loader = ImgLoader()

        dl_img_bytes = my_image_loader.get_image_as_bytes('https://imgur.com/a/jpwwwq6')
        self.assertEqual(sample_img_bytes, dl_img_bytes)

    def test_downloading_non_exist(self):
        my_image_loader = ImgLoader()

        result = my_image_loader.get_image_as_bytes('https://im_not_an_image_hoster.com/i_dont_exist.jpeg')
        self.assertIsNone(result)

    def test_postimg_cc_download(self):
        with open('tests/testdata/imgload_postimg.png', 'rb') as img_file:
            sample_img_bytes = img_file.read()
        my_image_loader = ImgLoader()

        dl_img_bytes = my_image_loader.get_image_as_bytes('https://postimg.cc/NyHVjkSZ')
        self.assertEqual(sample_img_bytes, dl_img_bytes)

    def test_get_link(self):
        my_image_loader = ImgLoader()

        dl_link = my_image_loader.get_image_direct_link('https://imgur.com/a/jpwwwq6')
        self.assertEqual('https://i.imgur.com/W0Cu3zE.png', dl_link)

    def test_pil_image(self):
        my_image_loader = ImgLoader()

        downloaded_pil = my_image_loader.get_image_as_pil('https://imgur.com/a/jpwwwq6')

        self.assertIsNotNone(downloaded_pil)
        self.assertEqual(800, downloaded_pil.width)
        self.assertEqual(600, downloaded_pil.height)
