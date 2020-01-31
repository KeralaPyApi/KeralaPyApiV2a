from io import BytesIO

from .primitives import Int, Long
from .tl_object import TLObject


class FutureSalt(TLObject):
    ID = 0x0949d9dc

    __slots__ = ["valid_since", "valid_until", "salt"]

    QUALNAME = "FutureSalt"

    def __init__(self, valid_since: int, valid_until: int, salt: int):
        self.valid_since = valid_since
        self.valid_until = valid_until
        self.salt = salt

    @staticmethod
    def read(b: BytesIO, *args) -> "FutureSalt":
        valid_since = Int.read(b)
        valid_until = Int.read(b)
        salt = Long.read(b)

        return FutureSalt(valid_since, valid_until, salt)
