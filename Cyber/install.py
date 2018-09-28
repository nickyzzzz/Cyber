import os, sys
from time import sleep

if not os.geteuid() == 0:
    sys.exit("Please run this script as root")

header = """
Cybertool
"""

print header
print "[Operating Systems Available]"
print "(1) Kali Linux "


option = input("Select Operating System:")

if option == 1:
    print "Loading..."
    os.system('apt-get install python-pip')
    os.system('apt-get install pip')
    import pip
    install = os.system("apt-get update && apt-get install -y build-essential git")
    install2 = os.system("cp -R Cyber/ /opt/ && cp Cyber.py /opt/Cyber && cp run.sh /opt/Cyber && cp run.sh /usr/bin/Cyber && chmod +x /usr/bin/Cyber")
    os.system('apt-get install sendemail')
    os.system('pip install qrcode')
    os.system('pip install google')
    os.system('pip install mechanize')
    os.system('pip install requests')
    os.system('apt-get install lib32ncurses5-dev')
    os.system('apt-get install libncurses5-dev')
    pip.main(["install", "netifaces", "scapy", "SpoofMAC", "pythonwhois", "readline", "BeautifulSoup"])
    print "\033[1;32m[!] Finished Installing! Run 'Cyber' to run program [!]\033[0m"
    sys.exit()
else:
    print "Tool NOT installed......!!!!! Or Improper Choice ...!!!Something went wrong!"