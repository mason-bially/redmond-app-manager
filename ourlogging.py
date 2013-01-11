from logging import *

configured = False

def config(consoleLevel=WARN, fileName='default.log', debugInfo=False):
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
    cf = Formatter('%(asctime)s   %(lineno)-3s@%(packageorcommand)-8s %(levelname)-8s:\n\\_\t%(message)s')
    ff = Formatter('%(asctime)s   %(lineno)-3s@%(packageorcommand)-8s %(levelname)-8s: \t %(message)s')
    #f = Formatter('%(asctime)s - %(levelname)s - %(message)s')
   
    ch.setFormatter(cf)
    fh.setFormatter(ff)
    
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

def logger(name):
    return LoggerAdapter(getLogger(name), {'packageorcommand': name})
