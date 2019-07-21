from unittest import TestCase

from imgload.Imgloader import ImgLoader


def load_sample_image():
    with open('tests/testdata/imgload.png', 'rb') as img_file:
        return img_file.read()


sample_img_bytes = load_sample_image()


class TestIntegration(TestCase):

    def test_downloading_image(self):
        my_image_loader = ImgLoader()

        dl_img_bytes = my_image_loader.get_image_as_bytes('https://imgur.com/a/jpwwwq6')
        self.assertEqual(sample_img_bytes, dl_img_bytes)

    def test_downloading_non_exist(self):
        my_image_loader = ImgLoader()

        result = my_image_loader.get_image_as_bytes('https://im_not_an_image_hoster.com/i_dont_exist.jpeg')
        self.assertIsNone(result)
