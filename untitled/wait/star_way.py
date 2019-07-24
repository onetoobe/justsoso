import xlrd

wb = xlrd.open_workbook('F:/巨星之路.xlsx')
sh3 = wb.sheet_by_index(2)
sh4 = wb.sheet_by_index(3)
sh2 = wb.sheet_by_index(1)

def get_data(a):
    if type(a) != type('lll') and a != '':
        g = int(a)
        if g == 0:
            return 0
        else:
            return g
    else:
        return 0

class gift:
    def __init__(self,other,x,homeModelId,awayCaseId,playerNum,integral,position,period):
        self.other = other
        self.x = x
        self.homeModelId = homeModelId
        self.awayCaseId = awayCaseId
        self.playerNum = playerNum
        self.integral = integral
        self.position = position
        self.period = period

    def get_model(self,a):
        for rownum in range(a.nrows):
            t2=a.row_values(rownum)
            modleid = get_data(t2[5])
            if  modleid == self.homeModelId:
                self.homeModelId = str(t2[2])

    def get_other(self,a):
        for rownum in range(a.nrows):
            t3 = a.row_values(rownum)
            other = get_data(t3[0])
            if self.position == 1:
                self.position = 'pg'
            if self.position == 2:
                self.position = 'sg'
            if self.position == 3:
                self.position = 'sf'
            if self.position == 4:
                self.position = 'pf'
            if self.position == 5:
                self.position = 'c'
            if other == self.other:
                self.other = str(t3[1])
                self.other = self.other.replace('X',str(self.x))
                self.other = self.other.replace('homeModelId', str(self.homeModelId))
                self.other = self.other.replace('awayCaseId', str(self.awayCaseId))
                self.other = self.other.replace('playerNum', str(self.playerNum))
                self.other = self.other.replace('integral', str(self.integral))
                self.other = self.other.replace('position', str(self.position))
                self.other = self.other.replace('period', str(self.period))


for rownum in range(sh4.nrows):
    op =[]
    t4 = sh4.row_values(rownum)

    tittle = str(t4[5])

    other_1 = get_data(t4[9])
    x_1 = get_data(t4[10])
    homeModelId_1 = get_data(t4[11])
    awayCaseId_1 = get_data(t4[12])
    playerNum_1 = get_data(t4[13])
    integral_1 = get_data(t4[14])
    position_1 = get_data(t4[15])
    period_1 = get_data(t4[16])

    other_2 = get_data(t4[17])
    x_2 = get_data(t4[18])
    homeModelId_2 =get_data(t4[19])
    awayCaseId_2 = get_data(t4[20])
    playerNum_2 = get_data(t4[21])
    integral_2 = get_data(t4[22])
    position_2 = get_data(t4[23])

    period_2 = get_data(t4[24])
    other_3 = get_data(t4[25])
    x_3 = get_data(t4[26])
    homeModelId_3 = get_data(t4[27])
    awayCaseId_3 = get_data(t4[28])
    playerNum_3 = get_data(t4[29])
    integral_3 = get_data(t4[30])
    position_3 = get_data(t4[31])
    period_3 = get_data(t4[32])

    print('------'+tittle+'------')
    gift_1 = gift(other_1,x_1,homeModelId_1,awayCaseId_1,playerNum_1,integral_1,position_1,period_1)
    gift_1.get_model(sh2)
    gift_1.get_other(sh3)
    print(gift_1.other)

    gift_2 = gift(other_2, x_2, homeModelId_2, awayCaseId_2, playerNum_2, integral_2, position_2, period_2)
    gift_2.get_model(sh2)
    gift_2.get_other(sh3)
    print(gift_2.other)

    gift_3 = gift(other_3, x_3, homeModelId_3, awayCaseId_3, playerNum_3, integral_3, position_3, period_3)
    gift_3.get_model(sh2)
    gift_3.get_other(sh3)
    print(gift_3.other)
    print('\n')
