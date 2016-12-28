import pcapy
import sys
import getopt
from impacket.ImpactDecoder import *

device = 'wlp4s0'
filter = 'arp'
decoder = Decoder()


def handle_packet(hdr, data):
    print decoder.decode(data)

