import socket, threading, sys, traceback, os,time



if __name__ == "__main__":


	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		packets_per_second = sys.argv[3]
		payload_size = sys.argv[4]
		seconds = sys.argv[5]  

	except:
		print "[Usage: TrafficSimulator.py Server_name Server_port packets_per_second payload_size_in_bytes_seconds_to_run]\n"  

	packetcount = 1
	toSend = int(packets_per_second) * int(seconds)
	genSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	start = time.time();
	lastSent = start

	waitTime = 1.0 / int(packets_per_second)
	
	while(packetcount < toSend ):
		if ((time.time() - lastSent) > waitTime):
			lastSent = time.time()
			#print str(time.time() - lastSent) + " " + str(waitTime) + "\n"
			preamble = "arnedab:" + str(packetcount) + ":" + str(packets_per_second) + ":" + str(payload_size) + ":" + str(seconds) + ":"
			if (len(preamble) < int(payload_size)):
				
				payload = preamble + os.urandom(int(payload_size)-len(preamble))
			else:
				payload = preamble
			
			genSocket.sendto(payload,(serverAddr,int(serverPort)))
			packetcount = packetcount + 1
			

	print "Sent " + str(packetcount) + " packages in " + str(lastSent-start) + " seconds"  