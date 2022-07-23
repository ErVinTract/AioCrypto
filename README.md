### About

AioCrypto is a library for working with the Crypto Bot API.

### Quickstartw

1. Install:

```bash
pip install AioCrypto
```

2. See Examples

### Usage

```python

from aiocrypto import CryptoApi

async def main():

    app = CryptoApi(token='12345:AaSvhiRsAHazxVB91KIB1dwia0OkmN')
    balances = await app.get_balance()
    print(balances) # List[Balance(...), Balance(...)]
    # or 
    # print(balances[0]) object[Balance]

```

More realistic example:

```python

async def main():

    app = CryptoApi(token='12345:AaSvhiRsAHazxVB91KIB1dwia0OkmN')
    me = await app.get_me()
    print(me) # object Me(...)



```
