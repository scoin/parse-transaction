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

        self.transaction["vin"] = [self.__parse_inputs(n) for n in range(self.transaction["num_inputs"])]

        self.transaction["num_outputs"] = self.__get_int_bytes(1)

        self.transaction["vout"] = [self.__parse_outputs(n) for n in range(self.transaction["num_outputs"])]            

        self.transaction["locktime"] = self.__get_int_bytes(4)

    @staticmethod
    def get_txid(hexstring):
        return sha256(sha256(hexstring.decode('hex_codec')).digest()).digest()[::-1].encode('hex_codec')

    def __read_tx_bytes(self, bytecount):
        self.__position += bytecount
        return self.__tx[(self.__position - bytecount): self.__position]

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

        if(reverse is True):
            strbytes = strbytes[::-1]

        return str(binascii.hexlify(strbytes))

    def __parse_inputs(self, n):
        input_dict ={
            "txid": self.__get_string_bytes(32, reverse=True),
            "vout": self.__get_int_bytes(4)
        }
        input_bytes = self.__get_int_bytes(1)
        input_dict["scriptSig"] = self.__get_string_bytes(input_bytes)
        input_dict["sequence"] = self.__get_string_bytes(4)
        return input_dict

    def __parse_outputs(self, n):
        output_dict = {
            "qty": self.__get_int_bytes(8),
            "n": n
        }
        output_bytes = self.__get_int_bytes(1)
        output_dict["script"] = self.__get_string_bytes(output_bytes)
        return output_dict


    def __getitem__(self, item):
        return self.transaction[item]

    def __repr__(self):
        return json.dumps(self.transaction, sort_keys=True, indent=4)

if __name__ == "__main__":
    __package__ = "decoder.transaction"
