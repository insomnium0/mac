#!/usr/bin/env python

#  i wuz here :3

import subprocess
import time
adr = input("enter mac address to change to: ")
print("\n")
intr = input("enter interface to change to: ")
print("\n")


subprocess.call(["sudo", "ip", "link", "set", "dev" , intr , "down"],)
subprocess.call(["sudo", "ip", "link", "set", "dev" , intr , "address" , adr])
subprocess.call(["sudo", "ip", "link", "set", "dev", intr , "up"])

print ('✅ Changed MAC address for '+ intr + " to " + adr + "!\n")

time.sleep(2)

print("Would you like to see confirmation to make sure your address has been changed?\n")


while True:
    choice = input("yes or no? : ").strip().lower()

    if choice in ["yes", "y"]:
        print("\nYou answered YES! Here it is!\n")
        subprocess.call("ip link show dev " + intr, shell=True)
        break
    elif choice in ["no", "n"]:
        print("\nYou answered NO! Now DIE!!!\n")
        break
    else:
        print("\nInvalid input. Please enter yes or no. idiot.\n")




