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
