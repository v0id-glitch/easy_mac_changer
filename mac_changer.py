
import subprocess

print("                              _                                 ")
print("                             | |                                ")
print("  _ __ ___   __ _  ___    ___| |__   __ _ _ __   __ _  ___ _ __ ")
print(" | '_ ` _ \ / _` |/ __|  / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|")
print(" | | | | | | (_| | (__  | (__| | | | (_| | | | | (_| |  __/ |   ")
print(" |_| |_| |_|\__,_|\___|  \___|_| |_|\__,_|_| |_|\__, |\___|_|   ")
print("                                                 __/ |          ")
print("                                                |___/           ")

interface = raw_input("[+] interface > ")
new_mac = raw_input("[+] new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface , "down"])
subprocess.call(["ifconfig" , interface ,"hw" , "ether", new_mac])
subprocess.call(["ifconfig" , interface , "up"])