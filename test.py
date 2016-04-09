import unittest
from decoder.transaction import TransactionDecoder


class TestTransactionDecoder(unittest.TestCase):

    def test_tx_single_input_single_output(self):
        hexstring = "01000000014d1757c30ad86d44a9e9eb576452c7d4b743825e6b76b2c43b45932410e75426000000008a47304402200411331fa3626502aaf0085569c449ffee97e52de4d0eedac7e528c562ddacaf0220453f1a8ad19c2c753e3a9319ab4b4cc57d7cde661feb49a13676faab4d4edbcb0141046e29695ce112ee28b00341e7e3ad5a6286f3bd13d9fb81bcd65af4ded09d98be0ce5f058428429aea0c7574b9cd218a031ab2b146f35fc0fc50bcdd6158dd406ffffffff01b8880000000000001976a914dda066bc83b2a8a5a663a97dd2d910e94e457f7988ac00000000"
        expected = {
            "locktime": 0,
            "num_inputs": 1,
            "num_outputs": 1,
            "txid": "e30cba14b82fdc75d284a9325e7553aa007bf5681c71bcf4c5dbdb739cd12607",
            "version": 1,
            "vin": [
                {
                    "scriptSig": "47304402200411331fa3626502aaf0085569c449ffee97e52de4d0eedac7e528c562ddacaf0220453f1a8ad19c2c753e3a9319ab4b4cc57d7cde661feb49a13676faab4d4edbcb0141046e29695ce112ee28b00341e7e3ad5a6286f3bd13d9fb81bcd65af4ded09d98be0ce5f058428429aea0c7574b9cd218a031ab2b146f35fc0fc50bcdd6158dd406",
                    "sequence": "ffffffff",
                    "txid": "2654e7102493453bc4b2766b5e8243b7d4c7526457ebe9a9446dd80ac357174d",
                    "vout": 0
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "qty": 35000,
                    "script": "76a914dda066bc83b2a8a5a663a97dd2d910e94e457f7988ac"
                }
            ]
        }
        tx = TransactionDecoder(hexstring)
        self.assertEqual(expected, tx.transaction)

    def test_tx_single_input_multiple_outputs(self):
        hexstring = "010000000115f2e4ef237e642b068e0edce85d6b4c20645461b9c47559a8e60e8d7659ea4f080000006a473044022025a74c8d09ef0062af4d03f7ba0b9edd722d94460687b56d6a025eb6012cbe13022008d07a40e8a6be3b0851ec37ae17455a9b202bf7f2335352428bc4a6126cbd56012103e12317b55cfac609abda17c9c547585c206cbca55f2032b9b1552d2b792ec0cdffffffff02383b0000000000001976a9148fdd1ec175956912f89237300aad94766ab47a7c88ac7863eb0b000000001976a914f3e48b3d3682b3765764894002669403acb2edc088ac00000000"
        expected = {
            "locktime": 0,
            "num_inputs": 1,
            "num_outputs": 2,
            "txid": "7e0d67b69882256857176d561a497546b1f952d92c5af780c0eb03888195b56d",
            "version": 1,
            "vin": [
                {
                    "scriptSig": "473044022025a74c8d09ef0062af4d03f7ba0b9edd722d94460687b56d6a025eb6012cbe13022008d07a40e8a6be3b0851ec37ae17455a9b202bf7f2335352428bc4a6126cbd56012103e12317b55cfac609abda17c9c547585c206cbca55f2032b9b1552d2b792ec0cd",
                    "sequence": "ffffffff",
                    "txid": "4fea59768d0ee6a85975c4b9615464204c6b5de8dc0e8e062b647e23efe4f215",
                    "vout": 8
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "qty": 15160,
                    "script": "76a9148fdd1ec175956912f89237300aad94766ab47a7c88ac"
                },
                {
                    "n": 1,
                    "qty": 199975800,
                    "script": "76a914f3e48b3d3682b3765764894002669403acb2edc088ac"
                }
            ]
        }
        tx = TransactionDecoder(hexstring)
        self.assertEqual(expected, tx.transaction)

    def test_tx_multiple_inputs_outputs(self):
        hexstring = "01000000038819521ac06094b54979d4431eb5e8357fc8cb328807dc3d8e019a6d5c148103010000006a47304402202e39e0d7ce5db1685e4dc38b59471c90c4a1d90b01d71ad3b495620f50296acf022054e20e88312d14a6d803ad8773187d4d47bf4319ef45de4b44212880cb4974c7012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5ffffffffe55b6f965cab250aa3c144901ab9740fd2726c9d91cbb58f5e04029df3fdea36000000006a4730440220071dbb1468be8770ed528687439f0c262660509d7e9de59ad3bc1a437fce1a2802202f7184c2cc5585ddf7c090c6e1a3f9849af4f5822c51a35b6cea4863259c7856012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5ffffffff68b0f397108d79aa84eeafe54db72f9b7f56359998572195ac22b3db4cb978bb000000006b483045022100e9f6852da20b07aadea26acd15bb49c26976446fe690b37fd480ae0ef1b5f67f022005f9f98a4fb539edc880c32409b4bf838b0342844613f6b2a23633fd595753fe012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5ffffffff02c2190000000000001976a91498a831b2f9b5b1806a4efb94336c6a441bc2847b88acea562600000000001976a9143214d00ee0bd49df1e80c24d9c11b4271d01143988ac00000000"
        expected = {
            "locktime": 0,
            "num_inputs": 3,
            "num_outputs": 2,
            "txid": "77f611bb7365cff7420b6b3a6bcecfa60ff4b727270cc750ad99a19041d27334",
            "version": 1,
            "vin": [
                {
                    "scriptSig": "47304402202e39e0d7ce5db1685e4dc38b59471c90c4a1d90b01d71ad3b495620f50296acf022054e20e88312d14a6d803ad8773187d4d47bf4319ef45de4b44212880cb4974c7012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5",
                    "sequence": "ffffffff",
                    "txid": "0381145c6d9a018e3ddc078832cbc87f35e8b51e43d47949b59460c01a521988",
                    "vout": 1
                },
                {
                    "scriptSig": "4730440220071dbb1468be8770ed528687439f0c262660509d7e9de59ad3bc1a437fce1a2802202f7184c2cc5585ddf7c090c6e1a3f9849af4f5822c51a35b6cea4863259c7856012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5",
                    "sequence": "ffffffff",
                    "txid": "36eafdf39d02045e8fb5cb919d6c72d20f74b91a9044c1a30a25ab5c966f5be5",
                    "vout": 0
                },
                {
                    "scriptSig": "483045022100e9f6852da20b07aadea26acd15bb49c26976446fe690b37fd480ae0ef1b5f67f022005f9f98a4fb539edc880c32409b4bf838b0342844613f6b2a23633fd595753fe012102fa79d041ef408594023bf47109529500a4c0474aa8b4ed49cbbf2d93266a3dc5",
                    "sequence": "ffffffff",
                    "txid": "bb78b94cdbb322ac952157989935567f9b2fb74de5afee84aa798d1097f3b068",
                    "vout": 0
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "qty": 6594,
                    "script": "76a91498a831b2f9b5b1806a4efb94336c6a441bc2847b88ac"
                },
                {
                    "n": 1,
                    "qty": 2512618,
                    "script": "76a9143214d00ee0bd49df1e80c24d9c11b4271d01143988ac"
                }
            ]
        }
        tx = TransactionDecoder(hexstring)
        self.assertEqual(expected, tx.transaction)

    def test_tx_with_compactsize_integer_encoding(self):
        hexstring = "0100000001749a67ab28ceef64e7cbaa04b62e8b692a3dee88c10df316030d13fe370ece9501000000fdfd00004830450221008cc69b42f5ebeb458a9aa0a29b2b6830ead97c8ec072a17a2fb1b57d71dd34c4022023b21a5742f5f379bd1471a7f46c96e35e2d31fab79c23b40e456768f8f81fa00147304402207c3a3741c26fe352fd429266bee6008ba8ec12d8f54fd6db51c17367536c11bf0220208c4c6c18c60a8577079b692df329ee9d7895635b18f9a7bb278df86eaf8ddb014c695221025d2d58b97da897e4a18c97f09358b9cb27710fdd3894ac3bc8eec07f39d4eb792103c0bf5248ce46235812384f9ecd5ea15bc4249ebf7ac3382dee9629855f32a22b21021ab21f8c39f027776a45a971599bbcdd11c984c6f940a9388f5cbc24cb763c0b53aeffffffff086f9923000000000017a914ee6da86812f2e7fe3d0e006eb633d43ff5f310b787141124200000000017a914c2f577c08fba8117c368b3baf3800c9481135a6d87cf679d000000000017a9145915dec107f14a7fdda323cc9be1628ddedf48f987f0a297000000000017a9144f93ed14d53f7cf41544b6644bda66f8fe849dd687e014eb1f000000001976a914305617b07ab7e20f57e80c59c9f713669e1b27c088acb2c8dc1c0000000017a9146e2257e0b473d383d326e25eb30f6b9c2a6ca47887e66898000000000017a9147ea9db321ff62cf77980ad4073cdb22ea283e1e1877e6558180000000017a914ee3c9ced95be865901e45e6e6628ff68fc32dffc8700000000"
        expected = {
            "locktime": 0,
            "num_inputs": 1,
            "num_outputs": 8,
            "txid": "5d7debb9bf688616cddeb765a7566f5bdf6d7621e3af07470de0dd27666d3a29",
            "version": 1,
            "vin": [
                {
                    "scriptSig": "004830450221008cc69b42f5ebeb458a9aa0a29b2b6830ead97c8ec072a17a2fb1b57d71dd34c4022023b21a5742f5f379bd1471a7f46c96e35e2d31fab79c23b40e456768f8f81fa00147304402207c3a3741c26fe352fd429266bee6008ba8ec12d8f54fd6db51c17367536c11bf0220208c4c6c18c60a8577079b692df329ee9d7895635b18f9a7bb278df86eaf8ddb014c695221025d2d58b97da897e4a18c97f09358b9cb27710fdd3894ac3bc8eec07f39d4eb792103c0bf5248ce46235812384f9ecd5ea15bc4249ebf7ac3382dee9629855f32a22b21021ab21f8c39f027776a45a971599bbcdd11c984c6f940a9388f5cbc24cb763c0b53ae",
                    "sequence": "ffffffff",
                    "txid": "95ce0e37fe130d0316f30dc188ee3d2a698b2eb604aacbe764efce28ab679a74",
                    "vout": 1
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "qty": 2333039,
                    "script": "a914ee6da86812f2e7fe3d0e006eb633d43ff5f310b787"
                },
                {
                    "n": 1,
                    "qty": 539234580,
                    "script": "a914c2f577c08fba8117c368b3baf3800c9481135a6d87"
                },
                {
                    "n": 2,
                    "qty": 10315727,
                    "script": "a9145915dec107f14a7fdda323cc9be1628ddedf48f987"
                },
                {
                    "n": 3,
                    "qty": 9937648,
                    "script": "a9144f93ed14d53f7cf41544b6644bda66f8fe849dd687"
                },
                {
                    "n": 4,
                    "qty": 535500000,
                    "script": "76a914305617b07ab7e20f57e80c59c9f713669e1b27c088ac"
                },
                {
                    "n": 5,
                    "qty": 484231346,
                    "script": "a9146e2257e0b473d383d326e25eb30f6b9c2a6ca47887"
                },
                {
                    "n": 6,
                    "qty": 9988326,
                    "script": "a9147ea9db321ff62cf77980ad4073cdb22ea283e1e187"
                },
                {
                    "n": 7,
                    "qty": 408446334,
                    "script": "a914ee3c9ced95be865901e45e6e6628ff68fc32dffc87"
                }
            ]
        }
        tx = TransactionDecoder(hexstring)
        self.assertEqual(expected, tx.transaction)

    def test_tx_with_op_return_output(self):
        hexstring = "010000000150670d0ab5aa462029da03f188c915105b19112b8478f797b81382a20f9eb622470000008a47304402201c5541112f0c0f0cad4ed168fb96806c893746259bcda292219f9fa7674a16220220389330bba914a43c3242f0598a2bf3aa0862e3bdf0bb3c15e48e598fc4127f03014104bd184b34e4e20698a7670854e16f68c4ca2f9326572342998bdf1b1c4685644c2374e40c19ca20eeb3439e3255d468d3e92aa32f577df99bdb409c8f064462f7ffffffff0100000000000000002a6a28444f4350524f4f4607559fae135abe5981f0d32fe6f5b6efe45e071b6f9910e0e596f266a291d8f900000000"
        expected = {
            "locktime": 0,
            "num_inputs": 1,
            "num_outputs": 1,
            "txid": "431ee17ef964f556c305a84103f15fa23eadb9d22ed851e49824a64b46932fff",
            "version": 1,
            "vin": [
                {
                    "scriptSig": "47304402201c5541112f0c0f0cad4ed168fb96806c893746259bcda292219f9fa7674a16220220389330bba914a43c3242f0598a2bf3aa0862e3bdf0bb3c15e48e598fc4127f03014104bd184b34e4e20698a7670854e16f68c4ca2f9326572342998bdf1b1c4685644c2374e40c19ca20eeb3439e3255d468d3e92aa32f577df99bdb409c8f064462f7",
                    "sequence": "ffffffff",
                    "txid": "22b69e0fa28213b897f778842b11195b1015c988f103da292046aab50a0d6750",
                    "vout": 71
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "qty": 0,
                    "script": "6a28444f4350524f4f4607559fae135abe5981f0d32fe6f5b6efe45e071b6f9910e0e596f266a291d8f9"
                }
            ]
        }
        tx = TransactionDecoder(hexstring)
        self.assertEqual(expected, tx.transaction)


if __name__ == '__main__':
    unittest.main()
