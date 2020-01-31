from io import BytesIO

from ..tl_object import TLObject


class BoolFalse(TLObject):
    ID = 0xbc799737
    value = False

    @classmethod
    def read(cls, *args) -> bool:
        return cls.value

    def __new__(cls) -> bytes:
        return cls.ID.to_bytes(4, "little")


class BoolTrue(BoolFalse):
    ID = 0x997275b5
    value = True


class Bool(TLObject):
    @classmethod
    def read(cls, b: BytesIO) -> bool:
        return int.from_bytes(b.read(4), "little") == BoolTrue.ID

    def __new__(cls, value: bool) -> BoolTrue or BoolFalse:
        return BoolTrue() if value else BoolFalse()
