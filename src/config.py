""""Library to interact with config file"""
import configparser
import argparse

class ConfigLibrary:
    """Class where is stored the configuration of the program"""
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('configuration/inquisitor.config')
        self.parser = argparse.ArgumentParser(
            description="""INQUISITOR ARP SPOOFER:\n
            This program spoof arp tables of victims in full duplex mode\n
            Once ARP tables are spoofed the program sniff the traffic"""
        )
        self.set_arguments()

    def set_arguments(self):
        """Function sets the arguments of the program"""
        self.parser.add_argument('-ips', '--ip_spoofer', metavar='<ip_spoofer>', type=str,
                                help="ip spoofer")
        self.parser.add_argument('-ms', '--mac_spoofer', metavar='<mac_spoofer>', type=str,
                                help="mac spoofer")
        self.parser.add_argument('-ipc', '--ip_client', metavar='<ip_client>', type=str,
                                help="ip client")
        self.parser.add_argument('-mc', '--mac_client', metavar='<mac_client>', type=str,
                                help="mac client")
        self.parser.add_argument('-ipsv', '--ip_server', metavar='<ip_server>', type=str,
                                help="ip spoofer")
        self.parser.add_argument('-msv', '--mac_server', metavar='<mac_server>', type=str,
                                help="mac spoofer")
        self.parser.add_argument('-v', '--verbose', action='store_true',
                                help="activates verbose mode")

    def get_log_level(self):
        """function returns the log level"""
        return self.config['logger']['level']
