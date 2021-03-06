from dataclasses import dataclass


@dataclass
class OrderInfo:
    order_id: int
    user_name: str
    shipping_email: str
    consumer_email: str


@dataclass
class SendEmailParams:
    to: str
    sender: str
    content: str
    subject: str
