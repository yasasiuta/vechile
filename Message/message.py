


class Message():
    def __init__(self):
        pass

    def data_head(self):
        pass



    def data_head_2013(self, messageid, messagebodyproperty,simcard, serialnumber, messagepacktotal=None, packserial=None,version = 0):
        '''
        消息头：消息ID（word）+ 消息体属性（word）+ 终端手机号（BCD[6]）+ 消息流水号+ 消息包分装项（消息包总数（word）+包序列（word））
        :return:
        '''
        data_head = messageid + messagebodyproperty + self.simcard_format(simcard,version) + serialnumber + messagepacktotal + packserial
        return data_head

    def data_head_2019(self, messageid, messagebodyproperty,simcard, serialnumber, messagepacktotal=None, packserial=None,version = 1):
        '''
        消息头：消息ID（word）+ 消息体属性（word）+ 终端手机号（BCD[10]）+ 消息流水号+ 消息包分装项（消息包总数（word）+包序列（word））
        :return:
        '''
        data_head = messageid + messagebodyproperty + self.simcard_format(simcard,version) + serialnumber + messagepacktotal + packserial
        return data_head

    @staticmethod
    def simcard_format(simcard,version):
        #格式化sim卡号，按照协议版本，将不足位补0
        if version == 0:
            while len(simcard) < 12:
                simcard = "0" + simcard
        elif version == 1:
            while len(simcard) < 20:
                simcard = "0" + simcard
        return simcard


