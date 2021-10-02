import subprocess
import optparse
import re




def get_argument():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    ( options  , args ) = parser.parse_args()
    if not options.interface :
        parser.error("[-] interface is require please specify it for info use --help  ")
    elif not options.new_mac:
        parser.error("[-] mac address is require please specify it for info use --help  ")

    return options
def mac_changer(interface ,macAddress):
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw","ether" , macAddress ])
    subprocess.call(["ifconfig" , interface , "up" ])


options = get_argument()




mac_changer( options.interface ,options.new_mac)


def check_mac_state(interface , new_mac) :
    ifconfig = subprocess.check_output("ifconfig " + interface , shell=True)
    mac_search_result =  re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig )
    if mac_search_result :

        if (mac_search_result.group(0) == new_mac) :
            print("[+] success to change the mac address to this value  " + mac_search_result.group(0))
        else:
            print("[-] faild to change the mac address   ")

    else: print("[-] faild to change the mac address ")





check_mac_state(options.interface , options.new_mac )
