from io import BytesIO

from . import FutureSalt
from .primitives import Int, Long
from .tl_object import TLObject


class FutureSalts(TLObject):
    ID = 0xae500895

    __slots__ = ["req_msg_id", "now", "salts"]

    QUALNAME = "FutureSalts"

    def __init__(self, req_msg_id: int, now: int, salts: list):
        self.req_msg_id = req_msg_id
        self.now = now
        self.salts = salts

    @staticmethod
    def read(b: BytesIO, *args) -> "FutureSalts":
        req_msg_id = Long.read(b)
        now = Int.read(b)

        count = Int.read(b)
        salts = [FutureSalt.read(b) for _ in range(count)]

        return FutureSalts(req_msg_id, now, salts)
