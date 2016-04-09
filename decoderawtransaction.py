import sys
from decoder.transaction import TransactionDecoder


if __name__ == "__main__":

    try:
        hexdata = sys.argv[1]
    except Exception, e:
        print "Usage: decoderawtransaction.py <rawtxdata>"
    else:
        print TransactionDecoder(hexdata)
