import requests
import json

# https://www.blockchain.com/api/blockchain_api

blockHashes = [ "0000000000000000000645da8ea481c958806d085b0be52e9ffc283c112e461d",
    "00000000000000000004a0a3a171d8889f2cc1ae05388c9fbcc10f7a7d7d8c00",
    "00000000000000000004ee9b714567db822de029a95426e26f4fe394868d94b3",
    "00000000000000000008c5ec257ca79da66806c6c6e5a306d9fe3ae379db7f57",
    "00000000000000000000015f70803f4a8fde073d699b6f8bd458a8f10d9a48cd",
    "000000000000000000026ce50efd0d2a0c88d7bde4af76c92a599176e4eecba4",
    "0000000000000000000685f068595dcc93d9032d70f276a63499e19702e15e36",
    "00000000000000000006ed3973188b89b5aeaeb316af07a9b0a3934cbfe768ab",
    "00000000000000000002cabb255f8d98ccabfb6d6c055dd2fa0251c0d9f9cec9",
    "00000000000000000003c289f11a9d1df3772cd4961ca8b4fcb05898e5d855f1" ]

class scrape:

    def __init__(self):
        self.blocks()

    def blocks(self):
        blockRequests = []
        for hash in blockHashes:
            blockRequests.append("https://blockchain.info/rawblock/" + hash)

        blockJsons = []
        for blockURL in blockRequests:
            blockJsons.appen(requests.get(blockURL).content)

scrape()
