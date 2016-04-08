import sys
from TransactionDecoder import TransactionDecoder

if __name__ == "__main__":

	try:
		hexdata = sys.argv[1]
	except Exception, e:
		print "Usage: txdecoder.py <rawtxdata>"
	else:
		print TransactionDecoder(sys.argv[1])

