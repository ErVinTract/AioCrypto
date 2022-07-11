from dataclasses import dataclass
from typing import Optional


@dataclass
class Assets:
    BTC: str = 'BTC'
    TON: str = 'TON'
    ETH: str = 'ETH'
    USDT: str = 'USDT'
    USDC: str = 'USDC'
    BUSD: str = 'BUSD'


@dataclass
class Balance:
    currency_code: str
    available: float

    def __post_init__(self) -> None:
        self.available = float(self.available)


@dataclass
class Invoice:
    """
    ## Invoice

    Parameters
    ----------
    * invoice_id       - Unique ID for this invoice. 
    * status           - Status of the invoice, can be either “active”, “paid” or “expired”.
    * hash             - Hash of the invoice.
    * asset            - Currency code. Currently, can be “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” or “BUSD”.
    * amount           - Amount of the invoice.
    * pay_url          - URL should be presented to the user to pay the invoice.
    * description      - Optional. Description for this invoice.
    * created_at       - Date the invoice was created in ISO 8601 format. 
    * allow_comments   - True, if the user can add comment to the payment.
    * allow_anonymous  - True, if the user can pay the invoice anonymously.
    * expiration_date  - Optional. Date the invoice expires in Unix time.
    * paid_at          - Optional. Date the invoice was paid in Unix time. 
    * paid_anonymously - True, if the invoice was paid anonymously.
    * comment          - Optional. Comment to the payment from the user.
    * hidden_message   - Optional. Text of the hidden message for this invoice.
    * payload          - Optional. Previously provided data for this invoice.
    * paid_btn_name    - Optional. Name of the button, can be “viewItem”, “openChannel”, “openChannel” or “callback”.
    * paid_btn_url     - Optional. URL of the button.

    """
    invoice_id: int
    status: int
    hash: str
    asset: str
    amount: str
    pay_url: str
    Uescription: str
    created_at: str
    allow_comments: bool
    allow_anonymous: bool
    expiration_date: str
    paid_at: str
    paid_anonymously: bool
    comment: str
    hidden_message: str
    payload: str
    paid_btn_name: str
    paid_btn_url: str


@dataclass
class Transfer:
    """
    ## Transfer

    Parameters
    ----------
    * transfer_id  - Unique ID for this transfer.
    * user_id:     - Telegram user ID the transfer was sent to.
    * asset        - Currency code. Currently, can be “BTC”, “TON”, “ETH” (testnet only), “USDT”, “USDC” or “BUSD”.
    * amount       - Amount of the transfer.
    * status       - Status of the transfer, can be “completed”.
    * completed_at - Date the transfer was completed in ISO 8601 format.
    * comment      - Optional. Comment for this transfer.

    """
    transfer_id: int
    user_id: int
    asset: str
    amount: str
    status: str
    completed_at: str
    comment: str


@dataclass
class ExchangeRate:
    is_valid: bool
    source: str
    target: str
    rate: float

    def __post_init__(self) -> None:
        self.rate = float(self.rate)


@dataclass
class Currency:
    is_blockchain: bool
    is_stablecoin: bool
    is_fiat: bool
    name: str
    code: str
    decimals: int
    url: Optional[str] = None


@dataclass
class PaidButtonNames:
    VIEW_ITEM: str = 'viewItem',
    OPEN_CHANNEL: str = 'openChannel',
    OPEN_BOT: str = 'openBot',
    CALLBACK: str = 'callback'


@dataclass
class Hostnames:
    MAIN_NET: str = 'https://pay.crypt.bot'
    TEST_NET: str = 'https://testnet-pay.crypt.bot'


@dataclass
class InvoiceStatus:
    active: str = 'active'
    paid: str = 'paid'


@dataclass
class App:
    app_id: int
    name: str
    payment_processing_bot_username: str
