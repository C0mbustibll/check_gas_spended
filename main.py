from config import *
from web3 import Web3
from web3.eth import AsyncEth
from web3.geth import Geth, AsyncGethTxPool
from loguru import logger
import asyncio
import aiohttp
from itertools import zip_longest

logger.add('log.log')

web3 = Web3(Web3.AsyncHTTPProvider('https://rpc.ankr.com/optimism'),
            modules={'eth': (AsyncEth,), 'geth': (Geth, {'txpool': (AsyncGethTxPool,)})}, middlewares=[])

async def check_tx(tx):
    return (await web3.eth.get_transaction_receipt(tx))['l1Fee']

async def gas(address, api_url, list_tx):
    list_t = [tx for tx in list_tx['result'] if tx['from'].lower() == address.lower()]
    gas_used = 0
    if api_url == 'https://api-optimistic.etherscan.io/':
        tx_gas = await asyncio.gather(*[check_tx(tx["hash"]) for tx in list_t])
        for i in tx_gas:
            gas_used += (int(i, 16) / 10 ** 18)
        for i in list_t:
            gas_used += (float(i['gasPrice']) * float(i['gasUsed'])) / 10 ** 18
    else:
        for i in list_t:
            gas_used += (float(i['gasPrice']) * float(i['gasUsed'])) / 10 ** 18
    if VIEW == 1:
        logger.info(f'{chain_dict[api_url]} {address} ${coin_dict[api_url]}  {"{:.12f}".format(gas_used)}')
    return gas_used


async def request_tx(address, api_url):
    while True:
        try:
            async with aiohttp.ClientSession() as ses:
                async with ses.get(
                        f'{api_url}api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey={key_dict[api_url]}') as r:
                    ls = await r.json()
                    return await gas(address, api_url, ls)
        except Exception as e:
            # logger.error(e)
            await asyncio.sleep(1)


with open('address.txt', 'r') as f:
    address_list = [i for i in [i.strip() for i in f] if i != '']

async def work(url):
    global_gas = 0
    for address in zip_longest(*([iter(address_list)] * streams)):
        gas = await asyncio.gather(*[request_tx(add, url) for add in address if add != None])
        for g in gas:
            if g != None:
                global_gas += float(g)
    logger.success(f'{chain_dict[url]} ${coin_dict[url]} {"{:.12f}".format(global_gas)}')

async def main():
    await asyncio.gather(*[work(url) for url in scan_url])

asyncio.run(main())
