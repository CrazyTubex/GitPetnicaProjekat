komande = {'init' : init, 'add' : add, 'commit' : commit, 'revert' : revertToCommit}

def parser(komanda,repath):
    #Pretvara komandu u funkciju
    #Prima ukucanu komandu i put do repozitorijuma kao parametre
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
    