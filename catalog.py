# NOTE: Some descriptions are taken from an applications web site or from wikipedia.  Camille
name = 'name'
category = 'category'
description = 'description'
emulateuseragent='emulateuersagent'
url = 'url'
regex = 'regex'
version = 'version'
download = 'download'
downloadtype = 'downloadtype'
regexpos = 'regexpos'
silentflags = 'silentflags'
installversion = 'installversion'
key = 'key'
subkey = 'subkey'
value = 'value'
querytype = "querytype"
path = 'path'
valsearchregex = 'valsearchregex'
    

#####ROLE YOUR OWN CAPTURING GROUPS
months="Janurary|February|March|April|May|June|July|August|September|October|November|December"
abmonths="Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
alphabeta="Alpha|Beta|alpha|beta"


#####
minimal_list = [ 'Ghostscript', 'GSview 32bit', 'Gimp', 'ImageMagick',
    '7-Zip', 'Firefox', 'Scribus' ]

##Taking out GPROLOGMSVC
full_list=['Git', 'Mscgen', 'XNAGameStudio', 'ActiveTcl-64',
           'Notepad++', 'Synergy2', 'Pidgin',
           'WindowsSystemControlCenter', 'Flash-Firefox',
           'Alice2Textbook', 'MySQLJDBC', 'WindowsServer2003ResourceKitTools',
           'GPrologMinGW', 'Ghostscript', 'LyX', 'SketchUp',
           'Synergy2-64', 'PHP5ThreadSafe', 'CamStudioCodec',
           'VirtualBox', 'AdobeReader', 'Flash-InternetExplorer',
           'PHP5NonThreadSafe', 'TortoiseHG-64', 'Skype',
           'SDL-64', 'Iview', 'StrawberryPerl-64', 'SDL',
           'rwhod', 'MicrosoftRoboticsStudio', 'Clisp',
           'Paint.Net', 'Boost', 'EMPTY', 'TexnicCenter',
           'VLC', 'Putty', 'PdfCreator', 'LibreOffice',
           'Ruby', 'Python3', 'Python2', 'Unity3d', 'Doxygen',
           'Thunderbird', 'Love2d', 'StrawberryPerl', 'CMake',
           'Alice2', 'Alice3', 'Eric', 'Inkscape', 'Gimp',
           'ImageMagick', 'MyPaint', 'Jarnal', 'Emacs', 'Windif',
           'Hugs', 'WinSCP', 'KinectSDK', 'LuaForWindows',
           'AviSynth', 'ArgoUML', 'Squeak', 'ODE', 'ScreenRecorder',
           'SMPlayer', 'MysqlODBC', 'Scribus', 'TrueCrypt', 'Audacity',
           'R', 'VioletUML', 'Firefox', 'HaskellPlatform', 'ActiveTcl',
           'GPrologMSVC64', 'Graphviz', 'KinectToolkit', 'CamStudio',
           'MySQLWorkbench', 'DIA', 'MysqlODBC-64',
           'LeagueOfLegends', 'Povray', 'MyPaint-64', 'SQLiteDatabaseBrowser',
           'XEmacs', 'UMLet', 'SMLNJ', 'Povray-64', 'Uncrustify', 'Spin',
           'InteractiveC', 'Groovy', 'TortoiseGit-64', 'LeJOS', 'Love2d-64',
           'GVim', 'GPrologMinGW64', 'VirtualDub', '7-Zip', 'Wings3D', 'DXSDK',
           'Blender-64', 'Tightvncviewer', 'Netbeans', 'Scratch', 'ViProlog',
           'SysinternalsSuite', 'UnrealDevelopmentKit', 'Inform7', 'Racket',
           'NASM', 'SmartGit', 'Blender']

broken_localversion_minimal_list = [ 'Gimp', 'AdobeReader' ]
broken_download_minimal_list = [ 'Inkscape', 'TrueCrypt', 'AdobeReader','Flash-InternetExplorer,OracleInstantBasic']
broken_silent_minimal_list = [ 'GSview 32bit', 'AdobeReader' ]


#### TODO major is add valsearchregex to all 
catalog={
    'EMPTY':{
        name:'',
        category:'',
        description:'',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'',
            regex:'',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	
    'Console':{
        name:'Console',
        category:'Programming',
        description:'Windows console window enhancement',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/console/',
        version:{
            url:'http://sourceforge.net/projects/console/files/',
            regex:'>Download Console-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://iweb.dl.sourceforge.net/project/console/console-devel/##VERSION##/Console-##VERSION##b148-Beta_32bit.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works --cc	
    'Mozart':{
        name:'Mozart',
        category:'Programming',
        description:'Mozart implements Oz, a concurrent object-oriented language with dataflow synchronization',
        emulateuseragent:'True',
        url:'http://www.mozart-oz.org/',
        version:{
            url:'http://www.mozart-oz.org/',
            regex:'Last released Mozart is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.mozart-oz.org/download/view.cgi?action=windows&version=##VERSION##',
            regex:'a href=\'(.*[0-9]+(?:\.[0-9]+)+.*.exe)',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Mozart_is1',
            value:'DisplayName',
            regex:'Mozart ([0-9]+(?:\.[0-9]+)+)', 
            regexpos:0
            }
        },
    'Bison':{
        name:'Bison for Windows',
        category:'Programming',
        description:'General purpose parser generator. Converts a grammar description into a C program to parse the grammar.',
        emulateuseragent:'True',
        url:'http://gnuwin32.sourceforge.net/packages/bison.htm',
        version:{
            url:'http://gnuwin32.sourceforge.net/packages/bison.htm',
            regex:'<p>([0-9]+(?:\.[0-9]+)+)</p>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-sea2.dl.sourceforge.net/project/gnuwin32/bison/##VERSION##/bison-##VERSION##-bin.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Bison',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'LLVM':{
        name:'Low Level Virtual Machine',
        category:'Programming',
        description:'collection of modular and reusable compiler and toolchain technologies',
        emulateuseragent:'True',
        url:'http://llvm.org/',
        version:{
            url:'http://llvm.org/',
            regex:'LLVM ([0-9]+(?:\.[0-9]+)+) is now <a href="releases',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://llvm.org/releases/##VERSION##/clang+llvm-##VERSION##-i386-mingw32-EXPERIMENTAL.tar.bz2',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works --cc	
    'ImgBurn':{
        name:'ImgBurn',
        category:'Multimedia',
        description:'allows the recording of many types of CD/DVD images to recordable media',
        emulateuseragent:'True',
        url:'http://www.imgburn.com/index.php?act=download',
        version:{
            url:'http://www.imgburn.com/index.php?act=download',
            regex:'Current version: ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.imgburn.com/SetupImgBurn_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ImgBurn',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works --cc	
    'GPG4Win':{
        name:'GPG4Win',
        category:'Encryption',
        description:'installation package with software tools and manuals for email and file encryption',
        emulateuseragent:'True',
        url:'http://www.gpg4win.org/index.html',
        version:{
            url:'http://www.gpg4win.org/index.html',
            regex:'Download<br />Gpg4win ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://files.gpg4win.org/gpg4win-##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\GPG4Win',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Cygwin':{
        name:'Cygwin',
        category:'',
        description:'collection of tools which provide a Linux look and feel environment for Windows',
        emulateuseragent:'True',
        url:'http://cygwin.com/',
        version:{
            url:'http://cygwin.com/',
            regex:'[0-9]+(?:\.[0-9]+)+-[0-9]', 
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://cygwin.com/',
            regex:'http://cygwin.com/setup.exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MinGW':{
        name:'Minimalist GNU for Windows',
        category:'Programming',
        description:'Minimalist development environment for native Microsoft Windows applications.',
        url:'http://www.mingw.org/',
        version:{
            url:'http://sourceforge.net/projects/mingw/',
            regex:'mingw-get-inst-([0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/mingw/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'TortoiseSVN-64':{
        name:'TortoiseSVN-64',
        category:'Version Controle',
        description:'Subversion client implemented as a Microsoft Windows shell extension',
        url:'http://tortoisesvn.net/downloads.html',
        version:{
            url:'http://tortoisesvn.net/downloads.html',
            regex:'current version is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://tortoisesvn.net/downloads.html',
            regex:'a \"href=\'(.*) title =\"TortoiseSVN ##VERSION## - 64-bit',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'TortoiseSVN',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'TortoiseSVN':{
        name:'TortoiseSVN',
        category:'Version Controle',
        description:'Subversion client implemented as a Microsoft Windows shell extension',
        url:'http://tortoisesvn.net/downloads.html',
        version:{
            url:'http://tortoisesvn.net/downloads.html',
            regex:'current version is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-sea2.dl.sourceforge.net/project/tortoisesvn/1.7.9/Application/TortoiseSVN-1.7.9.23248-win32-svn-1.7.6.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'TortoiseSVN',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'FLTK':{
        name:'Fast Light Tool Kit',
        category:'Programming',
        description:'provides modern GUI functionality without the bloat and supports 3D graphics via OpenGL',
        emulateuseragent:'True',
        url:'http://www.fltk.org/',
        version:{
            url:'http://www.fltk.org/',
            regex:'VERSION=([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://ftp.easysw.com/pub/fltk/##VERSION##/fltk-##VERSION##-docs-html.tar.gz',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#local version works	
	'VTK':{
        name:'Visualization Toolkit ',
        category:'Programming',
        description:'software system for 3D computer graphics, image processing and visualization',
        emulateuseragent:'True',
        url:'http://www.vtk.org/',
        version:{
            url:'http://www.vtk.org/VTK/resources/software.html',
            regex:'Download the latest release \(([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.vtk.org/VTK/resources/software.html#latest',
            regex:'http://www.vtk.org/files/release/[0-9]+(?:\.[0-9]+)+/vtk-[0-9]+(?:\.[0-9]+)+-win32-x86.exe',
	    regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\VTK',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion does not work	--Camille
    'Lazarus':{
        name:'Lazarus',
        category:'Editor',
        description:'Lazarus IDE is a stable and feature rich visual programming environment for the FreePascal Compiler',
        url:'http://www.lazarus.freepascal.org/',
        version:{
            url:'http://sourceforge.net/projects/lazarus/files/',
            regex:'Download lazarus-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/lazarus/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Lazarus_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'GHC':{
        name:'Glasgow Haskell compiler',
        category:'Programming',
        description:'Cross-platform environment for the writing and testing of Haskell code',
        emulateuseragent:'True',
        url:'http://www.haskell.org/ghc/download',
        version:{
            url:'http://www.haskell.org/ghc/download',
            regex:'Current Stable Release \(([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.haskell.org/ghc/dist/##VERSION##/ghc-##VERSION##-i386-windows.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'Unicon':{
        name:'Unicon',
        category:'Programming',
        description:'Unified exteded dialect of Icon',
        emulateuseragent:'True',
        url:'http://unicon.sourceforge.net/index.html',
        version:{
            url:'http://sourceforge.net/projects/unicon/files/',
            regex:'setup-unicon_([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://iweb.dl.sourceforge.net/project/unicon/setup-unicon_12.1.0_threads%2832-bit%29.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'Scala':{
        name:'Scala',
        category:'Programming',
        description:'Scala is a general purpose programming language.',
        emulateuseragent:'True',
        url:'http://www.scala-lang.org/',
        version:{
            url:'http://www.scala-lang.org/downloads/',
            regex:'The current version of Scala is <strong>([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.scala-lang.org/downloads/distrib/files/scala-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'GLUT':{
        name:'GLUT OpenGL Utility Toolkit ',
        category:'Utility',
        description:'A window system independent toolkit for writing OpenGL programs',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'http://www.opengl.org/resources/libraries/glut/',
            regex:'The current source code distribution is GLUT ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.opengl.org/resources/libraries/glut/glut##DOTLESSVERSION##data.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'SciLab-64':{
        name:'SciLab',
        category:'Utility',
        description:'Free Open Source Software for Numerical Computation',
        emulateuseragent:'True',
        url:'http://www.scilab.org/products/scilab/download',
        version:{
            url:'http://www.scilab.org/products/scilab/download',
            regex:'Latest stable release: Scilab ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.scilab.org/download/##VERSION##/scilab-##VERSION##_x64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'Maxima':{
        name:'Maxima',
        category:'Utility',
        description:'Computer algebra system',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/maxima/files/',
        version:{
            url:'http://sourceforge.net/projects/maxima/files/',
            regex:'title="/Maxima-Windows/([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-dca3.dl.sourceforge.net/project/maxima/Maxima-Windows/##VERSION##-Windows/maxima-##VERSION##-1.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works --Camille	
    'LibreOffice':{
        name:'LibreOffice',
        category:'Editors and Viewers',
        description:'Ffree, libre and open source personal productivity suite.',
        emulateuseragent:'True',
        url:'http://www.libreoffice.org/',
        version:{
            url:'http://www.libreoffice.org/download/',
            regex:'version ([0-9]+(?:\.[0-9]+)+), English',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.documentfoundation.org/libreoffice/stable/##VERSION##/win/x86/LibO_##VERSION##_Win_x86_install_multi.msi'},
        silentflags:'/quiet',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\LibreOffice\\LibreOffice',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
	#localversion FIXED --Camille
    'Emacs':{
        name:'Emacs',
        category:'Editors and Viewers',
        description:'GNU Emacs is an extensible, customizable text editor and more...',
        emulateuseragent:'True',
        url:'http://www.gnu.org/software/emacs/',
        version:{
            url:'http://www.gnu.org/software/emacs/',
            regex:'The current stable release is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://ftp.gnu.org/pub/gnu/emacs/windows/emacs-##VERSION##-bin-i386.zip'},
        silentflags:'/verysilent',
        installversion:{
            querytype:'filepathname',
            path:'c:\\Program Files (x86)\\',
            regex:'emacs-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
		
	#localversion works --cc	
    'Git':{
        name:'Git for Windows',
        category:'Programming Tools',
        description:'Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.',
        emulateuseragent:'True',
        url:'http://git-scm.com/',
        version:{
            url:'http://git-scm.com/download/win',
            regex:'version <strong>([0-9]+(?:\.[0-9]+)+)</strong> ',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://git-scm.com/download/win',
            regex:'a href="(.*[0-9]+(?:\.[0-9]+)+.*.exe)',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Git_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+).*',
            regexpos:0
            }
        },    
'TortoiseGit-64':{
        name:'TortoiseGit-64',
        category:'Programming Tools',
        description:'It is a port of TortoiseSVN for Git.',
        url:'http://code.google.com/p/tortoisegit/',
        version:{
            url:'http://code.google.com/p/tortoisegit/',
            regex:'<a href=\"/p/tortoisegit/wiki/Download\">([0-9]+(?:\.[0-9]+)+)<',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://code.google.com/p/tortoisegit/wiki/Download',
            regex:'url=(http://tortoisegit.googlecode.com/files/TortoiseGit-[0-9]+(?:\.[0-9]+)+-64[^"]*)"',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'TortoiseGit',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'NASM':{
        name:'NASM',
        category:'Programming tool',
        description:'an assembler and disassembler for the Intel x86 architecture.',
        emulateuseragent:'True',
        url:'http://www.nasm.us/',
        version:{
            url:'http://www.nasm.us/',
            regex:'releasebuilds/([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.nasm.us/pub/nasm/releasebuilds/##VERSION##/win32/nasm-##VERSION##-installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Jarnal':{
        name:'Jarnal',
        category:'Editor',
        description:'Open-source cross-platform notetaking and sketching application similar to Windows Journal',
        emulateuseragent:'True',
        url:'http://jarnal.wikispaces.com/Downloads',
        version:{
            url:'http://jarnal.wikispaces.com/Downloads',
            regex:'current version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://levine.sscnet.ucla.edu/general/software/tc1000/jarnal-public.jar',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'DIA':{
        name:'Dia Diagram Editor',
        category:'Editor',
        description:'',
        emulateuseragent:'True',
        url:'Dia is a program to draw structured diagrams',
        version:{
            url:'http://dia-installer.de/',
            regex:'win32-installer/([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-dca3.dl.sourceforge.net/project/dia-installer/dia-win32-installer/##VERSION##/dia-setup-##VERSION##-2-unsigned.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Paint.Net':{
        name:'Paint.Net-64',
        category:'Editor',
        description:'Proprietary freeware raster graphics editor',
        emulateuseragent:'True',
        url:'http://www.getpaint.net/download.html',
        version:{
            url:'http://www.getpaint.net/download.html',
            regex:'size="2"><strong>([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.dotpdn.com/files/Paint.NET.##VERSION##.Install.zip',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Paint.NET',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'PdfCreator':{
        name:'PdfCreator',
        category:'ulility',
        description:'convert documents to pdf',
        emulateuseragent:'True',
        url:'http://www.pdfforge.org/',
        version:{
            url:'http://www.pdfforge.org/pdfcreator',
            regex:'Download PDFCreator ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://yellow.download.pdfforge.org/pdfcreator/##VERSION##/PDFCreator-##UNDERSCOREVERSION##_setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'PDFCreator',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#this is a duplicate?  Camille	
    'LibreOffice':{
        name:'LibreOffice',
        category:'Editors and Viewers',
        description:'Ffree, libre and open source personal productivity suite.',
        emulateuseragent:'True',
        url:'http://www.libreoffice.org/',
        version:{
            url:'http://www.libreoffice.org/download/',
            regex:'version ([0-9]+(?:\.[0-9]+)+), English',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.documentfoundation.org/libreoffice/stable/##VERSION##/win/x86/LibO_##VERSION##_Win_x86_install_multi.msi'},
        silentflags:'/quiet',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\LibreOffice\\LibreOffice',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
	#registry key or value could not be found.  Possibly in programfiles? 	
    'Tightvncviewer':{
        name:'TightVNCViewer',
        category:'Internet Tools',
        description:'TightVNC is a free remote control software package.',
        emulateuseragent:'True',
        url:'http://www.tightvnc.com/',
        version:{
            url:'http://www.tightvnc.com/download.html',
            regex:'Download TightVNC Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.tightvnc.com/download/##VERSION##/tightvnc-##VERSION##-setup-64bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/quiet',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\TightVNC',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
		'Tightvncviewer-64':{
        name:'TightVNCViewer',
        category:'Internet Tools',
        description:'TightVNC is a free remote control software package.',
        emulateuseragent:'True',
        url:'http://www.tightvnc.com/',
        version:{
            url:'http://www.tightvnc.com/download.html',
            regex:'Download TightVNC Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.tightvnc.com/download/##VERSION##/tightvnc-##VERSION##-setup-64bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/quiet',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\TightVNC',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
 
    'AdobeReader':{
        name:'AdobeReader',
        category:'Editors and Viewers',
        description:'PDF viewer',
        emulateuseragent:'True',
        url:'http://get.adobe.com/reader/',
        version:{
            url:'http://get.adobe.com/reader/',
            regex:'<span id="clientversion">...\(([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl', #not implemented yet
            #enterprise URL can not be shared but may be substituted below
            url:'http://aihdownload.adobe.com/bin/live/install_reader10_en_mssd_aih.exe',
            },
        silentflags:'',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\Adobe\\Acrobat Reader',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works	
    'Scribus':{
        name:'Scribus',
        category:'Editors and Viewers',
        description:'Opensource Page Layout',
        emulateuseragent:'True',
        url:'http://www.scribus.net/',
        version:{
            url:'http://sourceforge.net/projects/scribus/',
            regex:'scribus-([0-9]+(?:\.[0-9])+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/scribus/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            regex:'Scribus ([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
    #localversion works-cc
    'Inkscape':{
        name:'Inkscape',
        category:'Multimedia',
        description:'Opensource Vector Graphics Editor',
        emulateuseragent:'True',
        url:'http://inkscape.org/',
        version:{
            url:'http://inkscape.org/download/',
            regex:'Stable release <b>([0-9]+(?:\.[0-9]+)+)</b>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/inkscape/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regval',
            key:'HKLM',           
		   subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Inkscape',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Gimp':{
        name:'Gimp-64',
        category:'Multimedia',
        description:'GNU Image Manipulation Program.',
        emulateuseragent:'True',
        url:'http://www.gimp.org/',
        version:{
            url:'http://www.gimp.org/downloads/',
            regex:'Download GIMP ([0-9]+(?:\.[0-9]+)+)',
            regexpos:1},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/gimp-win/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch', 
            key:'HKLM',
	    valsearchregex: 'GIMP',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
		
    'TrueCrypt':{
        name:'TrueCrypt',
        category:'Encryption',
        description:'Virtual disk encryption',
        emulateuseragent:'True',
        url:'http://www.truecrypt.org/',
        version:{
            url:'http://www.truecrypt.org/downloads',
            regex:'Latest Stable Version - ([0-9]+(?:\.[0-9]+)+[a-zA-Z]?)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.truecrypt.org/download/transient/066a18c825/TrueCrypt%20Setup%20##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\TrueCrypt',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+[a-zA-Z]?)',
            regexpos:0
            }
        },
    #Debug: local version does not work--Camille
	'ImageMagick':{
        name:'ImageMagick',
        category:'Multimedia',
        description:'A software suite to create, edit, compose, or convert bitmap images.',
        emulateuseragent:'True',
        url:'http://www.imagemagick.org',
        version:{
            url:'http://www.imagemagick.org/script/binary-releases.php',
            regex:'ImageMagick-([0-9]+(?:[\.\-][0-9A-Z]+)+)-windows-dll.exe',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.imagemagick.org/download/binaries/ImageMagick-##VERSION##-windows-dll.exe',
            regex:'',
            regexpos:0},
        silentflags:'/VERYSILENT',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\ImageMagick\\Current',
            value:'Version',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion okay --cc	
    'GSview32bit':{
        name:'GSview 32bit',
        category:'Utilities',
        description:'GSview is a graphical interface for Ghostscript',
        emulateuseragent:'True',
        url:'http://pages.cs.wisc.edu/~ghost/gsview/index.htm',
        version:{
            url:'http://pages.cs.wisc.edu/~ghost/gsview/index.htm',
            regex:'>Obtaining GSview ([0-9]+(?:\.[0-9]+)+)<',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://pages.cs.wisc.edu/~ghost/gsview/download/gsv##DOTLESSVERSION##w32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/auto',
        installversion:{
            querytype:'regvalname',
            key:'HKLM',
            subkey:'SOFTWARE\\Ghostgum\\GSView',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion okay --cc	
    'Ghostscript':{
        name:'Ghostscript',
        category:'Utilities',
        description:'An interpreter for the PostScript language and for PDF.',
        emulateuseragent:'True',
        url:'http://www.ghostscript.com/',
        version:{
            url:'http://www.ghostscript.com/download/',
            regex:'<a href="gsdnld.html">Ghostscript ([0-9]+(?:\.[0-9]+)+)</a>',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.ghostscript.com/download/gsdnld.html',
            regex:'<a href="(http://downloads\.ghostscript\.com/public/gs[0-9]+w32\.exe)">',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\GPL Ghostscript',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
    '7-Zip':{
        name:'7-Zip-64',
        category:'Utilities',
        description:'Multiple format file compression and decompression',
        emulateuseragent:'True',
        url:'http://7-zip.org',
        version:{
            url:'http://7-zip.org',
            regex:'<P><B>Download 7-Zip ([0-9]+(?:\.[0-9]+)+) \(',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/sevenzip/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: '7-Zip',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Firefox':{
        name:'Firefox',
        category:'Internet Tools',
        description:'The Mozilla Firefox browser',
        emulateuseragent:'True',
        url:'http://www.mozilla.org/en-US/firefox/new/',
        version:{
            url:'http://www.mozilla.org/en-US/firefox/new/',
            regex:'([0-9]+(?:\.[0-9]+)+) for Windows',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.cdn.mozilla.net/pub/mozilla.org/firefox/releases/##VERSION##/win32/en-US/Firefox%20Setup%20##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'-ms',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Mozilla\\Mozilla Firefox',
            value:'CurrentVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
     'Notepad++':{ 
        name:'Notepad++',
        category:'Multimedia',
        description:'An Editor that knows about \\n',
        emulateuseragent:'True',
        url:'http://notepad-plus-plus.org/',
        version:{
            url:'http://notepad-plus-plus.org/download/',
            regex:'v([0-9]+(?:\.[0-9]+)*)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.tuxfamily.org/notepadplus/##VERSION##/npp.##VERSION##.Installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'-ms',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Notepad++',
            value:'CurrentVersion', 
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GVim':{
        name:'GNU Vim',
        category:'Editors',
        description:'Vi Improved Editing Environment',
        emulateuseragent:'True',
        url:'http://www.vim.org',
        version:{
            url:'http://www.vim.org/download.php',
            regex:'gvim([0-9]+_[0-9]+).exe',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'ftp://ftp.vim.org/pub/vim/pc/gvim##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        }, 
	#localversion okay --cc	
   'Flash-Firefox':{
        name:'Adobe Flash Player (Firefox)',
        category:'Multimedia',
        description:'Web Plugin Framework for Firefox',
        emulateuseragent:'True',
        url:'http://www.adobe.com/products/flashplayer.html ',
        version:{
            url:'http://get.adobe.com/flashplayer/',
            regex:'<span id="clientversion">([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://aihdownload.adobe.com/bin/live/install_flashplayer11x32_mssd_aih.exe'},
        silentflags:'/verysilent',
        installversion:{    
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Adobe Flash Player Plugin',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
	#localversion works --camille	
    'Pidgin':{
        name:'Pidgin',
        category:'Internet tool',
        description:'Universal chat program ',
        emulateuseragent:'True',
        url:'http://pidgin.im/',
        version:{
            url:'http://pidgin.im/',
            regex:'<span class="number">([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://voxel.dl.sourceforge.net/project/pidgin/Pidgin/##VERSION##/pidgin-##VERSION##.exe'},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Pidgin',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
		#localversion works --camille	
    'Flash-InternetExplorer':{
        name:'Adobe Flash Player (IE)',
        category:'Multimedia',
        description:'Virus Plugin Framework for IE',
        emulateuseragent:'True',
        url:'http://www.adobe.com/products/flashplayer.html ',
        version:{
            url:'http://get.adobe.com/flashplayer/',
            regex:'<span id="clientversion">([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://aihdownload.adobe.com/bin/live/install_flashplayer11x32ax_mssd_aih.exe'},
        silentflags:'/verysilent',
        installversion:{    
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Adobe Flash Player Plugin',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Thunderbird':{
        name:'Thunderbird',
        category:'Internet Tools',
        description:'Bayes Classifier Spam Detector',
        emulateuseragent:'True',
        url:'http://www.mozilla.org/en-US/thunderbird/',
        version:{
            url:'http://www.mozilla.org/en-US/thunderbird/15.0.1/releasenotes/',
            regex:'v\.([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.cdn.mozilla.net/pub/mozilla.org/thunderbird/releases/##VERSION##/win32/en-US/Thunderbird%20Setup%20##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Mozilla Thunderbird',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VirtualBox':{
        name:'VirtualBox-64',
        category:'Virtual Machine',
        description:'x86 and AMD64/Intel64 virtualization product',
        emulateuseragent:'True',
        url:'https://www.virtualbox.org/',
        version:{
            url:'https://www.virtualbox.org/wiki/Downloads',
            regex:'VirtualBox ([0-9]+(?:\.[0-9]+)+) for Windows',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'https://www.virtualbox.org/wiki/Downloads',
            regex:'(http://download.virtualbox.org/virtualbox/[0-9]+(?:\.[0-9]+)+/VirtualBox-[0-9]+(?:[\.\-][0-9]+)+-Win.exe)',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex:'Oracle VM VirtualBox',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Python2':{
        name:'Python 2',
        category:'Programming',
        description:'T3h l337t3st Programming Language Yo',
        emulateuseragent:'True',
        url:'python.org',
        version:{
            url:'http://python.org/download/',
            regex:'Python (2(?:\.[0-9]+)+)',
            regexpos:1},
        download:{
            downloadtype:'directurl',
            url:'http://python.org/ftp/python/##VERSION##/python-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayIcon',
            valsearchregex: 'Python2',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Python3':{
        name:'Python 3',
        category:'Programming',
        description:'If you are into that New Age Stuff',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'http://python.org/download/',
            regex:'Python (3(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://python.org/ftp/python/##VERSION##/python-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayIcon',
            valsearchregex: 'Python3',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SmartGit':{
        name:'SmartGit',
        category:'Source Control Management',
        description:'The Smart way to git',
        emulateuseragent:'True',
        url:'http://www.syntevo.com/smartgit/index.html',
        version:{
            url:'http://www.syntevo.com/smartgit/index.html',
            regex:'Version:  <span>([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.syntevo.com/download/smartgit/smartgit-win32-setup-jre-##UNDERSCOREVERSION##.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'rwhod':{
        name:'Windows R Who Daemon',
        category:'Utilities',
        description:'Answers linux rwho requests for finding people on your network',
        emulateuseragent:'True',
        url:'http://matthew.loar.name/software/rwho/',
        version:{
            url:'http://matthew.loar.name/software/rwho/',
            regex:'([0-9]+(?:\.[0-9]+)+)</td>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://matthew.loar.name/software/archives/rwho/##VERSION##/rwho.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'rwho',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'ScreenRecorder':{
        name:'Screen Recorder-64',
        category:'Utilities',
        description:'For Recording Screens',
        emulateuseragent:'True',
        url:'http://technet.microsoft.com/en-us/magazine/2009.03.utilityspotlight2.aspx?pr=blog',
        version:{
            url:'http://technet.microsoft.com/en-us/magazine/2009.03.utilityspotlight2.aspx?pr=blog',
            regex:'UtilityOnline((?:'+months+')[0-9]+_[0-9]+)',
            regexpos:1},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/f/d/0/fd05def7-68a1-4f71-8546-25c359cc0842/UtilityOnlineMarch092009_03.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'ScreenRecorder',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SysinternalsSuite':{
        name:'Sysinternals Suite',
        category:'Utilities',
        description:'Collection of Mark Russinovich system utilities',
        emulateuseragent:'True',
        url:'http://technet.microsoft.com/en-us/sysinternals',
        version:{
            url:'http://technet.microsoft.com/en-us/sysinternals/bb842062',
            regex:'<p>Updated: ((?:'+months+') [0-9]+, [0-9]+)</p>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.sysinternals.com/files/SysinternalsSuite.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'CamStudioCodec':{
        name:'CamStudio Video Codec',
        category:'Multimedia',
        description:'The Codec for Camstudio',
        emulateuseragent:'True',
        url:'http://camstudio.org/',
        version:{
            url:'http://camstudio.org/',
            regex:'Lossless Video Codec v([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://voxel.dl.sourceforge.net/project/camstudio/legacy/CamStudioCodec-##VERSION##-w32.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Putty':{
        name:'Putty',
        category:'Utilties',
        description:'Windows SSH and telenet client',
        emulateuseragent:'True',
        url:'http://www.chiark.greenend.org.uk/~sgtatham/putty/',
        version:{
            url:'http://www.chiark.greenend.org.uk/~sgtatham/putty/',
            regex:'The latest version is ((?:'+alphabeta+') [0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://the.earth.li/~sgtatham/putty/latest/x86/putty-##VERSION##-installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',  
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\PuTTY_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }   
        },
    'WinSCP':{
        name:'WinSCP',
        category:'Utilties',
        description:'Secure Copy for Windows',
        emulateuseragent:'True',
        url:'http://winscp.net/eng/index.php',
        version:{
            url:'http://winscp.net/eng/download.php',
            regex:'WinSCP ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.winscp.net/download/files/201209172139457d6cc5704256b399748a581c926f20/winscp439setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'WindowsSystemControlCenter':{
        name:'Windows System Control Center',
        category:'Utilities ',
        description:'Utility Organizer',
        emulateuseragent:'True',
        url:'http://www.kls-soft.com/wscc/index.php',
        version:{
            url:'http://www.kls-soft.com/wscc/index.php',
            regex:'Latest version:</font></strong> ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.kls-soft.com/downloads/wscc.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VioletUML':{
        name:'Violet UML Editor',
        category:'Programming',
        description:'A UML editor with nice benefits',
        emulateuseragent:'True',
        url:'http://alexdp.free.fr/violetumleditor/page.php',
        version:{
            url:'http://sourceforge.net/projects/violet/',
            regex:'com.horstmann.violet-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/violet/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Racket':{
        name:'Racket',
        category:'Programming',
        description:'A Lisp',
        emulateuseragent:'True',
        url:'http://racket-lang.org/',
        version:{
            url:'http://racket-lang.org/download/',
            regex:'Download Racket v([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.racket-lang.org/installers/##VERSION##/racket/racket-##VERSION##-bin-i386-win32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Netbeans':{
        name:'Netbeans',
        category:'Programming',
        description:'Java IDE',
        emulateuseragent:'True',
        url:'netbeans.org',
        version:{
            url:'http://netbeans.org/community/releases',
            regex:'Release ([0-9]+(?:\.[0-9]+)) <',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.netbeans.org/netbeans/##VERSION##/final/bundles/netbeans-##VERSION##-ml-javase-windows.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MySQLJDBC':{
        name:'MySQLJDBC',
        category:'Database',
        description:'Java Database Connector for Mysql',
        emulateuseragent:'True',
        url:'http://www.mysql.com/downloads/connector/j/?product=c-j',
        version:{   
            url:'http://www.mysql.com/downloads/connector/j/?product=c-j',
            regex:'Connector/J ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.mysql.com/get/Downloads/Connector-J/mysql-connector-java-##VERSION##.tar.gz/from/http://cdn.mysql.com/',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MySQLWorkbench':{
        name:'MySQL Workbench',
        category:'Database',
        description:'GUI Mysql editor',
        emulateuseragent:'True',
        url:'http://www.mysql.com/products/workbench/',
        version:{
            url:'http://dev.mysql.com/downloads/workbench/',
            regex:'MySQL Workbench ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-gpl-##VERSION##-win32.msi/from/http://cdn.mysql.com/',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'MySQL Workbench',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Squeak':{
        name:'Squeak',
        category:'http://www.squeak.org ',
        description:'',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'http://www.squeakvm.org/win32/',
            regex:'SqueakVM-Win32-([0-9]+(?:\.[0-9]+)+)-bin.zip</a>. ',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.squeakvm.org/win32/release/SqueakVM-Win32-##VERSION##-bin.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'LyX':{
        name:'Lyx',
        category:'Editor',
        description:'Latex Editor',
        emulateuseragent:'True',
        url:'http://wiki.lyx.org/LyX/Welcome',
        version:{
            url:'http://wiki.lyx.org/Windows/Windows',
            regex:'Current stable version: ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://wiki.lyx.org/Windows/Windows',
            regex:'(ftp://ftp.lyx.org/pub/lyx/bin/[0-9]+(?:\.[0-9]+)+/LyX-[0-9]+(?:[\.\-][0-9]+)+-Installer.exe)',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\LyX',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'R':{
        name:'R',
        category:'Programming',
        description:'Statistical and Graphical Computing',
        emulateuseragent:'True',
        url:'http://cran.cs.wwu.edu/',
        version:{
            url:'http://www.r-project.org/main.shtml',
            regex:'R version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://cran.cs.wwu.edu/bin/windows/base/R-##VERSION##-win.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Clisp':{
        name:'Clisp',
        category:'Programming',
        description:'A GNU ANSI C Common Lisp',
        emulateuseragent:'True',
        url:'http://www.clisp.org/',
        version:{
            url:'http://sourceforge.net/projects/clisp/',
            regex:'clisp\-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/clisp/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'PHP5NonThreadSafe':{
        name:'PHP',
        category:'Programming',
        description:'A Great! Programming Language',
        emulateuseragent:'True',
        url:'http://windows.php.net',
        version:{
            url:'http://windows.php.net/download/',
            regex:'PHP 5.4 \\(([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://windows.php.net/downloads/releases/php-##VERSION##-nts-Win32-VC9-x86.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'PHP5ThreadSafe':{
        name:'PHP',
        category:'Programming',
        description:'A Great! Programming Language',
        emulateuseragent:'True',
        url:'http://windows.php.net',
        version:{
            url:'http://windows.php.net/download/',
            regex:'PHP 5.4 \\(([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://windows.php.net/downloads/releases/php-##VERSION##-Win32-VC9-x86.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SMLNJ':{
        name:'Standard ML New Jersey',
        category:'Programming',
        description:'A non Lazy Functional Programming Language',
        emulateuseragent:'True',
        url:'http://www.smlnj.org/',
        version:{
            url:'http://www.smlnj.org/dist/working/index.html',
            regex:'<b>([0-9]+(?:\.[0-9]+)+)</b>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://smlnj.cs.uchicago.edu/dist/working/##VERSION##/smlnj.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
   'GPrologMinGW':{
        name:'GNU Prolog (Microsoft Visual C Compiler)',
        category:'Programming',
        description:'GNU implementation of the declarative language Prolog',
        emulateuseragent:'True',
        url:'http://www.gprolog.org',
        version:{
            url:'http://www.gprolog.org/#download',
            regex:'gprolog\-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.gprolog.org/setup-gprolog-##VERSION##-msvc-x86.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\GNU Prolog_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GPrologMinGW':{
        name:'GNU Prolog (MinGW Compiler)',
        category:'Programming',
        description:'GNU implementation of the declarative language Prolog',
        emulateuseragent:'True',
        url:'http://www.gprolog.org',
        version:{
            url:'http://www.gprolog.org/#download',
            regex:'gprolog\-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.gprolog.org/setup-gprolog-##VERSION##-mingw-x86.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\GNU Prolog_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GPrologMSVC64':{
        name:'GNU Prolog (MSCV Compiler) 64 bit',
        category:'Programming',
        description:'GNU implementation of the declarative language Prolog',
        emulateuseragent:'True',
        url:'http://www.gprolog.org',
        version:{
            url:'http://www.gprolog.org/#download',
            regex:'gprolog\-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.gprolog.org/setup-gprolog-##VERSION##-msvc-x64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\GNU Prolog_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GPrologMinGW64':{
        name:'GNU Prolog (MinGW Compiler) 64 bit',
        category:'Programming',
        description:'GNU implementation of the declarative language Prolog',
        emulateuseragent:'True',
        url:'http://www.gprolog.org',
        version:{
            url:'http://www.gprolog.org/#download',
            regex:'gprolog\-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.gprolog.org/setup-gprolog-##VERSION##-mingw-x64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\GNU Prolog_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Groovy':{
        name:'Groovy',
        category:'Programming',
        description:'Dynamic Langauge for the JRE',
        emulateuseragent:'True',
        url:'http://groovy.codehaus.org/',
        version:{
            url:'http://groovy.codehaus.org/Download',
            regex:'Groovy ([0-9]+(?:\.[0-9]+)+)',
            regexpos:2},
        download:{
            downloadtype:'directurl',
            url:'http://dist.groovy.codehaus.org/distributions/groovy-binary-##VERSION##.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'LuaForWindows':{
        name:'Lua For Windows',
        category:'Programming',
        description:'Installation of Lua for the Windows OS including many lua libraries',
        emulateuseragent:'True',
        url:'http://code.google.com/p/luaforwindows/',
        version:{
            url:'http://code.google.com/p/luaforwindows/',
            regex:'Download Lua_V([0-9]+(?:[-|.][0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://luaforwindows.googlecode.com/files/LuaForWindows_v##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Lua_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Wings3D':{
        name:'Wings 3D',
        category:'Multimedia',
        description:'Wings 3D is an advanced subdivision modeler that is both powerful and easy to use',
        emulateuseragent:'True',
        url:'http://www.wings3d.com/index.php',
        version:{
            url:'http://www.wings3d.com/index.php',
            regex:'Wings 3D Stable ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-dca3.dl.sourceforge.net/project/wings/wings/##VERSION##/wings-##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Synergy2':{
        name:'Synergy 2',
        category:'Utility',
        description:'Screen Sharing Utility',
        emulateuseragent:'True',
        url:'http://synergy-foss.org/',
        version:{
            url:'http://synergy-foss.org/download/?list',
            regex:'Latest release:</b> ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://synergy.googlecode.com/files/synergy-##VERSION##-Windows-x86.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Synergy',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Synergy2-64':{
        name:'Synergy 2',
        category:'Utility',
        description:'Screen Sharing Utility',
        emulateuseragent:'True',
        url:'http://synergy-foss.org/',
        version:{
            url:'http://synergy-foss.org/download/?list',
            regex:'Latest release:</b> ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://synergy.googlecode.com/files/synergy-##VERSION##-Windows-x64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Synergy',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Doxygen':{
        name:'Doxygen',
        category:'Programming',
        description:'Generate documentation from source code',
        emulateuseragent:'True',
        url:'http://www.stack.nl/~dimitri/doxygen/',
        version:{
            url:'http://www.stack.nl/~dimitri/doxygen/download.html',
            regex:'doxygen\-([0-9]+(?:\.[0-9]+)+)\-setup.exe',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://ftp.stack.nl/pub/users/dimitri/doxygen-##VERSION##-setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\doxygen_is1',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Graphviz':{
        name:'Graphviz',
        category:'Utility',
        description:'Graph and Digraph layout engine',
        emulateuseragent:'True',
        url:'http://www.graphviz.org',
        version:{
            url:'http://www.graphviz.org/Download_windows.php',
            regex:'graphviz-([0-9]+(?:\.[0-9]+)+).msi',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'LeJOS':{
        name:'LeJOS',
        category:'Firmware',
        description:'leJOS is replacement firmware for LEGO Mindstorms RCX and NXT bricks. Yes, you can program a LEGO robot with Java',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/lejos/',
        version:{
            url:'http://sourceforge.net/projects/lejos/',
            regex:'leJOS_NXJ_([0-9]+(?:\.[0-9]+)+(?:alpha|beta)(?:\-[0-9]+))',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/lejos/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
     'ODE':{
        name:'Open Dynamics Engine',
        category:'Simulation',
        description:'An open source, high performance library for simulating rigid body dynamics',
        emulateuseragent:'True',
        url:'http://www.ode.org/',
        version:{
            url:'http://sourceforge.net/projects/opende/',
            regex:'ode-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://softlayer.dl.sourceforge.net/project/opende/ODE/0.12/ode-##VERSION##.tar.bz2',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'UMLet':{
        name:'UMLet',
        category:'Utility',
        description:'Free UML Tool for fast UML diagrams',
        emulateuseragent:'True',
        url:'http://www.umlet.com/',
        version:{
            url:'http://www.umlet.com/changes.htm',
            regex:'UMLet ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.umlet.com/umlet_##UNDERSCOREVERSION##/umlet_##VERSION##.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Alice2':{
        name:'Alice',
        category:'Programming',
        description:'An educational software that teaches students computer programming in a 3D Environment',
        emulateuseragent:'True',
        url:'http://www.alice.org/',
        version:{
            url:'http://www.alice.org/index.php?page=downloads/download_alice2.3',
            regex:'Download Alice ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.alice.org/downloads/##VERSION##/Alice##VERSION##.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Alice2Textbook':{
        name:'Alice',
        category:'Programming',
        description:'Alice 3D Modeling Plus Learning to Program with Alice',
        emulateuseragent:'True',
        url:'http://www.alice.org/',
        version:{
            url:'http://www.alice.org/index.php?page=downloads/download_alice2.3',
            regex:'Download Alice ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'www.alice.org/downloads/##VERSION##/Alice##VERSION##b.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Alice3':{
        name:'Alice',
        category:'Programming',
        description:'An educational software that teaches students computer programming in a 3D Environment',
        emulateuseragent:'True',
        url:'http://www.alice.org/',
        version:{
            url:'http://www.alice.org/index.php?page=downloads/download_alice3.1    ',
            regex:'Complete-([0-9]+(?:\.[0-9]+)+)-windows.exe',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.alice.org/downloads/installers/Alice3Installer-Complete-##VERSION##-windows.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Skype':{
        name:'Skype',
        category:'Chat',
        description:'Peer to Peer Voice,Video,IM Client',
        emulateuseragent:'True',
        url:'http://www.skype.com',
        version:{
            url:'http://blogs.skype.com/garage/windows/',
            regex:'Skype ([0-9]+(?:\.[0-9]+){2,}) for Windows(?!: Phone)',
            regexpos:0
            },
        download:{
            downloadtype:'directurl',
            url:'http://download.skype.com/ce0b222b5e04303dba1df2805ab1d5ed/SkypeSetup.exe',
            regex:'',
            regexpos:0
            },
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Skype',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SketchUp':{
        name:'SketchUp',
        category:'Modeling',
        description:'Google 3d Modeling Program',
        emulateuseragent:'True',
        url:'http://www.sketchup.com/',
        version:{
            url:'http://www.sketchup.com/intl/en/download/gsu.html',
            regex:'Download SketchUp ([0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://dl.google.com/sketchup/SketchUpWEN.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'SketchUp',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:1
            }
        },
    'ViProlog':{
        name:'Visual Prolog',
        category:'Programming',
        description:'Prolog that Targets Windows',
        emulateuseragent:'True',
        url:'http://www.visual-prolog.com/',
        version:{
            url:'http://www.visual-prolog.com/vip6/community/news.htm',
            regex:'Build ([0-9]+) has been released',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.pdc.dk/vip/vippe/vip##VERSION##pe.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'ActiveTcl':{
        name:'ActiveTcl',
        category:'Programming',
        description:'Commerical Tcl Distribution',
        emulateuseragent:'True',
        url:'http://www.activestate.com/activetcl',
        version:{
            url:'http://www.activestate.com/activetcl/downloads',
            regex:'<p>Download ActiveTcl ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.activestate.com/activetcl/downloads',
            regex:'http://downloads.activestate.com/ActiveTcl/releases/[0-9]+(?:\.[0-9]+)+/ActiveTcl[0-9]+(?:\.[0-9]+)+-win32-ix86-threaded.exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'ActiveTcl-64':{
        name:'ActiveTcl',
        category:'Programming',
        description:'Commerical Tcl Distribution',
        emulateuseragent:'True',
        url:'http://www.activestate.com/activetcl',
        version:{
            url:'http://www.activestate.com/activetcl/downloads',
            regex:'<p>Download ActiveTcl ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.activestate.com/activetcl/downloads',
            regex:'http://downloads.activestate.com/ActiveTcl/releases/[0-9]+(?:\.[0-9]+)+/ActiveTcl[0-9]+(?:\.[0-9]+)+-win32-x86_64-threaded.exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'KinectSDK':{
        name:'Kinect SDK',
        category:'Programming',
        description:'Source Development Kit for the Microsoft Kinect',
        emulateuseragent:'True',
        url:'research.microsoft.com/en-us/um/redmond/projects/kinectsdk/',
        version:{
            url:'http://msdn.microsoft.com/en-us/library/jj663803.aspx',
            regex:'version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/0/B/C/0BC13867-7ECD-4AC8-9400-873FF267467D/KinectSDK-v##VERSION##-Setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Microsoft Kinect',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'KinectToolkit':{
        name:'Kinect for Windows Developer Toolkit',
        category:'Programming',
        description:'Contains source code samples, Kinect Studio, Face Tracking SDK, and other resources to simplify developing applications using the Kinect for Windows SDK',
        emulateuseragent:'True',
        url:'research.microsoft.com/en-us/um/redmond/projects/kinectsdk/',
        version:{
            url:'http://msdn.microsoft.com/en-us/library/jj663803.aspx',
            regex:'version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/B/B/A/BBA5742E-8E6B-4C05-ADF2-B2F076DD7741/KinectDeveloperToolkit-v##VERSION##-Setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VirtualDub':{
        name:'VirtualDub',
        category:'Utility',
        description:'Video Capture and Processing Utility',
        emulateuseragent:'True',
        url:'http://virtualdub.sourceforge.net/',
        version:{
            url:'http://sourceforge.net/projects/virtualdub/files/virtualdub-win/',
            regex:'/projects/virtualdub/files/virtualdub-win/([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/virtualdub/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MicrosoftRoboticsStudio':{
        name:'Mircosoft Robotics Studio',
        category:'Programming',
        description:'Robot Development Environment',
        emulateuseragent:'True',
        url:'http://www.microsoft.com/robotics/',
        version:{
            url:'http://www.microsoft.com/en-us/download/details.aspx?id=29081',
            regex:'<span>([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://download.microsoft.com/download/7/7/B/77B9D6DD-8601-4C9B-A5A8-BD7E1D2D115E/Microsoft%20Robotics%20Developer%20Studio%204.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MysqlODBC':{
        name:'Mysql Open  Database Connectivity',
        category:'Database',
        description:'ODBC Driver for Mysql',
        emulateuseragent:'True',
        url:'http://dev.mysql.com/downloads/connector/odbc',
        version:{
            url:'http://dev.mysql.com/downloads/connector/odbc',
            regex:'Connector/ODBC ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://cdn.mysql.com/Downloads/Connector-ODBC/5.1/mysql-connector-odbc-##VERSION##-win32.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'MysqlODBC-64':{
        name:'Mysql Open  Database Connectivity',
        category:'Database',
        description:'ODBC Driver for Mysql',
        emulateuseragent:'True',
        url:'http://dev.mysql.com/downloads/connector/odbc',
        version:{
            url:'http://dev.mysql.com/downloads/connector/odbc',
            regex:'Connector/ODBC ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://cdn.mysql.com/Downloads/Connector-ODBC/5.1/mysql-connector-odbc-##VERSION##-winx64.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'TexnicCenter':{
        name:'Texnic Center',
        category:'Editor',
        description:'Latex Editor',
        emulateuseragent:'True',
        url:'http://www.texniccenter.org/',
        version:{
            url:'http://sourceforge.net/projects/texniccenter/',
            regex:'TXCSetup_([0-9]+(?:Stable)?(?:RC[0-9]+)?)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://sourceforge.net/projects/texniccenter/files/latest/download?source=files',
            regex:'http://downloads.sourceforge.net/project/texniccenter/TeXnicCenter/.+/TXCSetup_[0-9]+(?:Stable)?(?:RC[0-9]+)?.exe[^"]*',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'DisplayVersion',
            regex:'Version ([0-9]+(?:\.[0-9]+)+) Stable RC1',
            regexpos:0
            }
        },
    'HaskellPlatform':{
        name:'The Haskell Platform',
        category:'Programming',
        description:'The Best Way To Program, Obv',
        emulateuseragent:'True',
        url:'http://hackage.haskell.org/platform/',
        version:{
            url:'http://hackage.haskell.org/platform/',
            regex:'Current release: <a href="changelog.html">([0-9]+(?:\.[0-9]+)+)</a>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://lambda.haskell.org/platform/download/##VERSION##/HaskellPlatform-##VERSION##-setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'UnrealDevelopmentKit':{
        name:'Unreal Development Kit',
        category:'Programming',
        description:'3D Game Environment',
        emulateuseragent:'True',
        url:'http://www.unrealengine.com/udk/',
        version:{
            url:'http://www.unrealengine.com/en/udk/downloads/',
            regex:"((?:"+months+ ") [0-9]{4})",
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.unrealengine.com/en/udk/downloads/',
            regex:'http://download.udk.com/UDKInstall-[0-9]+-[0-9]+-BETA[0-9].exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Unity3d':{
        name:'Unity Game Engine',
        category:'Programming',
        description:'Game Engine',
        emulateuseragent:'True',
        url:'http://unity3d.com',
        version:{
            url:'http://unity3d.com/unity/download/',
            regex:'Download Unity ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://netstorage.unity3d.com/unity/UnitySetup-##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Ruby':{
        name:'Ruby',
        category:'Programming',
        description:'A Programming Langauge that your roommate is always telling you about but you really do not care',
        emulateuseragent:'True',
        url:'http://www.ruby-lang.org',
        version:{
            url:'http://rubyinstaller.org/downloads/',
            regex:'Ruby ([0-9]+(?:\.[0-9]+)+(?:-p[0-9]+))',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://rubyinstaller.org/downloads/',
            regex:'http://rubyforge.org/frs/download.php/[0-9]+/rubyinstaller-[0-9]+(?:\.[0-9]+)+(?:-p[0-9]+).exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Uncrustify':{
        name:'Uncrustify',
        category:'Utility',
        description:'Code Beautification Utility',
        emulateuseragent:'True',
        url:'http://uncrustify.sourceforge.net/',
        version:{
            url:'http://sourceforge.net/projects/uncrustify/',
            regex:'uncrustify-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://hivelocity.dl.sourceforge.net/project/uncrustify/uncrustify/uncrustify-##VERSION##/uncrustify-##VERSION##-win32.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    
    'SQLiteDatabaseBrowser':{
        name:'SQlite Database Browser',
        category:'database',
        description:'Graphical Sqlite Editor',
        emulateuseragent:'True',
        url:'http://sqlitebrowser.sourceforge.net/',
        version:{
            url:'http://sourceforge.net/projects/sqlitebrowser/',
            regex:'sqlitebrowser_([0-9]+_[a-zA-Z]+[0-9]+)_win',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://hivelocity.dl.sourceforge.net/project/sqlitebrowser/sqlitebrowser2/.0%20beta1/sqlitebrowser_##VERSION##_win.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'CMake':{
        name:'CMake',
        category:'Programming',
        description:'Cross Platform Make',
        emulateuseragent:'True',
        url:'http://www.cmake.org/',
        version:{
            url:'http://www.cmake.org/cmake/resources/software.html',
            regex:'Latest Release \(([0-9]+(?:\.[0-9]+)+)\)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.cmake.org/cmake/resources/software.html',
            regex:'http://www.cmake.org/files/v[0-9]+(?:\.[0-9]+)+/cmake-[0-9]+(?:\.[0-9]+)+-win32-x86.exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Cmake',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'AviSynth':{
        name:'AviSynth',
        category:'Programming',
        description:'Scripting langauge for non linear video editing',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/avisynth2/',
        version:{
            url:'http://sourceforge.net/projects/avisynth2/files/',
            regex:'Avisynth_([0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://iweb.dl.sourceforge.net/project/avisynth2/AviSynth%202.5/AviSynth%202.5.8/Avisynth_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\AviSynth',
            value:'DisplayName',
            regex:'AviSynth ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Spin':{
        name:'Sping',
        category:'Programming',
        description:'Formal Verification of Distributed Software Systems',
        emulateuseragent:'True',
        url:'spinroot.com/spin/whatispin.html',
        version:{
            url:'http://spinroot.com/spin/Bin/index.html',
            regex:'Current Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://spinroot.com/spin/Bin/spin##DOTLESSVERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'XNAGameStudio':{
        name:'XNA Game Studio',
        category:'Programming',
        description:'Xbox DevelopmentE nvironment',
        emulateuseragent:'True',
        url:'http://msdn.microsoft.com/en-us/aa937791.aspx',
        version:{
            url:'http://www.microsoft.com/en-us/download/details.aspx?id=23714',
            regex:'<td class="col2"><span>([0-9]+(?:\.[0-9]+)+)</span></td>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/0/1/4/01483A18-289E-4779-BB5A-0A28DFE18BC5/XNAGS##DOTLESSVERSION##_setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Microsoft XNA Game Studio',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },    
    'Iview':{
        name:'irfanview',
        category:'Multimedia',
        description:'Graphics View',
        emulateuseragent:'True',
        url:'http://www.irfanview.com/',
        version:{
            url:'http://download.cnet.com/IrfanView/3000-2192_4-10021962.html?part=dl-IrfanView&subj=dl&tag=button',
            regex:'<dd class="version">([0-9]+(?:\.[0-9]+)+)</dd>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://software-files-a.cnet.com/s/software/12/48/66/01/iview##DOTLESSVERSION##_setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\IrfanView',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Hugs':{
        name:'Hugs',
        category:'Programming',
        description:'The best programming that hugs you',
        emulateuseragent:'True',
        url:'http://cvs.haskell.org/Hugs',
        version:{
            url:'http://cvs.haskell.org/Hugs/pages/downloading.htm',
            regex:'WinHugs-((?:'+abmonths+')[0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://ndmitchell.googlecode.com/files/WinHugs-##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'StrawberryPerl':{
        name:'Strawberry Perl',
        category:'Programming',
        description:'A programming language with a lot of operators',
        emulateuseragent:'True',
        url:'http://strawberryperl.com/',
        version:{
            url:'http://strawberryperl.com/',
            regex:'Download Strawberry Perl ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'direct',
            url:'http://strawberry-perl.googlecode.com/files/strawberry-perl-##VERSION##-32bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Strawberry Perl',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'StrawberryPerl-64':{
        name:'Strawberry Perl-64',
        category:'Programming',
        description:'A programming language with a lot of operators',
        emulateuseragent:'True',
        url:'http://strawberryperl.com/',
        version:{
            url:'http://strawberryperl.com/',
            regex:'Download Strawberry Perl ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://strawberry-perl.googlecode.com/files/strawberry-perl-##VERSION##-64bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\',
            value:'DisplayName',
            valsearchregex: 'Strawberry Perl',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
       },
    'DXSDK':{
        name:'DXSDK',
        category:'Programming',
        description:'Direct X SDK',
        emulateuseragent:'True',
        url:'http://www.microsoft.com/en-us/download/details.aspx?id=6812',
        version:{
            url:'http://www.microsoft.com/en-us/download/details.aspx?id=6812',
            regex:'<span>DXSDK_((?:'+abmonths+')[0-9]+).exe</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/A/E/7/AE743F1F-632B-4809-87A9-AA1BB3458E31/DXSDK_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Povray':{
        name:'Povray',
        category:'Graphics',
        description:'Persistence of Vision Raytracer',
        emulateuseragent:'True',
        url:'http://www.povray.org/',
        version:{
            url:'http://www.povray.org/download/',
            regex:'The current official version of POV-Ray is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Official/Windows/povwin##DOTLESSVERSION##-32bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Povray-64':{
        name:'Povray',
        category:'Graphics',
        description:'Persistence of Vision Raytracer',
        emulateuseragent:'True',
        url:'http://www.povray.org/',
        version:{
            url:'http://www.povray.org/download/',
            regex:'The current official version of POV-Ray is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Official/Windows/povwin##DOTLESSVERSION##-64bit.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'WindowsServer2003ResourceKitTools':{
        name:'Windows Server 2003 Resource Kit Tools ',
        category:'Utility',
        description:'Manage AD',
        emulateuseragent:'True',
        url:'http://www.microsoft.com/en-us/download/details.aspx?id=17657',
        version:{
            url:'http://www.microsoft.com/en-us/download/details.aspx?id=17657',
            regex:'<span>([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/8/e/c/8ec3a7d8-05b4-440a-a71e-ca3ee25fe057/rktools.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VLC':{
        name:'VLC',
        category:'multimedia',
        description:'Multimedia player for files, DVD, Audio, CD, VCD and streaming products',
        emulateuseragent:'True',
        url:'http://www.videolan.org/',
        version:{
            url:'http://www.videolan.org/',
            regex:'var latestVersion  = \'([0-9]+(?:\.[0-9]+)+)\'',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://voxel.dl.sourceforge.net/project/vlc/##VERSION##/win32/vlc-##VERSION##-win32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\VLC media player',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'XEmacs':{
        name:'XEmacs',
        category:'Editor',
        description:'XEmacs',
        emulateuseragent:'True',
        url:'http://www.xemacs.org/Download/index.html',
        version:{
            url:'http://www.xemacs.org/Download/win32/index.html#InnoSetup-Stable-Download',
            regex:'XEmacs ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://ftp.xemacs.org/pub/xemacs/binaries/win32/InnoSetup/XEmacs_Setup_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\XEmacs_is1',
            value:'DisplayName',
            regex:'Xemacs([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'TortoiseHG-64':{
        name:'TortoiseHG-64',
        category:'Shell extention',
        description:'Windows shell extension',
        emulateuseragent:'True',
        url:'http://tortoisesvn.net/downloads.html',
        version:{
            url:'http://tortoisesvn.net/downloads.html',
            regex:'The current version is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/tortoisesvn/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'TortoiseHg',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'WindowsSystemControlCenter':{
        name:'Windows System Control Center',
        category:'Utilities',
        description:'WSCC is a free, portable program that allows you to install, update, execute and organize the utilities from various system utility suites',
        emulateuseragent:'True',
        url:'url=http://www.kls-soft.com/wscc/downloads.php',
        version:{
            url:'http://www.kls-soft.com/wscc/index.php',
            regex:'Latest version:</font></strong> ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.kls-soft.com/downloads/wscc.zip',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'CamStudio':{
        name:'CamStudio',
        category:'Multimedia',
        description:'Free streaming video software',
        emulateuseragent:'True',
        url:'url=http://camstudio.org/',
        version:{
            url:'http://camstudio.org/',
            regex:'Latest Version</strong></span><strong>: CamStudio ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://softlayer.dl.sourceforge.net/project/camstudio/stable/CamStudio_Setup_v2.6b_r294_%28build_24Oct2010%29.exe',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'CamStudio OSS',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    
    'LeagueOfLegends':{
        name:'League Of Legends',
        category:'Games',
        description:'HUEHUEHUEHUEHUEHUEHUEHUEHUEHUE',
        emulateuseragent:'True',
        url:'pvp.net',
        version:{
            url:'http://na.leagueoflegends.com/news/release-notes',
            regex:'League of Legends v([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://l3cdn.riotgames.com/Installer/NA_Installer/LeagueofLegends.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Eric':{
        name:'Eric Integrated Development Environment',
        category:'Programming',
        description:'Python3 IDE',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/eric-ide/',
        version:{
            url:'http://sourceforge.net/projects/eric-ide/',
            regex:'eric5-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/eric-ide/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Scratch':{
        name:'Scratch',
        category:'Programming',
        description:'Graphical Programming Language',
        emulateuseragent:'True',
        url:'http://scratch.mit.edu/',
        version:{
            url:'http://scratch.mit.edu/download',
            regex:'Scratch ([0-9]+(?:\.[0-9]+)+) Download',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.scratch.mit.edu/ScratchInstaller##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Scratch',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Inform7':{
        name:'Inform7',
        category:'Programming',
        description:'Interactive Fiction Programming CYOA',
        emulateuseragent:'True',
        url:'http://inform7.com/',
        version:{
            url:'http://inform7.com/download/',
            regex:'Inform release ([A-Z0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://inform7.com/download/content/##VERSION##/I7_##VERSION##_Windows.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Windif':{
        name:'Windif',
        category:'Utility',
        description:'Diff in Windows    ',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'http://www.codeproject.com/Articles/8302/WinDiff-or-WinMerge-the-way-you-want-it',
            regex:'Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.grigsoft.com/windiff.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Love2d':{
        name:'Love2d',
        category:'Programming',
        description:'Lua 2d engine',
        emulateuseragent:'True',
        url:'https://love2d.org/',
        version:{
            url:'https://love2d.org/',
            regex:'([0-9]+(?:\.[0-9]+)+) for Windows',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'https://bitbucket.org/rude/love/downloads/love-##VERSION##-win-x86.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Love2d-64':{
        name:'Love2d',
        category:'Programming',
        description:'Lua 2d engine',
        emulateuseragent:'True',
        url:'https://love2d.org/',
        version:{
            url:'https://love2d.org/',
            regex:'([0-9]+(?:\.[0-9]+)+) for Windows',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'https://bitbucket.org/rude/love/downloads/love-##VERSION##-win-x64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SDL':{
        name:'Simple DirectMedia Layer',
        category:'Programming',
        description:'Low Level Peripheral Library',
        emulateuseragent:'True',
        url:'http://www.libsdl.org/index.php',
        version:{
            url:'http://www.libsdl.org/download-1.2.php',
            regex:'SDL version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.libsdl.org/release/SDL-##VERSION##-win32.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SDL-64':{
        name:'Simple DirectMedia Layer',
        category:'Programming',
        description:'Low Level Peripheral Library',
        emulateuseragent:'True',
        url:'http://www.libsdl.org/index.php',
        version:{
            url:'http://www.libsdl.org/download-1.2.php',
            regex:'SDL version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.libsdl.org/release/SDL-##VERSION##-win32-x64.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
##    'OracleInstantBasic':{
##        name:'Oracal Instant Client',
##        category:'Database',
##        description:'Run Oracle Apps without having Oracle Client',
##        url:'http://www.oracle.com/technetwork/database/features/instant-client/index-100365.html',
##        version:{
##            url:'http://www.oracle.com/technetwork/topics/winsoft-085727.html',
##            regex:'Version ([0-9]+(?:\.[0-9]+)+)',
##            regexpos:0},
##        download:{
##            downloadtype:'directurl',
##            url:'',
##            regex:'',
##            regexpos:0},
##        silentflags:'/verysilent',
##        installversion:{
##            querytype:'',
##            key:'HKLM',
##            subkey:'SOFTWARE\\',
##            value:'',
##            regex:'([0-9]+(?:\.[0-9]+)+)',
##            regexpos:0
##            }
##        },
##    'OracleInstantBasic-64':{
##        name:'',
##        category:'',
##        description:'',
##        url:'',
##        version:{
##            url:'',
##            regex:'',
##            regexpos:0},
##        download:{
##            downloadtype:'pagesearch',
##            url:'',
##            regex:'',
##            regexpos:0},
##        silentflags:'/verysilent',
##        installversion:{
##            querytype:'',
##            key:'HKLM',
##            subkey:'SOFTWARE\\',
##            value:'',
##            regex:'([0-9]+(?:\.[0-9]+)+)',
##            regexpos:0
##            }
##        },
    'ArgoUML':{
        name:'Argo UML',
        category:'Utilities',
        description:'UML Drawing',
        emulateuseragent:'True',
        url:'http://argouml-downloads.tigris.org/',
        version:{
            url:'http://argouml-downloads.tigris.org/',
            regex:'Release ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://argouml-downloads.tigris.org/nonav/argouml-##VERSION##/ArgoUML-##VERSION##-setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ArgoUML',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'InteractiveC':{
        name:'Interactive C',
        category:'Programming',
        description:'C Interpreter',
        emulateuseragent:'True',
        url:'http://www.botball.org/ic',
        version:{
            url:'http://www.botball.org/ic',
            regex:'Vista: ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.botball.org/sites/default/files/page-files/77/InteractiveC_##UNDERSCOREVERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SMPlayer':{
        name:'MPlayer',
        category:'Multimedia',
        description:'Movie Player',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/smplayer/',
        version:{
            url:'http://sourceforge.net/projects/smplayer/',
            regex:'smplayer-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/smplayer/files/latest/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SMPlayer',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Boost':{
        name:'Boost',
        category:'Programming',
        description:'Fast C++ SDL',
        emulateuseragent:'True',
        url:'http://www.boost.org',
        version:{
            url:'http://www.boost.org/users/download/',
            regex:'Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://sourceforge.net/projects/boost/files/boost/##VERSION##/boost_##UNDERSCOREVERSION##.zip/download',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MyPaint':{
        name:'MyPaint',
        category:'Multimedia',
        description:'Open Source Graphics Editor',
        emulateuseragent:'True',
        url:'http://mypaint.intilinux.com/',
        version:{
            url:'http://mypaint.intilinux.com/?page_id=6',
            regex:'mypaint-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.gna.org/mypaint/mypaint-##VERSION##-win32-installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MyPaint-64':{
        name:'MyPaint',
        category:'Multimedia',
        description:'Open Source Graphics Editor',
        emulateuseragent:'True',
        url:'http://mypaint.intilinux.com/',
        version:{
            url:'http://mypaint.intilinux.com/?page_id=6',
            regex:'mypaint-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.gna.org/mypaint/mypaint-##VERSION##_win64_installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Blender':{
        name:'Blender',
        category:'Multipedia',
        description:'3d Modeling',
        emulateuseragent:'True',
        url:'http://www.blender.org',
        version:{
            url:'http://www.blender.org/download/get-blender/',
            regex:'Blender ([0-9]+(?:\.[0-9]+)+)',
            regexpos:2},
        download:{
            downloadtype:'directurl',
            url:'http://download.blender.org/release/Blender##VERSION##/blender-##VERSION##-release-windows32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Blender',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)-release',
            regexpos:0
            }
        },
    'Blender-64':{
        name:'Blender',
        category:'Multipedia',
        description:'3d Modeling',
        emulateuseragent:'True',
        url:'http://www.blender.org',
        version:{
            url:'http://www.blender.org/download/get-blender/',
            regex:'Blender ([0-9]+(?:\.[0-9]+)+)',
            regexpos:2},
        download:{
            downloadtype:'pagesearch',
            url:'http://download.blender.org/release/Blender##VERSION##/blender-##VERSION##-release-windows64.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Blender',
            value:'DisplayName',
            regex:'([0-9]+(?:\.[0-9]+)+)-release',
            regexpos:0
            }
        },
    'Mscgen':{
        name:'Mscgen',
        category:'Utility',
        description:'Message Seqence Chart Visualizer',
        emulateuseragent:'True',
        url:'http://www.mcternan.me.uk/mscgen/',
        version:{
            url:'http://www.mcternan.me.uk/mscgen/',
            regex:'current version is ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.mcternan.me.uk/mscgen/software/mscgen_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Mscgen',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Audacity':{
        name:'Audacity',
        category:'Multimedia',
        description:'Audio Editor',
        emulateuseragent:'True',
        url:'http://audacity.sourceforge.net',
        version:{
            url:'http://audacity.sourceforge.net',
            regex:'Audacity ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://audacity.googlecode.com/files/audacity-win-##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Audacity_is1',
            value:'DisplayName',
            regex:'Audacity ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Vuze':{
        name:'Vuze',
        category:'BitTorrent',
        description:'Heavyweight Torrent Client',
        emulateuseragent:'True',
        url:'http://www.vuze.com/',
        version:{
            url:'http://www.vuze.com/',
            regex:'Version ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://cf1.vuze.com/files/Vuze_Installer.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'WxWidgits':{
        name:'wxWidgits',
        category:'Programming',
        description:'GUI Library',
        emulateuseragent:'True',
        url:'http://www.wxwidgets.org/',
        version:{
            url:'http://www.wxwidgets.org/downloads/',
            regex:'<b>Current Stable Release: <a href="#latest_stable">([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://biolpc22.york.ac.uk/pub/##VERSION##/wxMSW-##VERSION##-Setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\wxWidgets_is1',
            value:'DisplayName',
            regex:'wxWidgets([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'IronPython':{
        name:'Iron Python',
        category:'Programming',
        description:'Python JiT For CLR',
        emulateuseragent:'True',
        url:'http://ironpython.codeplex.com/',
        version:{
            url:'http://ironpython.codeplex.com/releases/view/81726',
            regex:'IronPython ([0-9]+(?:\.[0-9]+)+) Installer',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download-codeplex.sec.s-thisdoesntworkl.com/Download/Release?ProjectName=ironpython&DownloadId=423690&FileTime=129858605577070000&Build=19383',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            valsearchregex: 'IronPython',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Fpc':{
        name:'Free Pascal',
        category:'Programming',
        description:'Implementation of Pascal',
        emulateuseragent:'True',
        url:'http://www.freepascal.org',
        version:{
            url:'http://www.freepascal.org/download.var',
            regex:'The latest release is <b>([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://softlayer.dl.sourceforge.net/project/freepascal/Win32/##VERSION##/fpc-##VERSION##.i386-win32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SmartEiffel':{
        name:'Smart Eiffel',
        category:'Programming',
        description:'A GNU Eiffel compiler',
        emulateuseragent:'True',
        url:'https://gforge.inria.fr/projects/smarteiffel/',
        version:{
            url:'https://gforge.inria.fr/frs/?group_id=184',
            regex:'SmartEiffel SmartEiffel ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'https://gforge.inria.fr/frs/download.php/2464/SmartEiffel-##DASHVERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Erlang':{
        name:'Erlang',
        category:'Programming',
        description:'Soft Realtime systems language',
        emulateuseragent:'True',
        url:'http://www.erlang.org/',
        version:{
            url:'http://www.erlang.org/download.html',
            regex:'Download Erlang/OTP ([A-Z0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.erlang.org/download/otp_win32_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Erlang-64':{
        name:'Erlang',
        category:'Programming',
        description:'Soft Realtime systems language',
        emulateuseragent:'True',
        url:'http://www.erlang.org/',
        version:{
            url:'http://www.erlang.org/download.html',
            regex:'Download Erlang/OTP ([A-Z0-9]+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.erlang.org/download/otp_win64_##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SBCL':{
        name:'Steel Bank Common Lisp',
        category:'Programming',
        description:'Lisp Implementation',
        emulateuseragent:'True',
        url:'http://www.sbcl.org/',
        version:{
            url:'http://sourceforge.net/projects/sbcl/',
            regex:'sbcl-([0-9]+(?:\.[0-9]+)+)', 
           regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-dca2.dl.sourceforge.net/project/sbcl/sbcl/##VERSION##/sbcl-##VERSION##-x86-windows-binary.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Octave-MinGW':{
        name:'Octave',
        category:'Programming',
        description:'Programming Language',
        emulateuseragent:'True',
        url:'http://sourceforge.net/projects/octave',
        version:{
            url:'http://sourceforge.net/projects/octave',
            regex:'mechanics-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://sourceforge.net/projects/octave/files/Octave Windows binaries/Octave 3.6.2 for Windows Microsoft Visual Studio/octave-3.6.2-optiminterp-0.3.3-vs2010-setup.exe/download',
            regex:'"a href=\"(http://.+) class=\"direct-download\""',   
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    
    'EMPTYEND':{
        name:'',
        category:'',
        description:'',
        emulateuseragent:'True',
        url:'',
        version:{
            url:'',
            regex:'',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        }
    }

