#from modul_intrepreter import *
#from modul_commit import *
#from modul_init import *


strInput = input()

def init(nesto):
    print('init')
def add():
    print('add')
def commit():
    print('commit1')
def revertToCommit(nesto):
    print('reverted1')

komande = {'init' : init, 'add' : add, 'commit' : commit, 'revert' : revertToCommit}


def parser(komanda):
    operacija = komanda.split()
    print(operacija[0])
    #print(operacija[1])
    if operacija[0] in komande:
        print('da')
    if operacija[0] == 'commit':
        komande[komanda]()
    else:
        komande[operacija[0]](operacija[1])
    
parser(strInput)