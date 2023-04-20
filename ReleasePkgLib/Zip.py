from zipfile import ZipFile
from datetime import datetime


# path:Unzip file path.
def UnZip(path):
    with ZipFile(path, 'r') as my_zip:
        for file in my_zip.namelist():
            my_zip.extract(file,path.rstrip(".zip"))
        my_zip.close()


# Print the information of the zip file.
def PrintZipAllInfo(path):
    zf = ZipFile(path)
    for info in zf.infolist():
        print(info.filename)
        print('\tComment:\t' + str(info.comment))
        print('\tModified:\t' + str(datetime(*info.date_time)))
        print('\tZIP version:\t' + str(info.create_version))
        print('\tCompressed:\t' + str(info.compress_size) + 'bytes')
        print('\tUncompressed:\t' + str(info.file_size) + 'bytes')


# Get the date of the file in the zip file.
def GetZipDateInfo(path, name):
    zf = ZipFile(path)
    for info in zf.infolist():
        if name in info.filename:
            return datetime(*info.date_time).strftime("%Y/%m/%d")