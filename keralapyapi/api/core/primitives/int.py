from io import BytesIO

from ..tl_object import TLObject


class Int(TLObject):
    SIZE = 4

    @classmethod
    def read(cls, b: BytesIO, signed: bool = True) -> int:
        return int.from_bytes(b.read(cls.SIZE), "little", signed=signed)

    def __new__(cls, value: int, signed: bool = True) -> bytes:
        return value.to_bytes(cls.SIZE, "little", signed=signed)


class Long(Int):
    SIZE = 8


class Int128(Int):
    SIZE = 16


class Int256(Int):
    SIZE = 32
