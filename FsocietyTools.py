import os
import time
import colorama
from colorama import Fore
import git

def banner_banner():
	os.system("clear")
	os.system("python3 banner.py")
	print("Fuck_Society----------creador: Crypto_453")
def start():
	os.system("python3 FsocietyTools.py")
def list_a():
	list_list = ["[ 1 ] Envio de mensajes anonimos", "[ 2 ] Escaneres de vulneravilidades", "[ 3 ] Herramientas de Explotacion", "[ 4 ] Ataques de contraseñas", "[ 5 ] Ataques Wireless", "[ 6 ] Herramientas Forenceses", "[ 7 ] Herramientas de Sniffing", "[ 8 ] Lenguajes de Programacion", "[ 9 ] FREE VPN", "[ 10 ] TorBrowser", "[ 11 ] Wallpapers", "[ 00 ] EXIT"]
	for list_x in list_list:
		print(list_x)
		time.sleep(0.2) 
def sms_sms():
	sms_list = ["[ 1 ] SETSMS", "[ 2 ] TBomb", "[ 3 ] GOD-KILLER", "[ 00 ] Volver"]
	for sms_x in sms_list:
		print(sms_x)
		time.sleep(0.2)

def scan_scan():
	scan_list = ["[ 1 ] nmap", "[ 2 ] dmitry", "[ 3 ] linys", "[ 4 ] ike-scan", "[ 5 ] p0f", "[ 00 ] Volver"]
	for scan_x in scan_list:
		print(scan_x)
		time.sleep(0.2)

def explotation_explotation():
	list_x = ["[ 1 ] Metasploit Framework", "[ 2 ] Social EnginerToolKit", "[ 3 ] sqlmap", "[ 4 ] apkTool", "[ 00 ] Volver "]
	for list_n in list_x:
		print(list_n)
		time.sleep(0.2)
def passwword_password():
	passw_list = ["[ 1 ] Hydra", "[ 2 ] Medusa", "[ 3 ] HashCat", "[ 4 ] Ncrack", "[ 5 ] John", "[ 6 ] crunch", "[ 7 ] cupp", "[ 00 ] Volver"]
	for passw in passw_list:
		print(passw)
		time.sleep(0.2)

def wireless_wireless():
	wire_list = ["[ 1 ] Aircrack-ng", "[ 2 ] wifite", "[ 3 ] reaver", "[ 4 ] Wifite2", "[ 00 ]"]
	for list_wi in wire_list:
		print(list_wi)
		time.sleep(0.2)
def forense_forense():
	fore_list = ["[ 1 ] Autopsy", "[ 2 ] binwalk", "[ 3 ] xplico", "[ 4 ] hashdeep", "[ 00 ] Volver"]
	for list_foren in fore_list:
		print(list_foren)
		time.sleep(0.2)
def sniffing_sniffing():
	sni_list = ["[ 1 ] bettercap", "[ 2 ] Wireshark", "[ 3 ] hamster", "[ 4 ] responder", "[ 5 ] macchanger", "[ 00 ] Volver"]
	for sni_x in sni_list:
		print(sni_x)
		time.sleep(0.2)
def languaje():
	list_lan = ["[ 1 ] python3", "[ 2 ] c++", "[ 3 ] php", "[ 4 ] JavaScript", "[ 00 ] Volver"]
banner_banner()
list_a()
fsociety_a = int(input("===> "))
if fsociety_a == 1:
	banner_banner()
	sms_sms()
	sms_in = int(input("===> "))
	if sms_in == 1:
		rute_a = input("Escriba la ruta: ")
		git.Git(f"{rute_a}").clone("https://github.com/Darkmux/SETSMS")
		start()
	elif sms_in == 2:
		rute_tbomb = input("Escriba la ruta: ")
		git.Git(f"{rute_tbomb}").clone("https://github.com/TheSpeedX/TBomb")
		start()
	elif sms_in == 3:
		rute_god_killer = input("Escriba la ruta: ")
		git.Git(f"{rute_god_killer}").clone("https://github.com/FDX100/GOD-KILLER")
		start()
	elif sms_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 2:
	banner_banner()
	scan_scan()
	scan_in = int(input("===> "))
	if scan_in == 1:
		os.system("apt install nmap")
		start()
	elif scan_in == 2:
		os.system("apt install dmitry")
		start()
	elif scan_in == 3:
		rute_dmitry= input("Escriba la ruta: ")
		git.Git(f"{rute_dmitry}").clone("https://github.com/CISOfy/lynis")
		start()
	elif scan_in == 4:
		rute_ike = input("Escriba la ruta: ")
		git.Git(f"rute_ike").clone("https://github.com/royhills/ike-scan")
		start()
	elif scan_in == 5:
		rute_pof = input("Escriba la ruta: ")
		git.Git(f"{rute_pof}").clone("https://github.com/p0f/p0f")
		start()
	elif scan_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 3:
	banner_banner()
	explotation_explotation()
	ex_in =  int(input("===> "))
	if ex_in == 1:
		rute_meta = input("Escriba la ruta: ")
		git.Git(f"{rute_mete}").clone("https://github.com/rapid7/metasploit-framework")
		start()
	elif ex_in == 2:
		rute_social = input("Escriba la ruta: ")
		git.Git(f"{rute_social}").clone("https://github.com/trustedsec/social-engineer-toolkit")
		start()
	elif ex_in == 3:
		rute_sql = input("Escruba la ruta: ")
		git.Git(f"{rute_sql}").clone("https://github.com/sqlmapproject/sqlmap")
		start()
	elif ex_in == 4:
		rute_apk = input("Escriba la ruta: ")
		git.Git(f"{rute_apk}").clone("https://github.com/iBotPeaches/Apktool")
		start()
	elif ex_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 4:
	banner_banner()
	passwword_password()
	passw_in = int(input("===> "))
	if passw_in == 1:
		os.system("apt -y install hydra")
		start()
	elif passw_in == 2:
		os.system("apt -y install medusa")
		start()
	elif passw_in == 3:
		rute_has = input("Escriba la ruta: ")
		git.Git(f"{rute_has}").clone("https://github.com/hashcat/hashcat")
		start()
	elif passw_in == 4:
		os.system("apt -y install ncrack")
		start()
	elif passw_in == 5:
		os.system("apt -y install john")
		start()
	elif passw_in == 6:
		os.system("apt -y install crunch")
		start()
	elif passw_in == 7:
		rute_cupp = input("Escriba la ruta: ")
		git.Git(f"{rute_cupp}").clone("https://github.com/Mebus/cupp")
		start()
	elif passw_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 5:
	banner_banner()
	wireless_wireless()
	wire_in = int(input("===> "))
	if wire_in == 1:
		os.system("apt -y install aircrack-ng")
		start()
	elif wire_in == 2:
		rute_wi = input("Escriba la ruta: ")
		git.Git(f"{rute_wi}").clone("https://github.com/derv82/wifite")
		start()
	elif wire_in == 3:
		rute_rever = input("Escriba la ruta: ")
		git.Git(f"{rute_rever}").clone("https://github.com/t6x/reaver-wps-fork-t6x")
		start()
	elif wire_in == 4:
		rute_wifite = input("Escriba la ruta: ")
		git.Git(f"{rute_wifite}").clone("https://github.com/derv82/wifite2")
		start()
	elif wire_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 6:
	banner_banner()
	forense_forense()
	for_in = int(input("===> "))
	if for_in == 1:
		rute_auto =  input("Escriba la ruta: ")
		git.Git(f"{rute_auto}").clone("https://github.com/sleuthkit/autopsy")
		start()
	elif for_in == 2:
		rute_bin = input("Escriba la ruta: ")
		git.Git(f"{rute_bin}").clone("https://github.com/ReFirmLabs/binwalk")
		start()
	elif for_in == 3:
		rute_xp = input("Escriba la ruta: ")
		git.Git(f"{rute_xp}").clone("https://github.com/xplico/xplico")
		start()
	elif for_in == 4:
		rute_hashdeep = input("Escriba la ruta: ")
		git.Git(f"{rute_hashdeep}").clone("https://github.com/jessek/hashdeep")
		start()
	elif for_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 7:
	banner_banner()
	sniffing_sniffing()
	snif_in = int(input("===> "))
	if snif_in == 1:
		os.system("apt -y install bettercap")
		start()
	elif snif_in == 2:
		os.system("apt -y install wireshark")
		start()
	elif snif_in == 3:
		os.system("apt -y install hamster")
		start()
	elif snif_in == 4:
		os.system("apt -y install responder")
		start()
	elif snif_in == 5:
		os.system("apt -y install macchanger")
		start()
	elif snif_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 8:
	banner_banner()
	languaje()
	lan_in = int(input("===> "))
	if lan_in == 1:
		os.system("apt -y update")
		os.system("apt  -y install python3")
		start()
	elif lan_in == 2:
		os.system("apt -y update")
		os.system("sudo apt -y install build-essential")
		start()
	elif lan_in == 3:
		os.system("apt -y update")
		os.system("apt -y install php")
		start()
	elif lan_in == 4:
		print(Fore.YELLOW+"Instalacion Completada!!!")
		start()
	elif lan_in == 00:
		start()
	else:
		print(Fore.RED+"Error Fatal!!!, Intentelo denuevo")
elif fsociety_a == 9:
	os.system("./script")
	start()
elif fsociety_a == 10:
	os.system("./script_Tor")
	start()
elif fsociety_a == 11:
	os.system("./wallpaper")
	start()
elif fsociety_a == 00:
	os.system("")
else:
	print("ERROR!!!")