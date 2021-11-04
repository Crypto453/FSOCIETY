import colorama
from colorama import Fore
import time

banner_a = ("#######  #####  #######  #####  ### ####### ####### #     # ")
banner_b = ("#       #     # #     # #     #  #  #          #     #   #  ")
banner_c = ("#       #       #     # #        #  #          #      # #   ")
banner_d = ("#####    #####  #     # #        #  #####      #       #    ")
banner_e = ("#             # #     # #        #  #          #       #    ")
banner_f = ("#       #     # #     # #     #  #  #          #       #    ")
banner_g = ("#        #####  #######  #####  ### #######    #       #    ")
banner_banner = [banner_a, banner_b, banner_c, banner_d, banner_e, banner_f, banner_g]
for banner_x in banner_banner:
	print(banner_x)
	time.sleep(0.2)

