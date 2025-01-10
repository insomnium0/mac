#!/usr/bin/env python


#                 source code for my 𝓶𝓪𝓬 𝓬𝓱𝓪𝓷𝓰𝓮𝓻 👅
#       _____   
#  _   /___  \      Made by: an actual retard
# (_)   ___) /          _________________
#      (___ (        💖 colon 3 supremacy 💖
#  _       ) \
# (_) /\___/  /
#     \______/ 
            

import subprocess # adds the module that lets you execute to bash through the python script

import time # just a silly little module i added to make a delay after the "changed your mac!" thing

import optparse # module that adds options and arguments, so instead of having the user input their mac and interface through individual inputs like before, it imports the module to allows them to use arguments such as "-i", "-m", and so on. (more args coming soon!)

# this little piece of code adds an object that can parse arguements, ie. the little "-i" things and whatnot.
parser = optparse.OptionParser()

# these 2 pieces of code call the parser object, and then calls the method add_option, which adds the option to use shortened args (or full length if you're weird...), and then puts those into the variables address, and interface, respectively.
parser.add_option("-i","--interface", dest="interface", help="Interface to change the mac address.")
parser.add_option("-m","--mac", dest="address", help="MAC address to change to.")

# this parses the args, and stores them in options and arguements
options, arguments = parser.parse_args()

# these are the variables that contain the arguments from above
adr = options.address
intr = options.interface

# displays an error and usage message if the user doesnt input doesnt input one or the other
if not intr or not adr:
    print("Error: Both interface and MAC address must be provided.")
    print("Usage: python mac.py -i <interface> -m <mac_address>")
    exit(1)

# runs the basic shell commands that takes down the interface given, changes the address to whatever you set it to, and then puts it back up.
subprocess.call(["sudo", "ip", "link", "set", "dev" , intr , "down"],)
subprocess.call(["sudo", "ip", "link", "set", "dev" , intr , "address" , adr])
subprocess.call(["sudo", "ip", "link", "set", "dev", intr , "up"])

# prints that the MAC address has, indeed, been changed.
print ('✅ Changed MAC address for '+ intr + " to " + adr + "!\n")

# im ngl this is literally just an artificial 2 second delay, gives the user more time to read that their MAC was successfully changed! :D
time.sleep(2)


# this part asks if you would like to see confirmation that the address has been changed, so you dont gotta go through the hassle of typing any more convoluted ip commands.
print("Would you like to see confirmation to make sure your address has been changed?\n")

# a while loop; basically loops this little section infinitely if anything else other than yes/y or no/n is entered, but it immediately stops the program if either of those are put in.
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


# alien lightskin wuz here :P

