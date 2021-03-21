import socket
import time
import xml.etree.ElementTree as ET

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 55555
BUFFER = 4096

afz_tree = ET.parse("udp-client/afz.xml")
root = afz_tree.getroot()
xml_string = ET.tostring(root, encoding="utf-8")


def main():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (UDP_IP_ADDRESS, UDP_PORT)
    try:
        while True:
            socket_client.sendto(xml_string.encode(), address)
            response, addr = socket_client.recvfrom(BUFFER)
            print("Sending Data")
            time.sleep(5)
    finally:
        socket_client.close()


if __name__ == "__main__":
    main()