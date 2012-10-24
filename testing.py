import catalog, utils
import datetime




class simpleLog():
    def __init__(self):
        self.fo = open('validateLog.txt','w')
    def write(self,function,package_list):
        self.fo.write(('#'*20)+str.upper(function)+('#'*20)+'\n')
        for item in package_list:
            self.fo.write(item+'\n')
        self.fo.write(('#'*20)+str.upper(function)+('#'*20)+'\n')
    def close(self):
        self.fo.close()
                 
Log = simpleLog()
def webVersionValidate():
    package_str = ''
    failed_package =[]
    for entry in catalog.full_list:
        if entry != 'EMPTY':
            try:
                package_str = entry
                package_str += "    "+utils.getWebVersion(catalog.catalog[entry])
            except Exception, e:
                package_str += "    %s" % e
                failed_package.append(package_str)
            print package_str
    Log.write('Web version',failed_package)

def localVersionValidate():
    package_str = ''
    failed_package =[]
    for entry in catalog.full_list:
        if entry != 'EMPTY':
            try:
                package_str = entry
                test = utils.getInstalledVersion(catalog.catalog[entry])
                if test is None:
                    package_str += '     has not been defined yet' 
                    failed_package.append(package_str)
            except Exception, e:
                package_str += "    %s" % e
                failed_package.append(package_str)
            print package_str
    Log.write('local Version',failed_package)

def runValidation(test_list):
    """ ie run runValidation(['web','local'])"""
    for test in test_list:
        if test == 'web':
            webVersionValidate()
        elif test == 'local':
            localVersionValidate()
    Log.close()
        
    
