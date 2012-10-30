from logging import *

configured = False

def config(consoleLevel=INFO, fileName='default.log', debugInfo=False):
    global configured

    rootLogger = getLogger()
    rootLogger.setLevel(DEBUG)

    #File Handler
    fh = FileHandler(fileName)
    fh.setLevel(DEBUG)

    #Console Handler
    ch = StreamHandler()
    ch.setLevel(consoleLevel)

    #The formmatter
    #vf = Formatter('%(module)-14s:%(lineno)-3s ++ %(packageorcommand)-16s %(levelname)-8s - %(message)s')
    #f = Formatter('%(packageorcommand)-16s %(levelname)-8s - %(message)s')
    f = Formatter('%(asctime)s - %(levelname)s - %(message)s')
   
    ch.setFormatter(f)
    fh.setFormatter(f)
    
    rootLogger.addHandler(fh)
    rootLogger.addHandler(ch)

    configured = True
    return  rootLogger

##def packageLogger(package):
##    return LoggerAdapter(getLogger(package), {'packageorcommand': '|-'+package})
##
##def commandLogger(command):
##    return LoggerAdapter(getLogger(command), {'packageorcommand': command})
##                                              
##def otherLogger(name):
    return LoggerAdapter(getLogger(name), {'packageorcommand': '*'+name})
