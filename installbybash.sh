
#!/data/data/com.termux/files/usr/bin/bash

green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
cyan='\033[36m'
magneta='\033[1;35m'
reset='\033[0m'


clear
echo -e "$green       Removing Ruby If Installed ... $reset"
apt purge ruby -y
echo -e "$green       Removing Ruby Gems If Installed ... $reset"
rm -rf $PREFIX/lib/ruby/gems
echo
echo -e "$green         Updating Packages ... $reset"
pkg update -y
apt upgrade
echo 
echo -e "$green         Installing Dependencies  ... $reset"
pkg install x11-repo
pkg install -y python autoconf bison clang coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ncurses-utils ncurses git wget unzip zip tar termux-tools termux-elf-cleaner pkg-config git ruby

echo
echo -e "$green Updating pip and installing requests ... $reset"
python3 -m pip install --upgrade pip
python3 -m pip install requests

echo
echo -e "$green     Fixing Ruby Big Decimal $reset"
apt install -yq patchelf

for i in aarch64-linux-android arm-linux-androideabi \
    i686-linux-android x86_64-linux-android; do

    if [ -e "$PREFIX/lib/ruby/2.6.0/${i}/bigdecimal.so" ]; then
        if [ -n "$(patchelf --print-needed "$PREFIX/lib/ruby/2.6.0/${i}/bigdecimal/util.so" | grep bigdecimal.so)" ]; then
            exit 0
        fi

        patchelf --add-needed \
            "$PREFIX/lib/ruby/2.6.0/${i}/bigdecimal.so" \
            "$PREFIX/lib/ruby/2.6.0/${i}/bigdecimal/util.so"
    fi
done

#
echo
echo -e "$green   Erasing Metasploit Folder If Already Exists ... $reset"

rm -rf $HOME/metasploit-framework
echo
echo -e "        Downloading Metasploit ... $reset"
cd $HOME
git clone https://github.com/rapid7/metasploit-framework.git --depth=1


echo
echo -e "$green    Installing Gems ... $reset "
#echo -e "$green     Installing Bundler ... $reset"
cd metasploit-framework/
gem install bundler
gem install nokogiri -v 1.8.0 -- --use-system-libraries
gem install nokogiri -v 1.12.4 -- --use-system-libraries
gem install actionpack
bundle update activesupport
bundle update --bundler

echo
echo -e "$green       Creating Symbolic Link ... $reset"
if [ -e $PREFIX/bin/msfconsole ];then
	rm $PREFIX/bin/msfconsole
fi
if [ -e $PREFIX/bin/msfvenom ];then
	rm $PREFIX/bin/msfvenom
fi
ln -s $HOME/metasploit-framework/msfconsole /data/data/com.termux/files/usr/bin/
ln -s $HOME/metasploit-framework/msfvenom /data/data/com.termux/files/usr/bin/
termux-elf-cleaner /data/data/com.termux/files/usr/lib/ruby/gems/3.0.0/gems/pg-0.20.0/lib/pg_ext.so

echo
echo -e "$green      Data Base Configuration  ... $reset"
cd $HOME/
wget https://raw.githubusercontent.com/Learn-Termux/termux-metasploit/main/database.yml -O $HOME/metasploit-framework/config/database.yml
wget https://raw.githubusercontent.com/Learn-Termux/metasploit-termux/main/pg_ctl.sh -O $HOME/pg_ctl.sh
chmod +x pg_ctl.sh
mkdir -p $PREFIX/var/lib/postgresql
initdb $PREFIX/var/lib/postgresql
pg_ctl -D $PREFIX/var/lib/postgresql start
createuser msf
createdb msf_database
echo
echo -e "$magneta Installed Metasploit-Framework $reset "
echo -e "$yellow Run Metasploit by msfconsole  $reset"







