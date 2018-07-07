from distutils.dir_util import copy_tree
import os
import shutil
from parser import *

class File:
    def __init__(self, path):
        self. path = path
    def getPath(self):
        return self.path

komande = {'revert' : revertToCommit}

def parser(komanda,repath):
    operacija = komanda.split()
    print(operacija[0])
    print(operacija[1])
    if operacija[0] in komande:
        print('da')
    if operacija[0] == 'commit':
        komande[komanda]()
    elif operacija[0] == 'revert':
        komande[operacija[0]](File(repath), operacija[1])
    else:
        komande[operacija[0]](operacija[1])
    


def getBackupFile(repositoryPath):
    #Vraca backups file
    return repositoryPath + '\\.backups'
    
def revertToCommit(repository, commit):
    #Kao parametar prima instancu klase file i sting u kom je broj komita (nasa interna verzija) na koji se vraca
    #Vraca repozitorijum u stanje nekog prošlog komita
    
    backupPath = getBackupFile(repository.getPath())
    
    for the_file in os.listdir(repository.getPath()):
        file_path = os.path.join(repository.getPath(), the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path) and (not(file_path == repository.getPath()+'\\.backups')): 
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
    for the_file in os.listdir(backupPath):
        file_path = os.path.join(backupPath, the_file)
        file_path = os.path.join(file_path, commit)
        print(file_path)
        if os.path.isdir(file_path):
            for fileToCopy in os.listdir(file_path):
                if os.path.isdir(file_path + '\\' + fileToCopy):
                        shutil.copytree(file_path + '\\' + fileToCopy,repository.getPath() + '\\' + fileToCopy)
                else:
                        copy_tree(file_path,repository.getPath())
                        
strInput = input()
repath = 'repozitorijum'
parser(strInput, repath)