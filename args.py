import sys, argparse
import catalog, utils
import ourlogging

logger = ourlogging.logger("command")

class Packages():
    def __init__(self, args):
        self.packages = args.packages

    def dofor(self, func):
        #TODO make paralle version
        d = {}
        for p in self.packages:
            d[p] = func(p)
        return d



def fetch(args):
    def dofetch(package):
        r = {}
        
        print "Downloading ", package + "..."
        loc = None
        try:
            loc = utils.downloadLatest(catalog.catalog[package])
        except:
            pass

        if loc != None:
            r['location'] = loc

        return r
            
    packages = Packages(args)
    
    results = packages.dofor(dofetch)


def version(args):
    def doversion(package):
        r = {'update': False}
        
        print "###", package, "###"
        
        webV = utils.getWebVersion(catalog.catalog[package])
        localV = utils.getInstalledVersion(catalog.catalog[package])
        r['webV'] = webV
        r['localV'] = localV
        print "Web  :", webV
        print "Local:", localV
        logger.info("'" + package + "' Web Version: " + str(webV))
        logger.info("'" + package + "' Local Version: " + str(localV))
        
        if webV != localV:
            print "! Update Needed"
            r['update'] = True

        print "\n",
        
        return r

    packages = Packages(args)
    
    results = packages.dofor(doversion)

    updatelist = []
    for k, v in results.items():
        if v['update']:
            updatelist.append(k)

    print "Packages that need to be updated: "
    print updatelist

    return updatelist


def valid(args):
    valid = True
    
    ###
    #Check 'full_list' matches 'catalog'
    s = set()
    for item in catalog.full_list:
        s.add(item)
    badkeylist = []
    for key, value in catalog.catalog.items():
        try:
            s.remove(key)
        except KeyError:
            valid = False
            logger.info("'%s' not in catalog.catalog but is in catalog.full_list" % key)
            badkeylist.append(key)
    print "\n=> The following packages are not in catalog.catalog, but are in catalog.full_list:"
    print badkeylist
    badkeylist = []
    for item in s:
        valid = False
        logger.info("'%s' not in catalog.full_list but is in catalog.catalog" % item)
        badkeylist.append(key)
    print "\n=> The following packages are not in catalog.full_list but are in catalog.catalog:"
    print badkeylist

    ###
    # Finish
    if valid:
        print "\n==>> Valid!"
    else:
        print "\n==>> Not Valid"

    return valid

def main():
    parser = argparse.ArgumentParser()
    shared_parser = argparse.ArgumentParser(add_help=False)
    shared_parser.add_argument('--foo', action='store_true')
    subparsers = parser.add_subparsers()

    # create the parser for the "fetch" command
    parser_fetch = subparsers.add_parser('fetch', parents=[shared_parser])
    parser_fetch.add_argument('packages', nargs='*', default=catalog.full_list)
    parser_fetch.set_defaults(func=fetch)

    # create the parser for the "version" command
    parser_version = subparsers.add_parser('version', parents=[shared_parser])
    parser_version.add_argument('packages', nargs='*', default=catalog.full_list)
    parser_version.set_defaults(func=version)
    
    # create the parser for the "valid" command
    parser_valid = subparsers.add_parser('valid', parents=[shared_parser])
    parser_valid.set_defaults(func=valid)
    
    args = parser.parse_args(sys.argv[1:])
    args.func(args)

if __name__ == "__main__":
    main()
