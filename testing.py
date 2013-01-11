import catalog, utils
import datetime




class simpleLog():
    def __init__(self):
        self.fo = open('validateLog.log','w')
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

def localVersionSearchValidate():
    package_str =''
    failed_package = []
    for entry in catalog.full_list:
        if entry != 'EMPTY' and catalog.catalog[entry]['installversion']['querytype'] == 'regvalsearch':
            test = utils.getInstalledVersion(catalog.catalog[entry])
            print entry
            print test
            if test is None:
                package_str += '     Has not been defined yet'
                failed_package.append(package_str)
    Log.write('local search',failed_package)
def downloadUrlValidate():
    package_str =''
    failed_package = []
    for entry in catalog.full_list:
        if entry != 'EMPTY':
            try:
                package_str = entry
                test = utils.getDownloadURL(catalog.catalog[entry])
                if test is None:
                    package_str += '     Has not been defined yet'
                    failed_package.append(package_str)
            except Exception, e:
                package_str += "    %s" % e
                failed_package.append(package_str)
    Log.write('downloadurl search',failed_package)

def downloadValidate():
    package_str =''
    failed_package = []
    for entry in catalog.full_list:
        if entry != 'EMPTY':
            try:
                package_str = entry
                utils.downloadLatest(catalog.catalog[entry])
            except Exception, e:
                package_str += "    %s" % e
                failed_package.append(package_str)
    Log.write('downloadlatest',failed_package)
		

def runValidation(test_list):
    """ ie run runValidation(['web','local'])"""
    for test in test_list:
        if test == 'web':
            webVersionValidate()
        elif test == 'local':
            localVersionValidate()
        elif test == 'search':
            localVersionSearchValidate()
        elif test =='downloadurl':
            downloadUrlValidate()
        elif test == 'download':
            downloadValidate()
    Log.close()


        
    
