from scapy import sniff
import cryptography

class refractionNet:
    def detect_tapdance(packet):
        
        if(self.check_tag(packet))                      ##If Refracted Packet, then return 
            return packet
            print(packet)
        
    def check_tag(packet):                              ##True if refracted, False if normal
        ##some crypto shit

    def decrypt_packet(packet):                         ##decrypt and extract real url from packet
        ##some crypto shit
        
