from io import BytesIO

from .message import Message
from .primitives import Int
from .tl_object import TLObject


class MsgContainer(TLObject):
    ID = 0x73f1f8dc

    __slots__ = ["messages"]

    QUALNAME = "MsgContainer"

    def __init__(self, messages: list):
        self.messages = messages

    @staticmethod
    def read(b: BytesIO, *args) -> "MsgContainer":
        count = Int.read(b)
        return MsgContainer([Message.read(b) for _ in range(count)])

    def write(self) -> bytes:
        b = BytesIO()

        b.write(Int(self.ID, False))

        count = len(self.messages)
        b.write(Int(count))

        for message in self.messages:
            b.write(message.write())

        return b.getvalue()
