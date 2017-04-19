import sys
import os
import json    
import subprocess


class FileToPics:
    def __init__(self, **kwargs) :
        self.filePath      = kwargs.get('filePath', '')
        self.picPath       = kwargs.get('picPath', '')
        self.fileName      = os.path.basename(self.filePath)
        self.fileExt       = kwargs.get('fileExt', '')
        self.picExt        = kwargs.get('picExt', 'webp')
        self.picExtList    = ['webp', 'jpeg', 'jpg', 'png']
        self.fileExtlist   = ['ppt', 'pptx', 'doc', 'docx']
        
    def checkParams(self):
        ret = 0

        if not (self.filePath and self.picPath and self.picExt and self.fileExt):
            ret = 400

        return ret

    def fileToPicture(self):
        ret = self.checkParams()
        if ret != 0:
            return self.returnResponse(ret, 'the necessary params is not given')

        if self.picExt not in self.picExtList:
            return self.returnResponse(401, 'the params picExt is invalid')

        if not os.path.exists(self.filePath):
            return self.returnResponse(402, 'the file is not found')

        pdfPath = self.filePath

        if self.fileExt in self.fileExtlist:
            ret = self.fileToPdf(self.filePath, self.picPath)
            if ret != 0:
                return self.returnResponse(ret, 'the file to pdf error')

            fileName     = self.fileName.split('.')[0]
            pdfPath     =  self.picPath + fileName + '.pdf'

        ret = self.pdfToPictures(pdfPath, self.picPath, self.picExt)

        if ret != 0:
            return self.returnResponse(ret, 'the file to images error')
        
        return self.returnResponse(ret, 'the file to images success')

    def fileToPdf(self, filePath, pdfPath):
        ret          = 0
        fileName     = self.fileName.split('.')[0]
        cmd          = 'libreoffice --invisible --headless --convert-to pdf:writer_pdf_Export '+filePath+' --outdir '+ pdfPath

        try:
            proc     = subprocess.run(cmd, stdin = subprocess.PIPE, input = None, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, timeout = None)
            outStr   = proc.stdout

            if proc.returncode != 0:
                ret  = 501

        except Exception as e:
            ret = 502
        
        return ret
    
    def pdfToPictures(self, pdfPath, picPath, ext='png'):
        ret = 0
        
        if not os.path.exists(pdfPath):
            return self.returnResponse(402, 'pdf file is not found, ' + pdfPath)

        fileName     = self.fileName.split('.')[0]

        imgDir = picPath + fileName + '/'

        if not os.path.exists(imgDir):
            os.makedirs(imgDir, 0o777)

        try:
            imgCmd  = 'convert ' + pdfPath + ' ' + imgDir + fileName + '-%d.' + ext
            proc    = subprocess.run(imgCmd, stdin = subprocess.PIPE, input = None, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, timeout = None)
            if proc.returncode != 0:
                ret = 501

        except Exception as e:
            ret = 502
        
        return ret

    def returnResponse(self, code, retMessage):
        ret        = dict(Code = code, Message = retMessage)
        return json.dumps(ret)

if __name__ == '__main__':

    #file2pics = FileToPics(picpath = '/home/caomingzhu/ppttopic/jiaoben/', filetype = 'pdf')
    file2pics = FileToPics(filePath = '/home/caomingzhu/python/githubppt/file/3-mini.pptx', picPath = '/home/caomingzhu/python/githubppt/images/', fileExt = 'ppt', picExt = 'png')
    res = file2pics.fileToPicture()
    
    print(json.dumps(res))
   
