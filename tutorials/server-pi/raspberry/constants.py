''' Hold all constants

And IP Handshakes'''

import subprocess
import cPickle as pickle  #faster serialisation

GLASS = 0
PAPER = 1
CARDBOARD = 2
PLASTIC = 3
METAL = 4
TRASH = 5

DIM1 = 384
DIM2 = 512

def read_IP():
    with open("./IP_constants.rb","rb") as f:
        return pickle.load(f)

def write_IP(L):
    # L is list of [RPI_IP,MAC_IP]
    with open("./IP_constants.rb","wb") as f:
        pickle.dump(L,f)

def IP_initialise():
    ''' Initialise Ip addresses, communicate to host ... \n'''
    while True:
        RPI_IP=raw_input("\n Enter IP for Raspberry Pi \t")
        MAC_IP=raw_input("\n Enter IP for Mac \t")
        key=raw_input("\n Press Q to break \t")
        if key.upper()=='Q':
            break
        else:
            print "Retrying inputs ...\n"

    write_IP([RPI_IP,MAC_IP])

    PORT_CONSTANTS='Ankivarun@'+MAC_IP+':~/Documents/Academics/IIT\ M/Projects/Smart\ DB/mac_interface/'
    subprocess.call(['sshpass','-p','1207','rsync','./IP_constants.rb',PORT_CONSTANTS])

if __name__=='__main__':
    IP_initialise()
