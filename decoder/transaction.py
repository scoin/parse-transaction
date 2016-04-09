from hashlib import sha256
import binascii
import json

class TransactionDecoder:
	def __init__(self, hexstring):
		self.hex = hexstring
		self.__tx = binascii.unhexlify(hexstring)
		self.__position = 0
		self.transaction = {}
		self.transaction["txid"] = self.get_txid(hexstring)
		self.transaction["version"] = self.__get_int_bytes(4)

		self.transaction["num_inputs"] = self.__get_int_bytes(1)

		self.transaction["vin"] = []

		for i in range(self.transaction["num_inputs"]):
			self.transaction["vin"].append({
				"txid": self.__get_string_bytes(32, reverse=True),
				"vout": self.__get_int_bytes(4)
			})
			scriptBytes = self.__get_int_bytes(1)
			self.transaction["vin"][i]["scriptSig"] = self.__get_string_bytes(scriptBytes)
			self.transaction["vin"][i]["sequence"] = self.__get_string_bytes(4)

		self.transaction["num_outputs"] = self.__get_int_bytes(1)

		self.transaction["vout"] = [];

		for j in range(self.transaction["num_outputs"]):
			self.transaction["vout"].append({
				"qty": self.__get_int_bytes(8),
				"n": j
			})
			outputBytes = self.__get_int_bytes(1)
			self.transaction["vout"][j]["script"] = self.__get_string_bytes(outputBytes)

		self.transaction["locktime"] = self.__get_int_bytes(4)


	@staticmethod
	def get_txid(hexstring):
		return sha256(sha256(hexstring.decode('hex_codec')).digest()).digest()[::-1].encode('hex_codec')


	def __read_tx_bytes(self, bytecount):
		self.__position += bytecount
		return self.__tx[self.__position - bytecount : self.__position]

	def __get_int_bytes(self, bytecount):
		intbytes = self.__read_tx_bytes(bytecount)
		
		if(bytecount > 1):
			intbytes = intbytes[::-1]

		num = int(binascii.hexlify(intbytes), 16)

		# #handle compactsize unsigned ints
		if(num > 252 and bytecount == 1):
			return self.__get_int_bytes(pow(2, num - 252))

		return num

	def __get_string_bytes(self, bytecount, reverse=False):
		strbytes = self.__read_tx_bytes(bytecount)

		if(reverse == True):
			strbytes = strbytes[::-1]

		return str(binascii.hexlify(strbytes))

	def __getitem__(self, item):
		return self.transaction[item]

	def __repr__(self):
		return json.dumps(self.transaction, sort_keys=True, indent=4)

if __name__ == "__main__":
	__package__ = "decoder.transaction"