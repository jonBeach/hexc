class Conversion:
    def __init__(self, num):
        self.num = num
    
    def bd(self):
        return int(self.num,2)
    
    def bh(self):
        return hex(int(self.num,2))
    
    def db(self):
        return bin(int(self.num))
    
    def dh(self):
        return hex(int(self.num))
    
    def hb(self):
        temp = bin(int(self.num, 16))[2:].zfill(32)
        return ' '.join(temp[i:i+4] for i in range(0,32,4))
    
    def hd(self):
        return int(self.num, 16)