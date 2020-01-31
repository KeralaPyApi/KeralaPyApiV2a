from .tl_object import TLObject


class List(list, TLObject):
    __slots__ = []

    def __repr__(self):
        return "keralapyapi.api.core.List([{}])".format(
            ",".join(TLObject.__repr__(i) for i in self)
        )
