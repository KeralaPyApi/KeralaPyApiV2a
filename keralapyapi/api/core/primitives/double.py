from io import BytesIO
from struct import unpack, pack

from ..tl_object import TLObject


class Double(TLObject):
    @staticmethod
    def read(b: BytesIO, *args) -> float:
        return unpack("d", b.read(8))[0]

    def __new__(cls, value: float) -> bytes:
        return pack("d", value)
