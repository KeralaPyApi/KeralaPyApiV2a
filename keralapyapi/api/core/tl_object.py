from collections import OrderedDict
from io import BytesIO
from json import dumps

from ..all import objects


class TLObject:
    __slots__ = []

    QUALNAME = "Base"

    @staticmethod
    def read(b: BytesIO, *args):  # TODO: Rename b -> data
        return objects[int.from_bytes(b.read(4), "little")].read(b, *args)

    def write(self, *args) -> bytes:
        pass

    @staticmethod
    def default(obj: "TLObject"):
        if isinstance(obj, bytes):
            return repr(obj)

        return OrderedDict(
            [("_", obj.QUALNAME)]
            + [
                (attr, getattr(obj, attr))
                for attr in obj.__slots__
                if getattr(obj, attr) is not None
            ]
        )

    def __str__(self) -> str:
        return dumps(self, indent=4, default=TLObject.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "keralapyapi.api.{}({})".format(
            self.QUALNAME,
            ", ".join(
                "{}={}".format(attr, repr(getattr(self, attr)))
                for attr in self.__slots__
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: "TLObject") -> bool:
        for attr in self.__slots__:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __len__(self) -> int:
        return len(self.write())

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)
