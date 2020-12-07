import time
from Public.basetool import BaseTool

'''
808协议的消息体
'''
alarmflag = 1
# tatus
# longitude
# latitude
# high
# speed
# direction
class Protocol_808_Body(BaseTool):
    def __init__(self):
        pass

    def databody_0200(self,alarmflag,status,longitude,latitude,high,speed,direction,addition):
        #报警标志【dwoed】+状态【dwoed】+经度【dwoed】+纬度【dwoed】+高程【word】+速度【word】+方向【word】+时间【bcd6】+附加信息
        longitude = self.location_format(longitude)
        latitude = self.location_format(latitude)
        databody_0200 = self.to_hex(alarmflag,8) +self.to_hex(status,8)+self.to_hex(longitude,8)+self.to_hex(latitude,8)\
        +self(high,4)+self.to_hex(speed,4)+self.to_hex(direction,4)+ self.getlocaltime() + addition

        return databody_0200

    def addition_808(self,**addition):
        #附加信息ID+附加信息长度
        newadditiondata = ''
        for key in addition.keys():
            if key in ('01','25','2B') :
                additiondata = key + self.to_hex(addition[key],8)
            elif key in ('02','03','04','2A'):
                additiondata = key + self.to_hex(addition[key], 4)
            elif key == '11':
                overspeedaddition = addition[key]
                print(overspeedaddition)
                for k in overspeedaddition.keys():
                    if k == '00' :
                        additiondata = key + k
                    elif k in ('01','02','03','04'):
                        additiondata = key + k + self.to_hex(overspeedaddition[k], 10)
            elif key == '12':
                additiondata = key + self.to_hex(addition[key], 12)
            elif key == '13':
                additiondata = key + self.to_hex(addition[key], 14)
            elif key in ('30','31'):
                additiondata = key + self.to_hex(addition[key], 2)
            elif key == '12':
                additiondata = key + self.to_hex(addition[key], 12)

            newadditiondata = newadditiondata + additiondata
        return newadditiondata




if __name__ == '__main__':

    addition = {
        '11':{
            '01': 10
        }
    }

    add = Protocol_808_Body()
    print(add.addition_808(**addition))