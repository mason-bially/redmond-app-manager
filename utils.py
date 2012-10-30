""" @file utils.py
@brief Utility functions to help with windows package management.

@author Phillip Nordwall <Phillip.Nordwall@wwu.edu>, <phillip@cs.wwu.edu>
@copyright {2011 Phillip Nordwall, Western Washington University Computer
Science Department, http://www.cs.wwu.edu}
@section LICENSE

Copyright (c) 2011 Phillip Nordwall, Western Washington University Computer
Science Department, http://www.cs.wwu.edu

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import urllib2
import re
import os
import _winreg
import copy
import sys
import catalog
import cookielib
import platform
import ourlogging

#We emulate Mozilla Firefox on Windows 7 64 bit as our UA
red=urllib2.HTTPRedirectHandler()
userAgent=[('User-Agent',' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0')]
cj = cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),red)
opener.addheaders=userAgent


def getPage(url):
    """Returns the contents of a url as a string.

    This currently doesn't do anything to handle exceptions.

    @param url The url to grab a page from.
    @return A string containing the page contents of url.
    """
    try:
        opener.addheaders=userAgent + [('Referer', url)]
        f=opener.open(url)
        page = f.read()
        f.close()
    except urllib2.URLError:
        print 'Couldn not connect to and read from %s' % url
    except Exception, e:
        print ' %s while running  getPage(%s)' % (e,url)
        raise
    else:
        return page

def scrapePage(reg, url, pos=0):
    """Scrapes the page from url for the reg at position pos.

    This will return the pos'th match of the regular expression reg from the
    page at url. pos defaults to 0.

    @param reg The regular expression to match.
    @param url The page to scrape.
    @param pos Which regulare expression match to return, defaults to 0.
    @return The pos'th reg match on the page at url.
    """
    try:
        ret = re.findall(reg, getPage(url))[pos]
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' % reg
        elif strerror == 'expected string or buffer':
            print 'your have no page being returned by getPage()'
        print 'when calling scrapePage(%s, %s, %d)' %(reg, url, pos)
    except IndexError:
        print 'regexpos entry larger then the number of results mathing regex '
        print 'when calling scrapePage(%s, %s, %d)' %(reg, url, pos)
    except Exception, e:
        print '%s while running  scrapePage(%s, %s, %d)' % (e,reg, url, pos)
        raise
    else:
        return ret

def scrapePageDict(d):
    """Scrapes the page from d['url'] for the d['regex'] at position 
    d['regexpos'].

    This will return the d['regexpos']'th match of the regular expression
    d['regex'] from the page at d['url'].

    @param d A dictionary that contains 'regex' The regular expression to match.
    'url' The page to scrape.
    'regexpos' Which regular expression match to return, defaults to 0.
    @return The regexpos'th reg match on the page at url.
    """
    try:
        ret = re.findall(d['regex'], getPage(d['url']))[d['regexpos']]
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' %d
        elif strerror == 'expected string or buffer':
            print 'your have no page being returned by getPage()'
        print 'when calling scrapePageDict(%s)' %d
    except IndexError:
        print 'regexpos entry larger then the number of results mathing regex '
        print 'when calling scrapePageDict(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling scrapePage(%s)' %d
    except Exception, e:
        print '%s while running scrapePage(%s)' % (e,d)
        raise
    else:
        return ret

def getWebVersion(d):
    """Get the version from the web of the catalog entry in d

    Use the page at the url specified in d['version']['url'], and the regular
    expression specified in d['version']['regex'] to find the latest version
    number of the passed package. The d['version']['regexpos']'th match of the
    regular expression is returned.

    @param d The dictionary entry for a package, containing at least an entry
    for 'version' that is a dictionary that contains a 'url', 'regex', and
    'regexpos'
    @return the version number matched by the regular expression and page
    passed in.
    """
    try:
        ret = scrapePageDict(d['version'])
    except KeyError:
        print 'd did not contain a "version" entry'
        print 'when calling getWebVersion(%s)' %d
    except Exception, e:
        print '%s while running getWebVersion(%s)' % (e,d)
        raise
    else:
        return ret

def getDownloadURL(d):
    """Get the DownloadURL from the web of the catalog entry in d

    Use the download type specified in d['download']['downloadtype']
    if downloadtype is direct download, download the file stored at d['download']['url'].
    If the download type is  pagesearch use the url specified in d['download']['url'] and the regular
    expression specified in d['download']['regex'] to find the download url of
    the latest version of the passed package. The d['download']['regexpos']'th
    match of the regular expression is returned.

    @param d The dictionary entry for a package, containing at least an entry
    for 'download' that is a dictionary that contains a 'url', 'regex' and
    'regexpos'
    @return the download url matched by the regular expression and page passed
    in.
    """
    try:
        expandedVersion=expandVersion(d)
        downurl=expandedVersion['download']['url']
        
        #Here is a switch to determine action based on download type. Default is direct download
        if d['download']['downloadtype']=='pagesearch':
            downurl = scrapePageDict(expandedVersion['download'])

        opener.addheaders=userAgent + [('Referer', downurl)]
        fredirectedurl = opener.open(downurl)
        
        redirectedurl = fredirectedurl.geturl()
        fredirectedurl .close()
    except urllib2.URLError:
        print 'could not connect to %s' %d['download']['url']
        print 'when calling getDownloadURL(%s)' %d
    except KeyError:
        print 'd did not contain a "download" entry'
        print 'when calling getDownloadURL(%s)' %d
    except Exception, e:
        print '%s while running getDownloadURL(%s)' % (e,d)
        raise
    else:
        return redirectedurl

def downloadLatest(d, location='downloads\\', overwrite=False):
    """Download the latest version of the package d.

    Use the information specified in the package d to download the latest
    version of the package from the web. The default download location is
    './downloads'

    @param d The dictionary entry for a package, containing at least a 'name', 
    as well as a 'version', and 'download' dict containing 'url', 'regex', and
    'regexpos'.
    @param location The location to download the file to.
    @param overwrite Boolean enabling overwriting of a file if it exists.
    @return the path to the downloaded file.
    """
    try:
        name = d['name']
        version = getWebVersion(d)
        downurl = getDownloadURL(d)

        #Sourceforge Antibot Hack
        if "sourceforge" in downurl:
            opener.addheaders=[]
        else:
            opener.addheaders=userAgent + [('Referer', downurl)]
        furl = opener.open(downurl)
        furl=opener.open(furl.geturl())
        parsed=urllib2.urlparse.urlparse(furl.geturl())
        pathname = urllib2.url2pathname(parsed.path)
        filename = pathname.split("\\")[-1]
        newfileloc = location + name + '---' + version + '---' + filename
        print "Downloading: %s" % newfileloc
        # if the file doesn't exist or we allow overwriteing write the file
        if overwrite or not os.path.exists(newfileloc):
            #XXX This needs to be modified to be done in blocks.
            
            with open(newfileloc, "wb") as f:
                block=furl.read(2**20)
                written=0.0
                percent=0.01
                if "Content-Length" in furl.headers:
                    print "File Size:"+furl.headers["Content-Length"]
                
                while block:
                    f.write(block)
                    written+=len(block)
                    if "Content-Length" in furl.headers:
                         try:
                             x=written/float(furl.headers["Content-Length"])
                             if x>percent:
                                 percent=round(x,2)+.01
                                 sys.stdout.write("..."+str((percent-0.01)*100)+"%...")
                         except Exception as e:
                             print e
                    block=furl.read(2**20)
                print ""
        else:
            print 'File already exists and overwriting was not enabled'
            print 'when calling downloadLatest(%s, %s, %s)' %(d, location, overwrite)
        furl.close()
    except IOError as (errno, strerror):
        print 'could not open file, I/O error({0}): {1}'.format(errno, strerror)
        print 'when calling downloadLatest(%s, %s, %s)' %(d, location, overwrite)
    except TypeError as strerror:
        print "TypeError: %s, location may not be a string" % strerror
        print 'when calling downloadLatest(%s, %s, %s)' %(d, location, overwrite)
    except urllib2.URLError:
        print 'could not connet to and read from %s' % downurl
        print 'when calling downloadLatest(%s, %s, %s)' %(d, location, overwrite)
    except KeyError:
        print 'd did not contain a "name" entry'
        print 'when calling downloadLatest(%s, %s, %s)' %(d, location, overwrite)
    except Exception, e:
        print '%s while running downloadLatest(%s, %s, %s)' %(e,d, location, overwrite)
        raise
    else:
        return newfileloc

def getInstalledRegkeyVersion(d):
    """Get the version of the installed package from a registry value.

    Use the information specified in the package d to lookup the installed
    version on the computer. 

    @param d A installversion dictionary entry for a package containing at
    least entries for 'key', 'subkey', 'regex', and 'regexpos'
    @return The version installed or None.
    """
    if(platform.machine =='i386'):
        if ("-64" in d['name']):
            return None
        else:
            mask=_winreg.KEY_READ
    else:
            
        if "-64" in d['name']:
            mask= _winreg.KEY_READ|_winreg.KEY_WOW64_64KEY
        else:
            mask=_winreg.KEY_READ|_winreg.KEY_WOW64_32KEY
    try:
        d = d['installversion']
        # should do a lookup table here
        if d['key'] == 'HKLM':
            tempkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, d['subkey'],0,mask)
        else:
            return None
        keys = _winreg.QueryInfoKey(tempkey)[0]
        keynames = sorted([_winreg.EnumKey(tempkey,i) for i in xrange(keys)])
        keynamesstr = "\n".join(keynames)
        version = re.findall(d['regex'], keynamesstr)[d['regexpos']]
        return version
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' %d
        elif strerror == 'expected string or buffer':
            print 'your have no value being pulled from the registry'
        print 'when calling getInstalledRegkeyVersion(%s)' %d
    except WindowsError:
        print 'The registry key or value could not be found'
        print 'when calling getInstalledRegkeyVersion(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling getInstalledRegkeyVersion(%s)' %d
    except Exception, e:
        print '%s while running getInstalledRegkeyVersion(%s)' % (e,d)
    else:
        return None


def getInstalledRegvalsearchVersion(d):
    """Get the version of the installed package from a registry value.

    Use the information specified in the package d to lookup the installed
    version on the computer.

    @param d A installversion dictionary entry for a package containing at
    least entries for 'key', 'subkey', 'regex', 'valsearchregex', 'value', and 'regexpos'
    @return The version installed or None.

    'value' specifies which value to search on DisplayName or DisplayIcon have been use, 'valsearchregex'
    is the regex used on value to determine if key is correct package.
    
    This function also will search all of the subkeys of a key as well as the key itself
    In order to handle the case of searching SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall
    Where Key names themselves can be cryptic, making it hard to find installed Versions

    EX: Key={3156336D-8E44-3671-A6FE-AE51D3D6564E}
    Step 1: Regval displayname, match some version
    Step 2: Regval the found key, match displayversion

    """
    t = []
    if(platform.machine =='i386'):
        if ("-64" in d['name']):
            return None
        else:
            mask=_winreg.KEY_READ
    else:
        if "-64" in d['name']:
            mask= _winreg.KEY_READ|_winreg.KEY_WOW64_64KEY
        else:
            mask=_winreg.KEY_READ|_winreg.KEY_WOW64_32KEY
            
    try:
        
        d=d['installversion']
        #import pdb
        #pdb.set_trace()
        #Open Uninstall
        if d['key'] == 'HKLM':
            un = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,d['subkey'],0,mask)
        else:
            return None
        unlen = _winreg.QueryInfoKey(un)[0]
        
        #LP Env: Enumerate all subkeys of uninstall   
        for i in range(unlen):
            key=_winreg.OpenKey(un,_winreg.EnumKey(un,i))
            vallen=_winreg.QueryInfoKey(key)[1]
            #Lp env: Enum each value of given subkey
            for j in range(vallen):
                #Check Value Name. If it matches d['value'] we have the correct node
                value=_winreg.EnumValue(key,j)
                if value[0] == d['value']:
                    #t.append(value[1])
                    
                    #If we are at the correct key. 
                    if(re.search(d['valsearchregex'],value[1]) ): #valsearchregex, what you want to find in the DisplayName
                        #Gets a list of tuples to search through for DisplayVersion
                        keynames = sorted([_winreg.EnumValue(key,l) for l in xrange(vallen)])
                        for key in keynames:
                            if key[0]=='DisplayVersion':
                                version=re.search(d['regex'],key[1]).group(0)
                                return version
        
                    
 
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print ('you are missing or have an invalid regex')
        elif strerror == 'expected string or buffer':
            print ('your have no value being pulled from the registry')
          
    except WindowsError:
        print ('The registry key or value could not be found')
      
    except KeyError as strerror:
        print ('did not contain a key entry')
       
    except Exception, e:
        print '%s while running getInstalledRegvalsearchVersion(%s)' % (e,d)
    else:
        return None
def getInstalledRegvalnameVersion(d):
    """Get the version of the installed package from a registry value.

    Use the information specified in the package d to lookup the installed
    version on the computer.

    @param d A installversion dictionary entry for a package containing at
    least entries for 'key', 'subkey', 'regex', and 'regexpos'
    @return The version installed or None.
    """
    if(platform.machine =='i386'):
        if "-64" in d['name']:
            return None
        else:
            mask=_winreg.KEY_READ
    else:
            
        if "-64" in d['name']:
            mask= _winreg.KEY_READ|_winreg.KEY_WOW64_64KEY
        else:
            mask=_winreg.KEY_READ|_winreg.KEY_WOW64_32KEY
    try:
        d=d['installversion']
        # should do a lookup table here
        if d['key'] == 'HKLM':
            tempkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, d['subkey'],0,mask)
        else:
            return None
        vals = _winreg.QueryInfoKey(tempkey)[1]
        valnames = [_winreg.EnumValue(tempkey,i)[0] for i in xrange(vals)]
        valnames = sorted(valnames)
        valnamesstr = "\n".join(valnames)
        version = re.findall(d['regex'], valnamesstr)[d['regexpos']]
        return version
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' %d
        elif strerror == 'expected string or buffer':
            print 'your have no value being pulled from the registry'
        print 'when calling getInstalledRegvalnameVersion(%s)' %d
    except WindowsError:
        print 'The registry key or value could not be found'
        print 'when calling getInstalledRegvalnameVersion(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling getInstalledRegvalnameVersion(%s)' %d
    except Exception, e:
        print '%s while running getInstalledRegvalnameVersion(%s)' %(e,d)
    else:
        return None

def getInstalledRegvalVersion(d):
    """Get the version of the installed package from a registry value.

    Use the information specified in the package d to lookup the installed
    version on the computer.

    @param d A installversion dictionary entry for a package containing at
    least entries for 'key', 'subkey', 'value', 'regex', and 'regexpos'
    @return The version installed or None.
    """
    if(platform.machine =='i386'):
        if "-64" in d['name']:
            return None
        else:
            mask=_winreg.KEY_READ
    else:
            
        if "-64" in d['name']:
            mask= _winreg.KEY_READ|_winreg.KEY_WOW64_64KEY
        else:
            mask=_winreg.KEY_READ|_winreg.KEY_WOW64_32KEY
    try:
        d= d['installversion']
        # should do a lookup table here
        if d['key'] == 'HKLM':
            tempkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, d['subkey'],mask)
            value = str(_winreg.QueryValueEx(tempkey, d['value'])[0])
            version = re.findall(d['regex'], value)[d['regexpos']]
            return version
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' %d
        elif strerror == 'expected string or buffer':
            print 'your have no value being pulled from the registry'
        print 'when calling getInstalledRegvalVersion(%s)' %d
    except WindowsError:
        print 'The registry key or value could not be found'
        print 'when calling getInstalledRegvalVersion(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling getInstalledRegvalVersion(%s)' %d
    except Exception, e:
        print '%s while running getInstalledRegvalVersion(%s)' %(e,d)
    else:
        return None
    
def getInstalledFilePathVersion(d):
    try:
       tempPath = os.listdir(d['path'])
       valnames = sorted(tempPath)
       valnamesstr = "\n".join(valnames)
       version =re.findall(d['regex'], valnamesstr) [d['regexpos']]
       return version
    except TypeError as strerror:
        if strerror == 'first argument must be a string or compiled pattern':
            print 'you are missing or have an invalid regex in %s' %d
        elif strerror == 'expected string or buffer':
            print 'your have no value being pulled from the registry'
        print 'when calling getInstalledFilePathVersion(%s)' %d
    except WindowsError:
        print 'The registry key or value could not be found'
        print 'when calling getInstalledFilePathVersion(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling getInstalledFilePathVersion(%s)' %d
    except:
        print 'unkown error running getInstalledFilePathVersion(%s)' %d
    else:
        return None

def getInstalledVersion(d):
    """Get the version of the installed package.

    Use the information specified in the package d to lookup the installed
    version on the computer. 

    @param d The dictionary entry for a package containing at least a
    'installversion' dictionary, which itself must contain a 'type' entry.
    Currently supported types are 'regval' which must have a key, subkey,
    regex, regexpos, and value entry. 'regkey' which must have a key, subkey,
    regex, and regexpos entry. 'regvalname' which must have a key, subkey,
    regex, and regexpos entry.

    @return The version installed or None.
    """
    try:
        #import ipdb; ipdb.set_trace(); #Remove when debuging finished. --Camille
        querytype = d['installversion']['querytype']
        if querytype == 'regval':
            return getInstalledRegvalVersion(d)
        elif querytype == 'regvalname':
            return getInstalledRegvalnameVersion(d)
        elif querytype == 'regkey':
            return getInstalledRegkeyVersion(d)
        elif querytype=="regvalsearch":
            return getInstalledRegvalsearchVersion(d)
        elif querytype == 'filepathname':
            return getInstalledFilePathVersion(d['installversion']) # camille working on
        else:
            print 'unknown querytype: %s' % querytype
            print 'when calling getInstalledVersion(%s)' %d
    except KeyError as strerror:
        print 'd did not contain a "%s" entry' % strerror
        print 'when calling getInstalledVersion(%s)' %d
    except Exception, e:
        print '%s while running getInstalledVersion(%s)' %(e,d)
    else:
        return None

def installPackage(d, location):
    """Install the package at location.

    Use the information specified in the package d to run the installer at 
    location with the correct commandline options.

    @param d The dictionary entry for a package, containing at least a 'name', 
    as well as a 'version', a 'download' dict containing 'url', 'regex', and
    'regexpos' a 'silentflags' entry containing silent command line options for
    the installer.
    @param location The location to install from.
    @return The value returned by the installer
    """
    try:
        print "installing: %s" % location
        # no silent flags for now 
		#ret = os.system('"' + location + '" ' + d['silentflags'])
        ret = os.system('"' + location + '" ')
    except Exception, e:
        print '%s while running installPackage(%s, %s)' %(e,d, location)
    else:
        return ret

def downloadAndInstallLatest(d, location='downloads\\', keep=True):
    """Download the latest version of the package d and install it.

    Use the information specified in the package d to download the latest
    version of the package from the web. The default download location is
    './downloads' and install it.

    @param d The dictionary entry for a package, containing at least a 'name', 
    as well as a 'version', and 'download' dict containing 'url', 'regex', and
    'regexpos'.
    @param location The location to download the file to.
    @param keep Should we keep the download?
    @return The value returned by the installer
    """
    try:
        fpath = downloadLatest(d, location)
        ret = installPackage(d, fpath)
        
        if not keep and ret == 0:
            os.remove(fpath)
    except WindowsError as (errno, strerror):
        print 'could not remove the file, WindowsError({0}): {1}'.format(errno,
            strerror)
        print 'when calling installPackage(%s, %s)' %(d, location)
    except Exception, e:
        print '%s while running installPackage(%s, %s)' %(e, d, location)
    else:
        return ret

def expandVersion(d):
    """Expand version numbers in download url.

    If the 'download' section of d contains a 'url' section that has a
    ##VERSION##, ##DASHVERSION##,##DOTLESSVERSION## ##UNDERSCOREVERSION##, lookup the latest webversion and
    replace the placeholder with the appropriate text.

    @param d The dictionary entry for a package, containing a valid 'version'
    section and a 'download' section with atleast a 'url' section.
    @return The dictionary with the placeholder if present replaced by the
    version or formatted version.
    
    @todo: XXX: exception handling
    """
    url = d['download']['url']
    if '##VERSION##' in url or '##DOTLESSVERSION##' or '##UNDERSCOREVERSION##'or '##DASHVERSION##' in url:
        ret = copy.deepcopy(d)
        version = getWebVersion(d)
        dotlessversion = re.sub('\.', '', version)
        underscoreversion=re.sub('\.','_', version)
        dashversion=re.sub('\.','-', version)
        url = re.sub('##VERSION##', version, url)
        url = re.sub('##DOTLESSVERSION##', dotlessversion, url)
        url = re.sub('##UNDERSCOREVERSION##', underscoreversion, url)
        url = re.sub('##DASHVERSION##', dashversion, url)
        ret['download']['url'] = url
        return ret
    else:
        return d

def uninstall(d):
    """@todo: XXX: STUB NEEDS FILLED OUT"""
    raise Exception("This is a stub")
    return 0

def upgrade(d):
    """@todo: XXX: STUB NEEDS FILLED OUT"""
    raise Exception("This is a stub")
    return 0

def installColl(catalog, collection, location='downloads\\', keep=True):
    """Download and install all of the applications in the collection.

    Run downloadAndInstallLatest for each catalog entry whose key is in the
    collection.

    \param catalog The catalog of install information.
    \param collection A collection of strings that are keys in catalog. Each
    \param location The path to store the downloaded files.
    \param keep Whether the downloads should be kept.
    catalog entry matching a string in collection gets downloaded and
    installed.
    """
    try:
        for entry in collection:
            downloadAndInstallLatest(catalog[entry], location, keep)
    except Exception, e:
        print '%s while running installColl(%s, %s)' %(e, catalog,
                collection)

def getCollInstalledVersions(catalog, collection):
    """@todo: XXX: STUB NEEDS FILLED OUT"""
    raise Exception("This is a stub")
    return 0

def getCollWebVersions(catalog, collection):
    """@todo: XXX: STUB NEEDS FILLED OUT"""
    raise Exception("This is a stub")
    return 0


def main(argv):
    
    if len(argv)<3:
        print "Usage:python utils.py [version|localversion|fetch|install] {packagename|all}"
        return -1

    package_name=argv[2]
    ourlogging.config(consoleLevel=ourlogging.DEBUG,debugInfo=True)
       
    everything=(package_name=="all")
    if not everything:
        package = catalog.catalog[package_name]

    if argv[1]=="version":
        print getWebVersion(package)
    elif argv[1]=="localversion":
        print getInstalledVersion(package)
    elif argv[1]=="install":
        if everything:
            installColl(catalog.catalog, sorted(catalog.catalog.keys()))
        else:
            downloadAndInstallLatest(package)
    elif argv[1]=="fetch":
        if everything:
            for i in catalog.catalog:
                try:
                    package = catalog.catalog[i]
                    print "Fetching:"+i
                    downloadLatest(package)
                except Exception:
                    print "Could not fetch:"+i
        else:
            downloadLatest(package)        
            

if __name__ == "__main__":   
    main(['utils.py','version','TortoiseSVN-64'])
