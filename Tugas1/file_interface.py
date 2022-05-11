import os, os.path
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,filename=''):
        if(filename==''):
            return None
        try:
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    
    # function delete
    def delete(self, params=[]):
        if not (len(params)==1):
            return dict(status='ERROR',data='Error, jumlah parameter hanya satu') # jika parameter salah
        filename=params[0]
        if not os.path.exists(filename):
            return dict(status='ERROR', data=f'File {filename} tidak ditemukan') # jika nama file tidak sesuai
        os.remove(filename)
        return dict(status='OK',data=f'File {filename} telah dihapus')



if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    #print(f.get('pokijan.jpg'))

    print(f.delete(['deletethis.jpg']))

