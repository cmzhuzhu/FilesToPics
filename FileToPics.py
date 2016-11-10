import sys
import os
import json    
import subprocess


class FileToPics:
    def __init__(self, **kwargs) :
        self.filepath = kwargs.get('filepath', '')
        self.picpath  = kwargs.get('picpath', '')
        self.filename = os.path.basename(self.filepath)
        self.filetype = kwargs.get('filetype', '')
        self.pictype  = kwargs.get('pictype', 'webp')
        self.info     = dict()

    def check_params(self):
        if not (self.filepath and self.picpath and self.pictype and self.filetype):
            res = {'Code': 400, 'Message': 'the necessary params is not given'}
        else:
            res = {'Code': 0, 'Message': 'check params success'}
        return res

    def check_path(self, filepath):
        check = os.path.exists(filepath)
        if not check:
            res = {'Code': 400, 'Message': 'the file: '+filepath+' is not found'}
        else:
            res = {'Code': 0, 'Message': 'success'}

        return res


    def file_to_pics(self):
        check_params = self.check_params()
        check_path   = self.check_path(self.filepath)

        if check_params['Code'] != 0:
            return check_params

        if check_path['Code'] != 0:
            return check_path

        if self.filetype == 'pdf':
            pic_res = self.pdf_to_pics(self.filepath, self.picpath, self.pictype)
        else:
            pdf_res = self.file_to_pdf(self.filepath, self.picpath)
            if pdf_res['PdfCode'] == 0:
                pic_res = self.pdf_to_pics(pdf_res['PdfPath'], self.picpath, self.pictype)
            else:
                return json.dumps(pdf_res)

        if pic_res != 0:
            res = {'Code': 500, 'Message': 'the file to pics failed'}
        else:
            res = {'Code': 0, 'Message': 'the file to pics success'}
            return json.dumps(res)

    def file_to_pdf(self, file_path, pdf_path):
        full_filename = self.filename
        file_name     = full_filename.split('.')[0]
        cmd       = 'libreoffice --invisible --headless --convert-to pdf:writer_pdf_Export '+file_path+' --outdir '+ pdf_path
        proc      = subprocess.run(cmd, stdin = subprocess.PIPE, input = None, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, timeout = None)
        
        outStr   = proc.stdout
        #errStr   = proc.stderr
        pdf_code  = proc.returncode
        return dict(PdfCode = pdf_code, PdfPath = pdf_path+file_name+'.pdf')
    
    def pdf_to_pics(self, pdf_path, pic_path, type='webp'):
        check = os.path.exists(pdf_path)
        if not check:
            return {'Code': 500, 'Message': 'pdf file is not found, '+pdf_path}
        full_filename = self.filename
        file_name     = full_filename.split('.')[0]

        img_dir = pic_path+file_name+'/'
        check = self.check_path(img_dir)
        if check['Code'] != 0:
            os.makedirs(img_dir)

        img_cmd = 'convert '+pdf_path+' '+img_dir+file_name+'-%d.'+type
        img_code = os.system(img_cmd)
        return img_code


if __name__ == '__main__':

    file2pics = FileToPics(picpath = '/home/caomingzhu/ppttopic/jiaoben/', filetype = 'pdf')
    res = file2pics.file_to_pics()
    print(json.dumps(res))
   
