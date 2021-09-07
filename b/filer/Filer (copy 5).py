def createFolder(folderName):
    
    '''Creates sub-folder of given name in projects root
    directory and returns its path'''
    
    import os
    target = os.getcwd() + '/'+ folderName
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

def readGeneralSettingsFile(request):
    import os
    settings = os.getcwd() + '/settings/GeneralSettings.txt'
    
    if(not os.path.exists(settings)):
        print('Path %s does not exists'%(settings))
        input('TODO: Exception should be raised here....')        
    else:
        f = open(settings,'r')
        tokens = f.readline().strip()
        daysList = list()
        for l in f:
            if(l.startswith('%s'%(request))):
                t  = l.strip().split('%s'%(tokens))
                return t[-1]
    print('Nothing found about %s in generalSettingsfile...'%(request))
    input('TODO: Exception')        
    return None
