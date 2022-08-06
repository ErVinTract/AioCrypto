# PyCoingate

[![Telegram Crypto](https://img.shields.io/badge/telegram-ErVinTract-blue.svg?style=flat)](https://t.me/ErVinTract)
[![PyPi Package Version](https://img.shields.io/pypi/v/aiocrypto.svg?style=flat)](https://pypi.python.org/pypi/AioCrypto)
[![Downloads](https://img.shields.io/pypi/dm/aiocrypto.svg?style=flat)](https://pypi.python.org/pypi/pycoingate)
[![Supported python versions](https://img.shields.io/pypi/pyversions/aiocrypto.svg?style=flat)](https://pypi.python.org/pypi/aiocrypto)
[![Crypto API](https://img.shields.io/badge/AioCrypto-1.1.1-green.svg?style=flat)](https://developer.coingate.com/v2/docs/)
[![Github issues](https://img.shields.io/github/issues/ErVinTract/AioCrypto.svg?style=flat-square)](https://github.com/ErVinTracst/PyCoingate/issues)
[![MIT License](https://img.shields.io/pypi/l/aiocrypto.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)

**AioCrypto** is a fairly simple and convenient library for working with the [Crypto API](https://help.crypt.bot/crypto-pay-api), written in Python 3.8 with [asyncio](https://docs.python.org/3/library/asyncio.html) and [aiohttp](https://github.com/aio-libs/aiohttp).

## Examples

<details>
  <summary>📚 Click to see some basic examples</summary>
 
**Few steps before getting started...**

- Install latest stable version of pycoingate, simply running `pip install AioCrypto`
    
###  - Get me

```python
from aiocrypto import CryptoApi

async def main():
    app = CryptoApi(token='12345:AaSvhiRsAHazxVB91KIB1dwia0OkmN')
    print(await app.get_me()) # App(app_id=12345, name='Magni..

```

###  - Get Balance

```python
from aiocrypto import CryptoApi

async def main():
    app = CryptoApi(token='12345:AaSvhiRsAHazxVB91KIB1dwia0OkmN')
    balances = await app.get_balance()
    print(balances) # List[Balance(...), Balance(...)]
    # print(balances[0]) Balance(currency_code='BTC', available=1.027)

```

### - Create Invoice 

```
from aiocrypto import CryptoApi

async def main():
    app = CryptoApi(token='12345:AaSvhiRsAHazxVB91KIB1dwia0OkmN')
    invoice = await app.create_invoice(asset="ETH", amount="0.023")
    print(invoice) 
    # {'invoice_id': 229875, 'status': 'active', ...}
```

### Moar!

You can find more examples in [`examples/`](https://github.com/ErVinTract/AioCrypto/tree/main/examples) directory

</details>

## Official AioCrypto resources

- News: [@CryptoBotRu](https://t.me/CryptoBotRU)
- Community: [@CryptoBotRussian](https://t.me/CryptoBotRussian)
- Pip: [AioCrypto](https://pypi.python.org/pypi/AioCrypto)
- Source: [Github repo](https://github.com/ErVinTract/AioCrypto)
- Issues/Bug tracker: [Github issues tracker](https://github.com/ErVinTract/AioCrypto/issues>)
