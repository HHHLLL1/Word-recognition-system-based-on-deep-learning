from django.test import TestCase

from .models import Post


class OcrModelTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     Post.objects.create(username='first file')
    #     Post.objects.create(file='test content')

    # def test_title_content(self):
    #     ocr = Post.objects.get(id=1)
    #     expected_object_name = f'{ocr.title}'
    #     self.assertEquals(expected_object_name, 'first file')
    #
    # def test_desription_content(self):
    #     ocr = Post.objects.get(id=2)
    #     expected_object_name = f'{ocr.content}'
    #     self.assertEquals(expected_object_name, 'test content')

    def test_get_history_data(self):
        hisdata = Post.objects.filter()
        print(hisdata)

