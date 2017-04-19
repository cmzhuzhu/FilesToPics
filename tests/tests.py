#!/usr/bin/env python3

# author : caomingzhu
# github : https://github.com/cmzhuzhu
# description : FileToPics test


import unittest
from FileToPics import FileToPics

class TestSimple(unittest.TestCase):
    def testNonFilePathParameter(self):
        file2pics     = FileToPics(picPath = '/home/test/', fileType = 'pdf')
        resData       = file2pics.fileToPicture()
        self.assertEqual(resData, {'Code': 400, 'Message': 'the necessary params is not given'})

    def testPdfToPics(self):
        file2pics     = FileToPics(filePath = '/home/test.pdf', picPath = '/home/test/', fileType = 'pdf')
        resData       = file2pics.fileToPicture()

        self.assertNotEqual(resData, None)

    def testFileToPictures(self):
        file2pics     = FileToPics(filePath = '/home/test.pptx', picPath = '/home/test/', fileType = 'pptx')
        resData       = file2pics.fileToPicture()

        self.assertNotEqual(resData, None)


if __name__ == '__main__':
    unittest.main()
