import unittest
from unittest import mock, TestCase

from patch import facebook, google

class TestApi(TestCase):

    def setUp(self) -> None:
        self.patcher = mock.patch("patch.google.get_data", return_value='data2')
        self.fb_patcher = mock.patch("patch.facebook.get_data", return_value='datafb')
        self.patcher.start()
        self.fb_patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()
        self.fb_patcher.stop()

    @mock.patch("patch.facebook.get_data")
    @mock.patch("patch.google.get_data", return_value='data2')
    def test_mock_external_api(self, googl, fb):
        fb.return_value = 'datafb'
        self.assertEqual(google.call_googl_api(), 'data2')
        self.assertEqual(facebook.call_fb_api(), 'datafb')

    @unittest.skip
    def test_mock_external_api_pt1(self):
        with mock.patch("patch.google.get_data", return_value='data2'):
            self.assertEqual(google.call_googl_api(), 'data2')

    def test_mock_external_api_pt2(self):
       self.assertEqual(google.call_googl_api(), 'data2')
       self.fb_patcher.return_value = 'datafb'
       self.assertEqual(facebook.call_fb_api(), 'datafb')

    @mock.patch("patch.google.get_data", side_effect = [
        'data_1',
        'data_2',
        'data_3'
    ])
    def test_mock_side_effect(self, googl):
        self.assertEqual(google.call_googl_api(), 'data_1')
        self.assertEqual(google.call_googl_api(), 'data_2')
        self.assertEqual(google.call_googl_api(), 'data_3')



    @mock.patch("patch.google.get_data1")
    @mock.patch("patch.google.get_data", return_value='data2')
    def test_mock_external_api(self, googl, googl1):
        googl1.return_value = 'datafb'
        self.assertEqual(google.call_googl_api2(), 'data2datafb')
