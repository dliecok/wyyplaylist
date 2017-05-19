import datetime


class baseInfo():
    def __init__(self, sId, sName, **op):
        self.sId = sId
        self.sName = sName
        self.sCreateTime = datetime.datetime.now()

        for p in op:
            setattr(self, p, op[p])