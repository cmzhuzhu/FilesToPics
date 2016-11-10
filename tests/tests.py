#!/usr/bin/env python3

# author : caomingzhu
# github : https://github.com/cmzhuzhu
# description : FileToPics test


import unittest
from FileToPics import FileToPics

class TestSimple(unittest.TestCase):
    def test_nonFilePathParameter(self):
        file2pics     = FileToPics(picpath = '/home/test/', filetype = 'pdf')
        resData       = file2pics.file_to_pics()
        self.assertEqual(resData, {'Code': 400, 'Message': 'the necessary params is not given'})

    def test_pdfToPics(self):
        file2pics     = FileToPics(filepath = '/home/test.pdf', picpath = '/home/test/', filetype = 'pdf')
        resData       = file2pics.file_to_pics()

        self.assertNotEqual(resData, None)

    def test_fileToPics(self):
        file2pics     = FileToPics(filepath = '/home/test.pptx', picpath = '/home/test/', filetype = 'pdf')
        resData       = file2pics.file_to_pics()

        self.assertNotEqual(resData, None)


if __name__ == '__main__':
    unittest.main()
