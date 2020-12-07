import time


class BaseTool():
    def __init__(self):
        pass

    @staticmethod
    def to_hex(data, leng):
        dec = str(hex(int(data)))
        dec = dec[2:]
        if dec.__len__() < leng:
            n = leng - len(dec)
            for i in range(0, n):
                dec = '0' + dec
                i = i + 1
        else:
            print("转化位数超限或格式不正确")
        print(dec)
        return dec

    @staticmethod
    def location_format(location):
        return (location * 10 ** 6)

    @staticmethod
    def getlocaltime():
        localti = time.strftime("%Y%m%d%H%M%S", time.localtime())
        localti = localti[2:]
        return localti