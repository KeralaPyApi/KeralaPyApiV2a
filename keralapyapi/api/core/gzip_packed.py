from gzip import compress, decompress
from io import BytesIO

from .primitives import Int, Bytes
from .tl_object import TLObject


class GzipPacked(TLObject):
    ID = 0x3072cfa1

    __slots__ = ["packed_data"]

    QUALNAME = "GzipPacked"

    def __init__(self, packed_data: TLObject):
        self.packed_data = packed_data

    @staticmethod
    def read(b: BytesIO, *args) -> "GzipPacked":
        # Return the Object itself instead of a GzipPacked wrapping it
        return TLObject.read(
            BytesIO(
                decompress(
                    Bytes.read(b)
                )
            )
        )

    def write(self) -> bytes:
        b = BytesIO()

        b.write(Int(self.ID, False))

        b.write(
            Bytes(
                compress(
                    self.packed_data.write()
                )
            )
        )

        return b.getvalue()
