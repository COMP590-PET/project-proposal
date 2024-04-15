from server.refract import refractionNet as rn
from scapy import sniff
import requests

##what if the server just ignored the return from decoy on its own?

packet = sniff(filter="tcp port 443 and src", prn=rn.detect_tapdance, store=0)           ##monitor outgoing packets 
src_ip = packet.ip
real_url = rn.decrypt_packet(packet.load)                                                ##/where is the payload within the packet??
response = requests.get(padded_url)                                                      ##
