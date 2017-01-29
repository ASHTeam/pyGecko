from tcpgecko import TCPGecko
import sys

try:
  input = raw_input
except:
  pass
ipfield = input("Your Wii U IP: ")
tcp = TCPGecko(ipfield)
print(tcp.readkern(0x10000000))
tcp.s.close()
print("Done.")
