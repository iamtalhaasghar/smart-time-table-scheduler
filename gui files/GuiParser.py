def createSettingsFolder():

    '''Creates sub-folder "settings" in projects root
    directory and returns its path'''

    import os
    currentP = os.path.dirname(os.getcwd())
    target = currentP + '/settings'
    if(not os.path.exists(target)):
        os.mkdir(target)
    return target

