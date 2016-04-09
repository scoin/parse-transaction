# parse-transaction

###Dependencies
Python 2.7.x

###Usage:

```bash
$ python decoderawrtransaction.py <hexdata>
```

###Example

```bash
$python decoderawtransaction.py 0100000001763b0b38e91d90a75fde6425be72285e73e81f072f321d574b59b744fd771f6b000000006a47304402202bb8b61244ee0ebc2f6d00f563a35aa7e5afc1727446086e45259c1fb00d194702201020df0479220ca6dadaffd82ab8f4a4c9fe8ed99b6c6d6c71678f2a582b0d65012103010f2163599d3dd737e1347b54bf836fdd7bcb5dbe15787aee5b70f48ecd9abdffffffff0180602400000000001976a9147a4f98ac48bf70308ed7731ce97a539a01d4209388ac00000000
```

```json
{
    "locktime": 0, 
    "num_inputs": 1, 
    "num_outputs": 1, 
    "txid": "d3d58c08e0390b354674b209957389953800ed607faae02119a2522ce44e81e9", 
    "version": 1, 
    "vin": [
        {
            "scriptSig": "47304402202bb8b61244ee0ebc2f6d00f563a35aa7e5afc1727446086e45259c1fb00d194702201020df0479220ca6dadaffd82ab8f4a4c9fe8ed99b6c6d6c71678f2a582b0d65012103010f2163599d3dd737e1347b54bf836fdd7bcb5dbe15787aee5b70f48ecd9abd", 
            "sequence": "ffffffff", 
            "txid": "6b1f77fd44b7594b571d322f071fe8735e2872be2564de5fa7901de9380b3b76", 
            "vout": 0
        }
    ], 
    "vout": [
        {
            "n": 0, 
            "qty": 2384000, 
            "script": "76a9147a4f98ac48bf70308ed7731ce97a539a01d4209388ac"
        }
    ]
}
```

To run the tests:

```
$ python test.py
```
