import os, sys, argparse
import catalog, utils
import ourlogging

logger = ourlogging.logger("command")

def all_packages():
    return catalog.full_list
            
class Packages():
    @staticmethod
    def calc_packages(args):
        if args['all-except']:
            return list(set(all_packages()) - set(args['packages']))
        else:
            return args['packages']
    
    def __init__(self, args):
        self.packages = self.calc_packages(args)

        self.args = args

    def dofor(self, func):
        #TODO make parallel version
        d = {}
        for p in self.packages:
            d[p] = func(p, self.args)
        return d

def find_file(package, location):
    # read through all the file names.
    for filename in os.listdir(location):
        if filename.startswith(package['name']):
            return location + filename


def fetch(args):
    def dofetch(package, args):
        r = {}
        
        print "Downloading ", package + "..."
        loc = None
        try:
            loc = utils.downloadLatest(catalog.catalog[package], location=args['dir']+'\\', overwrite=args['overwrite'])
        except:
            pass

        if loc != None:
            r['location'] = loc

        return r
            
    packages = Packages(args)
    
    results = packages.dofor(dofetch)


def install(args):
    def doinstall(package, args):
        r = {}

        catapackage = catalog.catalog[package]
        path = args['dir']+'\\'

        if not args['installonly']:
            loc = utils.downloadLatest(catapackage, location=path, overwrite=args['overwrite'])
        else:
            loc = find_file(catapackage, path)
        
        if args['installonly']:
            utils.installPackage(catapackage, loc)
        else:
            utils.downloadAndInstallLatest(catapackage, path)
        
        return r

    packages = Packages(args)
    
    results = packages.dofor(doinstall)


def version(args):
    def doversion(package, args):
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
    
    packages_parser = argparse.ArgumentParser(add_help=False)
    packages_parser.add_argument('packages', nargs='*', default=all_packages(),
                                 help="""The list of packages to execute the command with. Defaults to all.""")    
    packages_parser.add_argument('--all-except', dest='all-except', action='store_true',
                                 help="Executes all packages, EXCPET those specified in 'packages'.")

    fetching_parser = argparse.ArgumentParser(add_help=False)
    fetching_parser.add_argument('-d', '--download-directory', dest="dir",
                              default="downloads",
                              help="The download directory")
    fetching_parser.add_argument('--overwrite', dest="overwrite", action='store_true',
                              help="Allow overwriting of files.")
    
    subparsers = parser.add_subparsers()

    # create the parser for the "fetch" command
    parser_fetch = subparsers.add_parser('fetch', parents=[packages_parser, fetching_parser])
    parser_fetch.set_defaults(func=fetch)

    # create the parser for the "install" command
    parser_install = subparsers.add_parser('install', parents=[packages_parser, fetching_parser])
    parser_install.add_argument('-i', '--install-only', dest="installonly",
                              action='store_true',
                              help="Skip downloading.")
    parser_install.set_defaults(func=install)

    # create the parser for the "version" command
    parser_version = subparsers.add_parser('version', parents=[packages_parser])
    parser_version.set_defaults(func=version)
    
    # create the parser for the "valid" command
    parser_valid = subparsers.add_parser('valid', parents=[packages_parser])
    parser_valid.set_defaults(func=valid)
    
    args = parser.parse_args(sys.argv[1:])
    args.func(vars(args))

if __name__ == "__main__":
    main()
