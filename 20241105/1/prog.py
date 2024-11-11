class Omnibus:
    attrs = dict()
    _attrs = dict()

    def __setattr__(self, attr, value):
        if attr in Omnibus.attrs:
            Omnibus.attrs[attr] += 1
        else:
            Omnibus.attrs[attr] = 1
        self._attrs[attr] = 1

    def __getattr__(self, attr):
        return Omnibus.attrs.get(attr, 0)

    def __delattr__(self, attr):
        if attr in self._attrs:
            del self._attrs[attr]
            Omnibus.attrs[attr] -= 1
            if not Omnibus.attrs[attr]:
                del Omnibus.attrs[attr]


import sys

exec(sys.stdin.read())
