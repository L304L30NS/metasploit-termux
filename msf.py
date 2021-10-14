from colorama import *
from os import system
import os
from time import sleep
init(autoreset=True)

###

#Colors Fore
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGNETA = Fore.MAGENTA
RED=Fore.RED
#Colors Back
BACKBLUE = Back.BLUE
BACKGREEN = Back.GREEN
BACKYELLOW = Back.YELLOW
BACKCYAN = Back.CYAN
BACKMAGNETA = Back.MAGENTA
BACKRED=Back.RED
#Colors Style
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL
NORMAL=Style.NORMAL

###

AUTH = "on termux".rjust(40)
print( CYAN +"""

        ┏┳┓┏━╸╺┳╸┏━┓┏━┓┏━┓╻  ┏━┓╻╺┳╸
        ┃┃┃┣╸  ┃ ┣━┫┗━┓┣━┛┃  ┃ ┃┃ ┃
        ╹ ╹┗━╸ ╹ ╹ ╹┗━┛╹  ┗━╸┗━┛╹ ╹
""")
print(MAGNETA + AUTH.upper())
#sleep(3)
print(GREEN +"\n Do You Want To Install ?".upper())
print(CYAN + " push enter to continue".upper() + MAGNETA + " >>" )

###
MAIN_PKGS = " pkg install -y python clang git wget zip tar ruby "

DEPENDENCIES = "pkg install -y autoconf bison coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ncurses-utils ncurses   termux-tools termux-elf-cleaner pkg-config "

RM_RUBY = "apt purge ruby -y && apt autoremove"

RM_MSF_OLD_DIR = "rm -rf $PREFIX/share/metasploit-framework $HOME/metasploit-framework $PREFUX/bin/msfconsole $PREFIX/bin/msfvenom"

###

input()
print(BACKMAGNETA +"\n    removing metasploit if installed".upper())
sleep(3)
system(RM_RUBY + RM_MSF_OLD_DIR)
print(BACKBLUE +"\n            installing packages".upper())
system(MAIN_PKGS)
print(BACKBLUE + "\n          installing dependencies  ".upper())
sleep(2)
system(DEPENDENCIES)

print(BACKGREEN  +"\n     CLONING METASPLOIT-FRAMEWORK FOLDER  " +RESET)
sleep(2)
system('cd $HOME')
system ('git clone https://github.com/rapid7/metasploit-framework.git --depth=1 ')
 
print(BACKCYAN + RED +"\n       Intalling Gems" .upper() +RESET	)

###
system ('wget https://raw.githubusercontent.com/Learn-Termux/metasploit-termux/main/bigdecimal.sh ')
system ('chmod +x bigdecimal.sh')
system ('./bigdecimal.sh')
os.chdir("metasploit-framework") 
system	('gem install bundler')
system	('gem install nokogiri -- --use-system-libraries')
system	('gem install actionpack')
system	('bundle update activesupport')
system	('bundle update --bundler')
system	("bundle install -j$(nproc --all)")


print(BACKBLUE	+ "     creating symoblic link    ".upper())
system	('ln -s $HOME/metasploit-framework/msfconsole /data/data/com.termux/files/usr/bin/')
system	('ln -s $HOME/metasploit-framework/msfvenom /data/data/com.termux/files/usr/bin/')


print( BACKGREEN + "     creating database  ".upper())
system ('wget https://raw.githubusercontent.com/Learn-Termux/termux-metasploit/main/database.yml -O $HOME/metasploit-framework/config/database.yml')
system	('wget https://raw.githubusercontent.com/Learn-Termux/metasploit-termux/main/pg_ctl.sh -O $HOME/pg_ctl.sh')
system	('mkdir -p $PREFIX/var/lib/postgresql')
system	('initdb $PREFIX/var/lib/postgresql')
system	('pg_ctl -D $PREFIX/var/lib/postgresql start')
system	('createuser msf')
system	('createdb msf_database')


print(BACKBLUE	+ "\n\n Metasploit-Framework Installination Complete ... \n")
