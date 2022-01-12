from zipfile import ZipFile

def extractor (file_name):
    for i in file_name:
        with ZipFile(''E:\\Repos\\Brazilian-Election-Data-Analysis\\Election_Data\\'' + i) as myZip:
            csv = [file for file in myZip.namelist() if ('.csv' or '.txt') in file] 
            myZip.extractall(members=csv, path='E:\Repos\Brazilian-Election-Data-Analysis\Election_Data')