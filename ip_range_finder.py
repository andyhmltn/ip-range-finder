from struct import *
from socket import *

def ip_range_search(start, end, search):

	found     = False
	search_ip = gethostbyname(search)

	try:
		for ip in xrange(unpack('!I',inet_pton(AF_INET,start))[0],unpack('!I',inet_pton(AF_INET,end))[0]):
			current_ip = inet_ntop(AF_INET, pack('!I', ip))

			if current_ip == search_ip:
				found = current_ip
	except error:
		print('Invalid IP Address!')

	return found

start_ip = raw_input('Please Enter The First IP: ')
end_ip   = raw_input('Please Enter The Last IP: ')

domain   = raw_input('Please Enter The Domain Name: ')

print('Please wait, finding domain in IP address... (This may take a while)')

result = ip_range_search(start_ip, end_ip, domain)

if result:
	print('IP in given range! Found on IP: ' + result)
else:
	print('IP not in given range')



