from io import BytesIO

from . import Int
from ..list import List
from ..tl_object import TLObject


class Vector(TLObject):
    ID = 0x1cb5c415

    # Method added to handle the special case when a query returns a bare Vector (of Ints);
    # i.e., RpcResult body starts with 0x1cb5c415 (Vector Id) - e.g., messages.GetMessagesViews.
    @staticmethod
    def _read(b: BytesIO) -> TLObject or int:
        try:
            return TLObject.read(b)
        except KeyError:
            b.seek(-4, 1)
            return Int.read(b)

    @staticmethod
    def read(b: BytesIO, t: TLObject = None) -> list:
        return List(
            t.read(b) if t
            else Vector._read(b)
            for _ in range(Int.read(b))
        )

    def __new__(cls, value: list, t: TLObject = None) -> bytes:
        return b"".join(
            [Int(cls.ID, False), Int(len(value))]
            + [
                t(i) if t
                else i.write()
                for i in value
            ]
        )
