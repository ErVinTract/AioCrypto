from aiocrypto import App, Invoice, Balance, Currency, Transfer, ExchangeRate, Unauthorized, __version__
from aiocrypto.types import Hostnames, Assets

from aiohttp import ClientSession

from typing import List, Union, Optional


class CryptoApi:
    def __init__(self, token, hostname: str = Hostnames.MAIN_NET) -> None:
        """
        ### Init CryptoPay api

        * async class CryptoApi

        ### Args:
            token (str): CryptoPay api token from @CryptoBot or @CryptoTestnetBot

            hostname (str, optional): Api endpoint hostname. Defaults to Hostnames.MAIN_NET.

            delay (int, optional): Not implemented, wait for version 1.2, zero by default
        """

        self._token = token
        self._hostname = hostname
        self._client: ClientSession = ClientSession(
            base_url=self._hostname, headers={
                'Crypto-Pay-API-Token': self._token, 'user-agent': f'AioCrypto Stable {__version__}', }
        )

    def _raise(self, response: dict) -> Exception:
        """
        ### Raise api errors

        #### Args:
            response (dict): [response dict data]
        #### Returns:
            Exception: [Exception models]
        """
        if response['ok'] == False:
            if response['error']['code'] == 401:
                raise Unauthorized(
                    response['error']['code'], response['error']['name'])
            else:
                raise response

    @classmethod
    def _validate_asset(cls, asset):
        assert asset in Assets.__annotations__.keys()

    @classmethod
    def _clear_dict(cls, dict_: dict):
        return {key: value for key, value in dict_.items() if value is not None}

    async def get_me(self) -> App:
        """
        ### About

        Use this method to test your app's authentication token. Requires no parameters.
        On success, returns basic information about an app.

        Returns
        --------
            - App: object[App]
        """

        async with self._client.get(url='/api/getMe') as response:
            resp = await response.json()
            self._raise(response=resp)

            return App(**resp['result'])

    async def create_invoice(self,
                             asset: str,
                             amount: float,
                             **kwargs: Union[str, bool, int]):
        """
        ### About

        Use this method to test your app's authentication token. Requires no parameters.
        On success, returns basic information about an app.

        Params
        -------
            - asset (String): Supported assets: “BTC”, “TON”, “ETH”, “USDT”, “USDC”.
            - amount (Float)
            - description (String): Optional. Description for the invoice. User will see this description when they pay the invoice. Up to 1024 characters.
            - hidden_message (String): Optional. Text of the message that will be shown to a user after the invoice is paid. Up to 2048 characters.

            - paid_btn_name (String): Optional. Name of the button that will be shown to a user after the invoice is paid.
                - Supported names: 
                1. viewItem – “View Item”
                2. openChannel – “View Channel”
                3. openBot – “Open Bot”
                4. callback – “Return”

            - paid_btn_url (String): Optional. Required if paid_btn_name is used.URL to be opened when the button is pressed. You can set any success link (for example, a link to your bot). Starts with https or http.
            - payload (String): Optional. Any data you want to attach to the invoice (for example, user ID, payment ID, ect). Up to 4kb.
            - allow_comments (Boolean): Optional. Allow a user to add a comment to the payment. Default is true.
            - allow_anonymous (Boolean): Optional. Allow a user to pay the invoice anonymously. Default is true.
            - expires_in (Number): Optional. You can set a payment time limit for the invoice in seconds. Values between 1-2678400 are accepted.


        Returns
        --------
            - Invoice: dict
        """

        data = {
            k: v for k, v in kwargs.items()
        }

        data['asset'] = asset
        data['amount'] = amount

        async with self._client.get(url="/api/createInvoice", data=data) as response:
            resp = await response.json()
            self._raise(response=resp)

            return resp['result']

    async def transfer(self, user_id: int, asset: str, amount: Union[float, str], spend_id: str, **kwargs) -> Transfer:
        """
        ### About

        Use this method to send your coins to other users.
          If successful, returns information about the given translation.

        Params
        -------
            - user_id (Number): Telegram user ID. User must have previously used @CryptoBot (@CryptoTestnetBot for testnet).
            - asset (String): Currency code. Supported assets: “BTC”, “TON”, “ETH”, “USDT”, “USDC”.
            - amount (String): Amount of the transfer in float. The minimum and maximum amounts for each of the support asset roughly correspond to the limit of 1-25000 USD. Use getExchangeRates to convert amounts. For example: 125.50
            - spend_id (String): Unique ID to make your request idempotent and ensure that only one of the transfers with the same spend_id is accepted from your app. This parameter is useful when the transfer should be retried (i.e. request timeout, connection reset, 500 HTTP status, etc). Up to 64 symbols.
            - comment (String): Optional. Comment for the transfer. Users will see this comment when they receive a notification about the transfer. Up to 1024 symbols.
            - disable_send_notification (Boolean): Optional. Pass true if the user should not receive a notification about the transfer.Default is false.


        Returns
        --------
            - Transfer: object[Transfer]
        """

        data = {
            k: v for k, v in kwargs.items()
        }

        data['user_id'] = user_id
        data['asset'] = asset
        data['amount'] = amount
        data['spend_id'] = spend_id

        async with self._client.post(url='/api/transfer', data=data) as response:
            resp = await response.json()

    async def get_balance(self) -> List[Balance]:
        """
        ### About

        Use this method to check your balance. Requires no parameters.
            If successful, returns information about the balance of the connected application.
            - Supported assets: “BTC”, “TON”, “ETH”, “USDT”, “USDC” and “BUSD”.

        Returns
        --------
            - list[Balance]: Balance list object
        """

        async with self._client.get(url='/api/getBalance') as response:
            resp = await response.json()
            self._raise(response=resp)

            return [Balance(**balance) for balance in resp['result']]

    async def get_invoices(
            self,
            asset: Optional[str] = None,
            invoice_ids: Optional[List[Union[str, int]]] = None,
            status: Optional[str] = None,
            offset: Optional[int] = None,
            count: Optional[int] = None
    ) -> List[Invoice]:
        """
        ### About

        Use this method to view active invoices.
            If successful, returns a sheet with information about all specified invoices.

        Returns
        --------
            - list[Invoice]: Invoice list object

        """
        if asset is not None:
            self._validate_asset(asset)

        if invoice_ids is not None:
            invoice_ids = ",".join(map(str, invoice_ids))

        params = {"asset": asset, "invoice_ids": invoice_ids, "status": status, "offset": offset, "count": count}
        async with self._client.get(url='/api/getInvoices', params=self._clear_dict(params)) as response:
            resp = await response.json()
            self._raise(response=resp)

            return [Invoice(**invoice) for invoice in resp['result']['items']]

    async def get_exchange_rates(self) -> List[ExchangeRate]:
        """

        ### About

        Use this method to get exchange rates of supported currencies. Returns array of currencies.

        Returns:
        --------
            - List[ExchangeRate]: ExchangeRate list object
        """
        async with self._client.get(url='/api/getExchangeRates') as response:
            resp = await response.json()
            self._raise(response=resp)

            return [ExchangeRate(**rate) for rate in resp['result']]

    async def get_currencies(self) -> List[Currency]:
        """
        ### About

        Use this method to get a list of supported currencies. Returns array of currencies.


        Returns:
        --------
            - List[Currency]: Currency list object
        """

        async with self._client.get(url='/api/getCurrencies') as response:
            resp = await response.json()
            self._raise(response=resp)

            return [Currency(**currency) for currency in resp['result']]

    async def close(self) -> str:
        """
        ### Close client session
        """
        await self._client.close()
        return "Success!"
