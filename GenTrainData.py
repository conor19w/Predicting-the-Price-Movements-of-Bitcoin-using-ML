import Data_flow as flow
import TA_indicators as ind
import pandas as pd
import math

################# This generates csv files similar to traintype1 included in the supporting documents

df = pd.read_csv('C:\\Users\\conor\\Desktop\\Final year project\\Output\\extractedBitcoin_16.02.2021.csv')
Close= df["Close"]
Open= df["Open"]
High= df["High"]
Low= df["Low"]
Volume= df["Volume"]
'''Close=[]
Open=[]
High=[]
Low=[]
Volume=[]'''


'''
##Change time period
for i in range(len(Close1)):
    if i%2==0 and i!=0:
        Close.append(Close1[i])

for i in range(len(Open1)):
    if i%2==0 and i!=0:
        Open.append(Open1[i-1])

for i in range(len(High1)):
    if i%2==0 and i!=0:
        if High1[i-1]>High1[i]:
            High.append(High1[i-1])
        else:
            High.append(High1[i])

for i in range(len(Low1)):
    if i%2==0 and i!=0:
        if Low1[i-1]<Low1[i]:
            Low.append(Low1[i-1])
        else:
            Low.append(Low1[i])

for i in range(len(Volume1)):
    if i%2==0 and i!=0:
        Volume.append(Volume1[i]+Volume1[i-1])'''



#y=[5,7,13,17,41,200]
#y1=[5,7,13,17,41,200]
#y=[5,13,20,40,55,200]
#y=[5,7,10,14,18,23,27,30,33,38,50,55,73,77,83,91,101,151,233]
y = [1,2, 3, 4, 5, 6, 7, 8, 9, 10] ##SMA lengths
y1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]  ##EMA lengths

#y = [5, 10, 13, 15, 19, 23, 27, 30, 45, 60]
#y1 = [5, 10, 13, 15, 19, 23, 27, 30, 45, 60]
#y = [4, 5, 6, 7, 8, 9, 10, 13, 15, 20]
#y1 = [4, 5, 6, 7, 8, 9, 10, 13, 15, 20]
#y=[3,5,8,13,21,34,55,89,144,233]
#y1=[3,5,8,13,21,34,55,89,144,233]
#y1=[5,13,17,20,25,200]
#y=[5,13,17,20,25,200]
#y1=[5,7,13,16,24,27,53,114,215,305]
largest=0
## Array of indicator values associated with current data point & the actual next market move
if y1[len(y1)-1]>y[len(y)-1]:
    largest=y1[len(y1)-1]
else:
    largest=y[len(y)-1]

dataStream = []
dataStream1=[]
dataStream2=[]
dataStream3=[]
dataStream4=[]
SMAind=[]
EMAind=[]
BBind=[]
RSIind=[]
MACDind=[]
CMFVind=[]
MFIind=[]
decision=[]
CMFVgraph=[]
ADgraph=[]
dataStreamClose =[]
dataStreamLow = []
dataStreamHigh = []
dataStreamVolume = []
ADlineInd=[]
ADXind=[]
Aroonind=[]
OBVind=[]
StocInd=[]
ChaikinInd=[]
z=[]
TrainSet=""




length=len(Close)
#length=500



#print(len(Close),len(High),len(Open),len(Low),len(Volume))



period=4  ##How far ahead to label
Average=1  ##Label based on the Average over given period

if Average:
    ##Average
    for i in range(period,length-period):
        temp=0
        for j in range(i+1,i+period+1):
            temp+=Close[j]
        temp=temp/period
        if Close[i-period]>temp:
            z.append("0") ##price went down
        else:
            z.append("1") ##price went up
    print("Z values complete")
else:
    ##Gen expected outputs
    for i in range(period,length):
        if Close[i-period]>Close[i]:
            z.append("0") ##price went down
        elif Close[i-period]<Close[i]:
            z.append("1") ##price went up
        else:
            if i < length-1:
                if Close[i - period] > Close[i+1]:
                    z.append("0")  ##price went down
                elif Close[i - period] < Close[i+1]:
                    z.append("1")  ##price went up
                else:
                    if i < length - 2:
                        if Close[i - period] > Close[i + 2]:
                            z.append("0")  ##price went down
                        elif Close[i - period] < Close[i + 2]:
                            z.append("1")  ##price went up
                        else:
                            if i<length -3:
                                if Close[i - period] > Close[i + 3]:
                                    z.append("0")  ##price went down
                                elif Close[i - period] < Close[i + 3]:
                                    z.append("1")  ##price went up
                            else:
                                z.append("1")  ##price went up
                    else:
                        z.append("1")  ##price went up
            else:
                z.append("1")  ##price went up
    print("Z values complete")
decisionsSMA = []
decisionsEMA = []
previousSMA=[]
previousEMA=[]
for i in range(length-period):
    #SMA
    dataStream = flow.dataflow(dataStream, Close, i, largest, y[0])  # appends new piece of data
    SMA1 = ind.SMA(dataStream, y1[0])
    SMA2 = ind.SMA(dataStream, y1[1])
    SMA3 = ind.SMA(dataStream, y1[2])
    SMA4 = ind.SMA(dataStream, y1[3])
    SMA5 = ind.SMA(dataStream, y1[4])
    SMA6 = ind.SMA(dataStream, y1[5])
    SMA7 = ind.SMA(dataStream, y1[6])
    SMA8 = ind.SMA(dataStream, y1[7])
    SMA9 = ind.SMA(dataStream, y1[8])
    SMA10 = ind.SMA(dataStream, y1[9])
    #indicators of up trend
    compSMA_1_2 = ind.find_SMA_cross(SMA1, SMA2)
    compSMA_1_3 = ind.find_SMA_cross(SMA1, SMA3)
    compSMA_1_4 = ind.find_SMA_cross(SMA1, SMA4)
    compSMA_1_5 = ind.find_SMA_cross(SMA1, SMA5)
    compSMA_1_6 = ind.find_SMA_cross(SMA1, SMA6)
    compSMA_1_7 = ind.find_SMA_cross(SMA1, SMA7)
    compSMA_1_8 = ind.find_SMA_cross(SMA1, SMA8)
    compSMA_1_9 = ind.find_SMA_cross(SMA1, SMA9)
    compSMA_1_10 = ind.find_SMA_cross(SMA1, SMA10)
    compSMA_2_3 = ind.find_SMA_cross(SMA2, SMA3)
    compSMA_2_4 = ind.find_SMA_cross(SMA2, SMA4)
    compSMA_2_5 = ind.find_SMA_cross(SMA2, SMA5)
    compSMA_2_6 = ind.find_SMA_cross(SMA2, SMA6)
    compSMA_2_7 = ind.find_SMA_cross(SMA2, SMA7)
    compSMA_2_8 = ind.find_SMA_cross(SMA2, SMA8)
    compSMA_2_9 = ind.find_SMA_cross(SMA2, SMA9)
    compSMA_2_10 = ind.find_SMA_cross(SMA2, SMA10)
    compSMA_3_4 = ind.find_SMA_cross(SMA3, SMA4)
    compSMA_3_5 = ind.find_SMA_cross(SMA3, SMA5)
    compSMA_3_6 = ind.find_SMA_cross(SMA3, SMA6)
    compSMA_3_7 = ind.find_SMA_cross(SMA3, SMA7)
    compSMA_3_8 = ind.find_SMA_cross(SMA3, SMA8)
    compSMA_3_9 = ind.find_SMA_cross(SMA3, SMA9)
    compSMA_3_10 = ind.find_SMA_cross(SMA3, SMA10)
    compSMA_4_5 = ind.find_SMA_cross(SMA4, SMA5)
    compSMA_4_6 = ind.find_SMA_cross(SMA4, SMA6)
    compSMA_4_7 = ind.find_SMA_cross(SMA4, SMA7)
    compSMA_4_8 = ind.find_SMA_cross(SMA4, SMA8)
    compSMA_4_9 = ind.find_SMA_cross(SMA4, SMA9)
    compSMA_4_10 = ind.find_SMA_cross(SMA4, SMA10)
    compSMA_5_6 = ind.find_SMA_cross(SMA5, SMA6)
    compSMA_5_7 = ind.find_SMA_cross(SMA5, SMA7)
    compSMA_5_8 = ind.find_SMA_cross(SMA5, SMA8)
    compSMA_5_9 = ind.find_SMA_cross(SMA5, SMA9)
    compSMA_5_10 = ind.find_SMA_cross(SMA5, SMA10)
    compSMA_6_7 = ind.find_SMA_cross(SMA6, SMA7)
    compSMA_6_8 = ind.find_SMA_cross(SMA6, SMA8)
    compSMA_6_9 = ind.find_SMA_cross(SMA6, SMA9)
    compSMA_6_10 = ind.find_SMA_cross(SMA6, SMA10)
    compSMA_7_8 = ind.find_SMA_cross(SMA7, SMA8)
    compSMA_7_9 = ind.find_SMA_cross(SMA7, SMA9)
    compSMA_7_10 = ind.find_SMA_cross(SMA7, SMA10)
    compSMA_8_9 = ind.find_SMA_cross(SMA8, SMA9)
    compSMA_8_10 = ind.find_SMA_cross(SMA8, SMA10)
    compSMA_9_10 = ind.find_SMA_cross(SMA9, SMA10)

    currentSMA=[compSMA_1_2[0], compSMA_1_3[0], compSMA_1_4[0],
                    compSMA_1_5[0], compSMA_1_6[0], compSMA_2_3[0],
                    compSMA_2_4[0], compSMA_2_5[0], compSMA_2_6[0],
                    compSMA_3_4[0], compSMA_3_5[0], compSMA_3_6[0],
                    compSMA_4_5[0], compSMA_4_6[0],compSMA_5_6[0]
                    ,compSMA_5_7[0],compSMA_6_7[0],
                    compSMA_5_8[0],compSMA_5_9[0],compSMA_1_7[0],compSMA_2_7[0],compSMA_3_7[0],compSMA_4_7[0],
                    compSMA_5_10[0],compSMA_6_8[0],compSMA_6_9[0],compSMA_6_10[0],
                    compSMA_7_8[0],compSMA_7_9[0],compSMA_7_10[0],compSMA_8_9[0],
                    compSMA_8_10[0],compSMA_9_10[0],compSMA_2_8[0],compSMA_2_9[0],compSMA_2_10[0],
                    compSMA_3_8[0],compSMA_3_9[0],compSMA_3_10[0],compSMA_4_8[0],
                    compSMA_4_9[0],compSMA_4_10[0],compSMA_1_8[0],compSMA_1_9[0],
                    compSMA_1_10[0]]
    decision1=[]
    if i>0:
        for j in range(len(currentSMA)):
            if currentSMA[j]!=previousSMA[j]:
                decision1.append(currentSMA[j])
            else:
                decision1.append(.5)
        SMAind.append(decision1)
    else:
        SMAind.append([compSMA_1_2[0], compSMA_1_3[0], compSMA_1_4[0],
                    compSMA_1_5[0], compSMA_1_6[0], compSMA_2_3[0],
                    compSMA_2_4[0], compSMA_2_5[0], compSMA_2_6[0],
                    compSMA_3_4[0], compSMA_3_5[0], compSMA_3_6[0],
                    compSMA_4_5[0], compSMA_4_6[0],compSMA_5_6[0]
                    ,compSMA_5_7[0],compSMA_6_7[0],
                    compSMA_5_8[0],compSMA_5_9[0],compSMA_1_7[0],compSMA_2_7[0],compSMA_3_7[0],compSMA_4_7[0],
                    compSMA_5_10[0],compSMA_6_8[0],compSMA_6_9[0],compSMA_6_10[0],
                    compSMA_7_8[0],compSMA_7_9[0],compSMA_7_10[0],compSMA_8_9[0],
                    compSMA_8_10[0],compSMA_9_10[0],compSMA_2_8[0],compSMA_2_9[0],compSMA_2_10[0],
                    compSMA_3_8[0],compSMA_3_9[0],compSMA_3_10[0],compSMA_4_8[0],
                    compSMA_4_9[0],compSMA_4_10[0],compSMA_1_8[0],compSMA_1_9[0],
                    compSMA_1_10[0]])
    previousSMA=currentSMA

        #EMA
    data = pd.Series(dataStream)
    EMA1 = ind.EMA(data, y1[0])
    EMA2 = ind.EMA(data, y1[1])
    EMA3 = ind.EMA(data, y1[2])
    EMA4 = ind.EMA(data, y1[3])
    EMA5 = ind.EMA(data, y1[4])
    EMA6 = ind.EMA(data, y1[5])
    EMA7 = ind.EMA(data, y1[6])
    EMA8 = ind.EMA(data, y1[7])
    EMA9 = ind.EMA(data, y1[8])
    EMA10 = ind.EMA(data, y1[9])
    ##uptrend indicators
    compEMA_1_2 = ind.find_SMA_cross(EMA1, EMA2)
    compEMA_1_3 = ind.find_SMA_cross(EMA1, EMA3)
    compEMA_1_4 = ind.find_SMA_cross(EMA1, EMA4)
    compEMA_1_5 = ind.find_SMA_cross(EMA1, EMA5)
    compEMA_1_6 = ind.find_SMA_cross(EMA1, EMA6)
    compEMA_1_7 = ind.find_SMA_cross(EMA1, EMA7)
    compEMA_1_8 = ind.find_SMA_cross(EMA1, EMA8)
    compEMA_1_9 = ind.find_SMA_cross(EMA1, EMA9)
    compEMA_1_10 = ind.find_SMA_cross(EMA1, EMA10)
    compEMA_2_3 = ind.find_SMA_cross(EMA2, EMA3)
    compEMA_2_4 = ind.find_SMA_cross(EMA2, EMA4)
    compEMA_2_5 = ind.find_SMA_cross(EMA2, EMA5)
    compEMA_2_6 = ind.find_SMA_cross(EMA2, EMA6)
    compEMA_2_7 = ind.find_SMA_cross(EMA2, EMA7)
    compEMA_2_8 = ind.find_SMA_cross(EMA2, EMA8)
    compEMA_2_9 = ind.find_SMA_cross(EMA2, EMA9)
    compEMA_2_10 = ind.find_SMA_cross(EMA2, EMA10)
    compEMA_3_4 = ind.find_SMA_cross(EMA3, EMA4)
    compEMA_3_5 = ind.find_SMA_cross(EMA3, EMA5)
    compEMA_3_6 = ind.find_SMA_cross(EMA3, EMA6)
    compEMA_3_7 = ind.find_SMA_cross(EMA3, EMA7)
    compEMA_3_8 = ind.find_SMA_cross(EMA3, EMA8)
    compEMA_3_9 = ind.find_SMA_cross(EMA3, EMA9)
    compEMA_3_10 = ind.find_SMA_cross(EMA3, EMA10)
    compEMA_4_5 = ind.find_SMA_cross(EMA4, EMA5)
    compEMA_4_6 = ind.find_SMA_cross(EMA4, EMA6)
    compEMA_4_7 = ind.find_SMA_cross(EMA4, EMA7)
    compEMA_4_8 = ind.find_SMA_cross(EMA4, EMA8)
    compEMA_4_9 = ind.find_SMA_cross(EMA4, EMA9)
    compEMA_4_10 = ind.find_SMA_cross(EMA4, EMA10)
    compEMA_5_6 = ind.find_SMA_cross(EMA5, EMA6)
    compEMA_5_7 = ind.find_SMA_cross(EMA5, EMA7)
    compEMA_5_8 = ind.find_SMA_cross(EMA5, EMA8)
    compEMA_5_9 = ind.find_SMA_cross(EMA5, EMA9)
    compEMA_5_10 = ind.find_SMA_cross(EMA5, EMA10)
    compEMA_6_7 = ind.find_SMA_cross(EMA6, EMA7)
    compEMA_6_8 = ind.find_SMA_cross(EMA6, EMA8)
    compEMA_6_9 = ind.find_SMA_cross(EMA6, EMA9)
    compEMA_6_10 = ind.find_SMA_cross(EMA6, EMA10)
    compEMA_7_8 = ind.find_SMA_cross(EMA7, EMA8)
    compEMA_7_9 = ind.find_SMA_cross(EMA7, EMA9)
    compEMA_7_10 = ind.find_SMA_cross(EMA7, EMA10)
    compEMA_8_9 = ind.find_SMA_cross(EMA8, EMA9)
    compEMA_8_10 = ind.find_SMA_cross(EMA8, EMA10)
    compEMA_9_10 = ind.find_SMA_cross(EMA9, EMA10)

    currentEMA=[compEMA_1_2[0], compEMA_1_3[0], compEMA_1_4[0],
                    compEMA_1_5[0], compEMA_1_6[0], compEMA_2_3[0],
                    compEMA_2_4[0], compEMA_2_5[0], compEMA_2_6[0],
                    compEMA_3_4[0], compEMA_3_5[0], compEMA_3_6[0],
                    compEMA_4_5[0], compEMA_4_6[0],compEMA_5_6[0]
                    ,compEMA_5_7[0],compEMA_6_7[0],
                    compEMA_5_8[0],compEMA_5_9[0],compEMA_1_7[0],compEMA_2_7[0],compEMA_3_7[0],compEMA_4_7[0],
                    compEMA_5_10[0],compEMA_6_8[0],compEMA_6_9[0],compEMA_6_10[0],
                    compEMA_7_8[0],compEMA_7_9[0],compEMA_7_10[0],compEMA_8_9[0],
                    compEMA_8_10[0],compEMA_9_10[0],compEMA_2_8[0],compEMA_2_9[0],compEMA_2_10[0],
                    compEMA_3_8[0],compEMA_3_9[0],compEMA_3_10[0],compEMA_4_8[0],
                    compEMA_4_9[0],compEMA_4_10[0],compEMA_1_8[0],compEMA_1_9[0],
                    compEMA_1_10[0]]
    decision1 = []
    if i > 0:
        for j in range(len(currentEMA)):
            if currentEMA[j] != previousEMA[j]:
                decision1.append(currentEMA[j])
            else:
                decision1.append(.5)
        EMAind.append(decision1)
    else:
        EMAind.append([compEMA_1_2[0], compEMA_1_3[0], compEMA_1_4[0],
                    compEMA_1_5[0], compEMA_1_6[0], compEMA_2_3[0],
                    compEMA_2_4[0], compEMA_2_5[0], compEMA_2_6[0],
                    compEMA_3_4[0], compEMA_3_5[0], compEMA_3_6[0],
                    compEMA_4_5[0], compEMA_4_6[0],compEMA_5_6[0]
                    ,compEMA_5_7[0],compEMA_6_7[0],
                    compEMA_5_8[0],compEMA_5_9[0],compEMA_1_7[0],compEMA_2_7[0],compEMA_3_7[0],compEMA_4_7[0],
                    compEMA_5_10[0],compEMA_6_8[0],compEMA_6_9[0],compEMA_6_10[0],
                    compEMA_7_8[0],compEMA_7_9[0],compEMA_7_10[0],compEMA_8_9[0],
                    compEMA_8_10[0],compEMA_9_10[0],compEMA_2_8[0],compEMA_2_9[0],compEMA_2_10[0],
                    compEMA_3_8[0],compEMA_3_9[0],compEMA_3_10[0],compEMA_4_8[0],
                    compEMA_4_9[0],compEMA_4_10[0],compEMA_1_8[0],compEMA_1_9[0],
                    compEMA_1_10[0]])
    previousEMA = currentEMA

print("SMA & EMA complete")


BBvals=[2,3,4,5,6,7,8,9,10,11]
dataStream1=[]
for i in range(length-period):
    ##Bollinger Bands
    dataStream1 = flow.dataflow(dataStream1, Close, i, 100, y[0])  ## responds to data outside window
    bbupperL1,bblowerU1,bbupperU1,bblowerL1 = ind.BB(dataStream1, BBvals[0])
    decision1 = ind.find_BB_cross(bbupperL1, bblowerU1,bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[1])
    decision2 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[2])
    decision3 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[3])
    decision4 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[4])
    decision5 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[5])
    decision6 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[6])
    decision7 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[7])
    decision8 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[8])
    decision9 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(dataStream1, BBvals[9])
    decision10 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, dataStream1)

    BBind.append([decision1[0],decision2[0],decision3[0],decision4[0],decision5[0],
                  decision6[0],decision7[0],decision8[0],decision9[0],decision10[0]])

print("Bollinger Bands complete")
dataStream = []
dataStream1=[]
dataStream2=[]
for i in range(length-period):
    ##RSI
    dataStream = flow.dataflow(dataStream, Close, i, 3, 0)
    dataStream1 = flow.dataflow(dataStream1, Close, i, 4, 0)
    dataStream2 = flow.dataflow(dataStream2, Close, i, 5, 0)
    if len(dataStream2) > 15:
        decision1 = ind.RSI(dataStream)
        decision2 = ind.RSI(dataStream1)
        decision3 = ind.RSI(dataStream2)
        decision=[decision1,decision2,decision3]
    else:
        decision = [50,50,50]
    RSIind.append(decision)
print("RSI complete")

dataStream1=[]
dataStream2=[]
dataStream3=[]
dataStream4=[]
dataStream5=[]
dataStream6=[]
dataStream7=[]
dataStream8=[]
dataStream9=[]
dataStream10=[]
for i in range(length-period):
    ##MACD
    dataStream1 = flow.dataflow(dataStream1, Close, i,50, 4)  ##responds to data outside window
    decision1 = ind.MACDsignal(dataStream1, 6, 4, 3, type=0)
    decision2 = ind.MACDsignal(dataStream1, 7, 5, 4, type=0)
    decision3 = ind.MACDsignal(dataStream1, 8, 5, 4, type=0)
    decision4 = ind.MACDsignal(dataStream1, 9, 5, 4, type=0)
    decision5 = ind.MACDsignal(dataStream1, 10, 6, 5, type=0)
    decision6 = ind.MACDsignal(dataStream1, 13, 9, 7, type=0)
    decision7 = ind.MACDsignal(dataStream1, 15, 10, 8, type=0)
    decision8 = ind.MACDsignal(dataStream1, 26, 12, 9, type=0)
    decision9 = ind.MACDsignal(dataStream1, 12, 6, 5, type=0)
    decision10 = ind.MACDsignal(dataStream1, 18, 14, 9, type=0)

    MACDind.append([decision1[0],decision2[0],decision3[0],decision4[0],decision5[0],
                    decision6[0],decision7[0],decision8[0],decision9[0],decision10[0]])
print("MACD complete")


dataStream = []
for i in range(length-period):
    ##CMFV
    dataStream = flow.dataflow(dataStream, Close, i, 30, y[0])  # appends new piece of data
    CMFVgraph = ind.CMFV(CMFVgraph, Close[i], Low[i], High[i], Volume[i])  ##Calculate A/D Line
    decision1 = ind.CMFVInd(CMFVgraph, dataStream)
    ##ADline
    ADgraph = ind.ADline(ADgraph, Close[i], Low[i], High[i], Volume[i])  ##Calculate A/D Line
    decision2 = ind.ADlineInd(ADgraph, dataStream)

    CMFVind.append(decision1[0])
    ADlineInd.append(decision2[0])
print("CMFV & A/D line complete")


for i in range(length-period):
    ##MFI
    dataStreamClose = flow.dataflow(dataStreamClose, Close, i, 15, 0)  # appends new piece of data
    dataStreamLow = flow.dataflow(dataStreamLow, Low, i, 15, 0)  # appends new piece of data
    dataStreamHigh = flow.dataflow(dataStreamHigh, High, i, 15, 0)  # appends new piece of data
    dataStreamVolume = flow.dataflow(dataStreamVolume, Volume, i, 15, 0)  # appends new piece of data
    MFI = ind.MFI(dataStreamHigh,dataStreamLow,dataStreamClose,dataStreamVolume,len(dataStreamClose))  ##Calculate MFI
    MFIind.append(MFI)
print("MFI complete")

ADX=[0,0,0,0,0,0,0,0,0,0]
pos_DI=[0,0,0,0,0,0,0,0,0,0]
neg_DI=[0,0,0,0,0,0,0,0,0,0]
CTM=[0,0,0,0,0,0,0,0,0,0]
CDMneg=[0,0,0,0,0,0,0,0,0,0]
CDMpos=[0,0,0,0,0,0,0,0,0,0]
dec=[]
dataStreamClose1 =[]
dataStreamLow1 = []
dataStreamHigh1 = []
dataStreamClose2 =[]
dataStreamLow2 = []
dataStreamHigh2 = []
dataStreamClose3 =[]
dataStreamLow3 = []
dataStreamHigh3 = []
dataStreamClose4 =[]
dataStreamLow4 = []
dataStreamHigh4 = []
dataStreamClose5 =[]
dataStreamLow5 = []
dataStreamHigh5 = []
dataStreamClose6 =[]
dataStreamLow6 = []
dataStreamHigh6 = []
dataStreamClose7 =[]
dataStreamLow7 = []
dataStreamHigh7 = []
dataStreamClose8 =[]
dataStreamLow8 = []
dataStreamHigh8 = []
dataStreamClose9 =[]
dataStreamLow9 = []
dataStreamHigh9 = []
dataStreamClose10 =[]
dataStreamLow10 = []
dataStreamHigh10 = []
ADXvals = [2,3,4,5,6,7,8,9,10,11]
for i in range(length-period):
    dataStreamClose1 = flow.dataflow(dataStreamClose1, Close, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamLow1 = flow.dataflow(dataStreamLow1, Low, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamHigh1 = flow.dataflow(dataStreamHigh1, High, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamClose2 = flow.dataflow(dataStreamClose2, Close, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamLow2 = flow.dataflow(dataStreamLow2, Low, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamHigh2 = flow.dataflow(dataStreamHigh2, High, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamClose3 = flow.dataflow(dataStreamClose3, Close, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamLow3 = flow.dataflow(dataStreamLow3, Low, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamHigh3 = flow.dataflow(dataStreamHigh3, High, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamClose4 = flow.dataflow(dataStreamClose4, Close, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamLow4 = flow.dataflow(dataStreamLow4, Low, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamHigh4 = flow.dataflow(dataStreamHigh4, High, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamClose5 = flow.dataflow(dataStreamClose5, Close, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamLow5 = flow.dataflow(dataStreamLow5, Low, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamHigh5 = flow.dataflow(dataStreamHigh5, High, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamClose6 = flow.dataflow(dataStreamClose6, Close, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamLow6 = flow.dataflow(dataStreamLow6, Low, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamHigh6 = flow.dataflow(dataStreamHigh6, High, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamClose7 = flow.dataflow(dataStreamClose7, Close, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamLow7 = flow.dataflow(dataStreamLow7, Low, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamHigh7 = flow.dataflow(dataStreamHigh7, High, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamClose8 = flow.dataflow(dataStreamClose8, Close, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamLow8 = flow.dataflow(dataStreamLow8, Low, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamHigh8 = flow.dataflow(dataStreamHigh8, High, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamClose9 = flow.dataflow(dataStreamClose9, Close, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamLow9 = flow.dataflow(dataStreamLow9, Low, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamHigh9 = flow.dataflow(dataStreamHigh9, High, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamClose10 = flow.dataflow(dataStreamClose10, Close, i, ADXvals[9], 0)  # appends new piece of data
    dataStreamLow10 = flow.dataflow(dataStreamLow10, Low, i, ADXvals[9], 0)  # appends new piece of data
    dataStreamHigh10 = flow.dataflow(dataStreamHigh10, High, i, ADXvals[9], 0)  # appends new piece of data
    if i >= 20:
        ADX[0], pos_DI[0], neg_DI[0], CTM[0], CDMneg[0], CDMpos[0] = ind.DI(dataStreamHigh1, dataStreamLow1,
                                                                            dataStreamClose1, CDMpos[0], CDMneg[0],
                                                                            CTM[0], ADX[0])
        ADX[1], pos_DI[1], neg_DI[1], CTM[1], CDMneg[1], CDMpos[1] = ind.DI(dataStreamHigh2, dataStreamLow2,
                                                                            dataStreamClose2, CDMpos[1], CDMneg[1],
                                                                            CTM[1], ADX[1])
        ADX[2], pos_DI[2], neg_DI[2], CTM[2], CDMneg[2], CDMpos[2] = ind.DI(dataStreamHigh3, dataStreamLow3,
                                                                            dataStreamClose3, CDMpos[2], CDMneg[2],
                                                                            CTM[2], ADX[2])
        ADX[3], pos_DI[3], neg_DI[3], CTM[3], CDMneg[3], CDMpos[3] = ind.DI(dataStreamHigh4, dataStreamLow4,
                                                                            dataStreamClose4, CDMpos[3], CDMneg[3],
                                                                            CTM[3], ADX[3])
        ADX[4], pos_DI[4], neg_DI[4], CTM[4], CDMneg[4], CDMpos[4] = ind.DI(dataStreamHigh5, dataStreamLow5,
                                                                            dataStreamClose5, CDMpos[4], CDMneg[4],
                                                                            CTM[4], ADX[4])
        ADX[5], pos_DI[5], neg_DI[5], CTM[5], CDMneg[5], CDMpos[5] = ind.DI(dataStreamHigh6, dataStreamLow6,
                                                                            dataStreamClose6, CDMpos[5], CDMneg[5],
                                                                            CTM[5], ADX[5])
        ADX[6], pos_DI[6], neg_DI[6], CTM[6], CDMneg[6], CDMpos[6] = ind.DI(dataStreamHigh7, dataStreamLow7,
                                                                            dataStreamClose7, CDMpos[6], CDMneg[6],
                                                                            CTM[6], ADX[6])
        ADX[7], pos_DI[7], neg_DI[7], CTM[7], CDMneg[7], CDMpos[7] = ind.DI(dataStreamHigh8, dataStreamLow8,
                                                                            dataStreamClose8, CDMpos[7], CDMneg[7],
                                                                            CTM[7], ADX[7])
        ADX[8], pos_DI[8], neg_DI[8], CTM[8], CDMneg[8], CDMpos[8] = ind.DI(dataStreamHigh9, dataStreamLow9,
                                                                            dataStreamClose9, CDMpos[8], CDMneg[8],
                                                                            CTM[8], ADX[8])
        ADX[9], pos_DI[9], neg_DI[9], CTM[9], CDMneg[9], CDMpos[9] = ind.DI(dataStreamHigh10, dataStreamLow10,
                                                                            dataStreamClose10, CDMpos[9], CDMneg[9],
                                                                            CTM[9], ADX[9])
        ADXind.append([ind.ADXdec(neg_DI[0],pos_DI[0],ADX[0]),ind.ADXdec(neg_DI[1],pos_DI[1],ADX[1]),ind.ADXdec(neg_DI[2],pos_DI[2],ADX[2]),
                   ind.ADXdec(neg_DI[3],pos_DI[3],ADX[3]),ind.ADXdec(neg_DI[4],pos_DI[4],ADX[4]),ind.ADXdec(neg_DI[5],pos_DI[5],ADX[5]),
                   ind.ADXdec(neg_DI[6],pos_DI[6],ADX[6]),ind.ADXdec(neg_DI[7],pos_DI[7],ADX[7]),ind.ADXdec(neg_DI[8],pos_DI[8],ADX[8]),
                   ind.ADXdec(neg_DI[9],pos_DI[9],ADX[9])])
    else:
        ADXind.append([.5,.5,.5,.5,.5,.5,.5,.5,.5,.5])

print("ADX complete")

counterHigh=[0,0,0,0,0,0,0,0,0,0]
counterLow=[0,0,0,0,0,0,0,0,0,0]
highesthigh=[0,0,0,0,0,0,0,0,0,0]
lowestlow=[99999999,99999999,99999999,99999999,99999999,99999999,99999999,99999999,99999999,99999999]
dataStreamLow1=[]
dataStreamHigh1=[]
dataStreamLow2=[]
dataStreamHigh2=[]
dataStreamLow3=[]
dataStreamHigh3=[]
dataStreamLow4=[]
dataStreamHigh4=[]
dataStreamLow5=[]
dataStreamHigh5=[]
dataStreamLow6=[]
dataStreamHigh6=[]
dataStreamLow7=[]
dataStreamHigh7=[]
dataStreamLow8=[]
dataStreamHigh8=[]
dataStreamLow9=[]
dataStreamHigh9=[]
dataStreamLow10=[]
dataStreamHigh10=[]
AroonUp=[0,0,0,0,0,0,0,0,0,0]
AroonDown=[0,0,0,0,0,0,0,0,0,0]
for i in range(length-period):
    dataStreamLow1 = flow.dataflow(dataStreamLow1, Low, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamHigh1 = flow.dataflow(dataStreamHigh1, High, i, ADXvals[0], 0)  # appends new piece of data
    AroonUp[0], AroonDown[0], counterHigh[0], counterLow[0], highesthigh[0], lowestlow[0] = ind.Aroon(dataStreamHigh1,
                                                                                                      dataStreamLow1,
                                                                                                      len(
                                                                                                          dataStreamLow1),
                                                                                                      counterHigh[0],
                                                                                                      counterLow[0],
                                                                                                      highesthigh[0],
                                                                                                      lowestlow[0])

    dataStreamLow2 = flow.dataflow(dataStreamLow2, Low, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamHigh2 = flow.dataflow(dataStreamHigh2, High, i, ADXvals[1], 0)  # appends new piece of data
    AroonUp[1], AroonDown[1], counterHigh[1], counterLow[1], highesthigh[1], lowestlow[1] = ind.Aroon(dataStreamHigh2,
                                                                                                      dataStreamLow2,
                                                                                                      len(
                                                                                                          dataStreamLow2),
                                                                                                      counterHigh[1],
                                                                                                      counterLow[1],
                                                                                                      highesthigh[1],
                                                                                                      lowestlow[1])

    dataStreamLow3 = flow.dataflow(dataStreamLow3, Low, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamHigh3 = flow.dataflow(dataStreamHigh3, High, i, ADXvals[2], 0)  # appends new piece of data
    AroonUp[2], AroonDown[2], counterHigh[2], counterLow[2], highesthigh[2], lowestlow[2] = ind.Aroon(dataStreamHigh3,
                                                                                                      dataStreamLow3,
                                                                                                      len(
                                                                                                          dataStreamLow3),
                                                                                                      counterHigh[2],
                                                                                                      counterLow[2],
                                                                                                      highesthigh[2],
                                                                                                      lowestlow[2])

    dataStreamLow4 = flow.dataflow(dataStreamLow4, Low, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamHigh4 = flow.dataflow(dataStreamHigh4, High, i, ADXvals[3], 0)  # appends new piece of data
    AroonUp[3], AroonDown[3], counterHigh[3], counterLow[3], highesthigh[3], lowestlow[3] = ind.Aroon(dataStreamHigh4,
                                                                                                      dataStreamLow4,
                                                                                                      len(
                                                                                                          dataStreamLow4),
                                                                                                      counterHigh[3],
                                                                                                      counterLow[3],
                                                                                                      highesthigh[3],
                                                                                                      lowestlow[3])

    dataStreamLow5 = flow.dataflow(dataStreamLow5, Low, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamHigh5 = flow.dataflow(dataStreamHigh5, High, i, ADXvals[4], 0)  # appends new piece of data
    AroonUp[4], AroonDown[4], counterHigh[4], counterLow[4], highesthigh[4], lowestlow[4] = ind.Aroon(dataStreamHigh5,
                                                                                                      dataStreamLow5,
                                                                                                      len(
                                                                                                          dataStreamLow5),
                                                                                                      counterHigh[4],
                                                                                                      counterLow[4],
                                                                                                      highesthigh[4],
                                                                                                      lowestlow[4])

    dataStreamLow6 = flow.dataflow(dataStreamLow6, Low, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamHigh6 = flow.dataflow(dataStreamHigh6, High, i, ADXvals[5], 0)  # appends new piece of data
    AroonUp[5], AroonDown[5], counterHigh[5], counterLow[5], highesthigh[5], lowestlow[5] = ind.Aroon(dataStreamHigh6,
                                                                                                      dataStreamLow6,
                                                                                                      len(
                                                                                                          dataStreamLow6),
                                                                                                      counterHigh[5],
                                                                                                      counterLow[5],
                                                                                                      highesthigh[5],
                                                                                                      lowestlow[5])

    dataStreamLow7 = flow.dataflow(dataStreamLow7, Low, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamHigh7 = flow.dataflow(dataStreamHigh7, High, i, ADXvals[6], 0)  # appends new piece of data
    AroonUp[6], AroonDown[6], counterHigh[6], counterLow[6], highesthigh[6], lowestlow[6] = ind.Aroon(dataStreamHigh7,
                                                                                                      dataStreamLow7,
                                                                                                      len(
                                                                                                          dataStreamLow7),
                                                                                                      counterHigh[6],
                                                                                                      counterLow[6],
                                                                                                      highesthigh[6],
                                                                                                      lowestlow[6])

    dataStreamLow8 = flow.dataflow(dataStreamLow8, Low, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamHigh8 = flow.dataflow(dataStreamHigh8, High, i, ADXvals[7], 0)  # appends new piece of data
    AroonUp[7], AroonDown[7], counterHigh[7], counterLow[7], highesthigh[7], lowestlow[7] = ind.Aroon(dataStreamHigh8,
                                                                                                      dataStreamLow8,
                                                                                                      len(
                                                                                                          dataStreamLow8),
                                                                                                      counterHigh[7],
                                                                                                      counterLow[7],
                                                                                                      highesthigh[7],
                                                                                                      lowestlow[7])

    dataStreamLow9 = flow.dataflow(dataStreamLow9, Low, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamHigh9 = flow.dataflow(dataStreamHigh9, High, i, ADXvals[8], 0)  # appends new piece of data
    AroonUp[8], AroonDown[8], counterHigh[8], counterLow[8], highesthigh[8], lowestlow[8] = ind.Aroon(dataStreamHigh9,
                                                                                                      dataStreamLow9,
                                                                                                      len(
                                                                                                          dataStreamLow9),
                                                                                                      counterHigh[8],
                                                                                                      counterLow[8],
                                                                                                      highesthigh[8],
                                                                                                      lowestlow[8])

    dataStreamLow10 = flow.dataflow(dataStreamLow10, Low, i, ADXvals[9], 0)  # appends new piece of data
    dataStreamHigh10 = flow.dataflow(dataStreamHigh10, High, i, ADXvals[9], 0)  # appends new piece of data
    AroonUp[9], AroonDown[9], counterHigh[9], counterLow[9], highesthigh[9], lowestlow[9] = ind.Aroon(dataStreamHigh10,
                                                                                                      dataStreamLow10,
                                                                                                      len(
                                                                                                          dataStreamLow10),
                                                                                                      counterHigh[9],
                                                                                                      counterLow[9],
                                                                                                      highesthigh[9],
                                                                                                      lowestlow[9])

    Aroonind.append([ind.Aroon_dec(AroonUp[0],AroonDown[0]),ind.Aroon_dec(AroonUp[1],AroonDown[1]),
                 ind.Aroon_dec(AroonUp[2],AroonDown[2]),ind.Aroon_dec(AroonUp[3],AroonDown[3]),
                 ind.Aroon_dec(AroonUp[4],AroonDown[4]),ind.Aroon_dec(AroonUp[5],AroonDown[5]),
                 ind.Aroon_dec(AroonUp[6], AroonDown[6]), ind.Aroon_dec(AroonUp[7], AroonDown[7]),
                 ind.Aroon_dec(AroonUp[8], AroonDown[8]), ind.Aroon_dec(AroonUp[9], AroonDown[9])])
print("Aroon complete")

dataStreamClose = []
dataStreamVolume = []
OBV=[]
for i in range(length-period):
    dataStreamClose = flow.dataflow(dataStreamClose, Close, i, 25, 0)  # appends new piece of data
    dataStreamVolume = flow.dataflow(dataStreamVolume, Volume, i, 25, 0)  # appends new piece of data
    OBV=ind.OBV(dataStreamClose,OBV,dataStreamVolume) ##OBV gets very long should fix
    OBVind.append(ind.decOBV(OBV))
print("On Balance Volume complete")


dataStreamHigh1 = []
dataStreamLow1 = []
dataStreamHigh2 = []
dataStreamLow2 = []
dataStreamHigh3 = []
dataStreamLow3 = []
dataStreamLow4 = []
dataStreamHigh4 = []
dataStreamLow5 = []
dataStreamHigh5 = []
dataStreamLow6 = []
dataStreamHigh6 = []
dataStreamLow7 = []
dataStreamHigh7 = []
dataStreamLow8 = []
dataStreamHigh8 = []
dataStreamLow9 = []
dataStreamHigh9 = []
dataStreamLow10 = []
dataStreamHigh10 = []

for i in range(length-period):
    dataStreamLow1 = flow.dataflow(dataStreamLow1, Low, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamHigh1 = flow.dataflow(dataStreamHigh1, High, i, ADXvals[0], 0)  # appends new piece of data
    dataStreamLow2 = flow.dataflow(dataStreamLow2, Low, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamHigh2 = flow.dataflow(dataStreamHigh2, High, i, ADXvals[1], 0)  # appends new piece of data
    dataStreamLow3 = flow.dataflow(dataStreamLow3, Low, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamHigh3 = flow.dataflow(dataStreamHigh3, High, i, ADXvals[2], 0)  # appends new piece of data
    dataStreamLow4 = flow.dataflow(dataStreamLow4, Low, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamHigh4 = flow.dataflow(dataStreamHigh4, High, i, ADXvals[3], 0)  # appends new piece of data
    dataStreamLow5 = flow.dataflow(dataStreamLow5, Low, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamHigh5 = flow.dataflow(dataStreamHigh5, High, i, ADXvals[4], 0)  # appends new piece of data
    dataStreamLow6 = flow.dataflow(dataStreamLow6, Low, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamHigh6 = flow.dataflow(dataStreamHigh6, High, i, ADXvals[5], 0)  # appends new piece of data
    dataStreamLow7 = flow.dataflow(dataStreamLow7, Low, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamHigh7 = flow.dataflow(dataStreamHigh7, High, i, ADXvals[6], 0)  # appends new piece of data
    dataStreamLow8 = flow.dataflow(dataStreamLow8, Low, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamHigh8 = flow.dataflow(dataStreamHigh8, High, i, ADXvals[7], 0)  # appends new piece of data
    dataStreamLow9 = flow.dataflow(dataStreamLow9, Low, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamHigh9 = flow.dataflow(dataStreamHigh9, High, i, ADXvals[8], 0)  # appends new piece of data
    dataStreamLow10 = flow.dataflow(dataStreamLow10, Low, i, ADXvals[9], 0)  # appends new piece of data
    dataStreamHigh10 = flow.dataflow(dataStreamHigh10, High, i, ADXvals[9], 0)  # appends new piece of data
    if i > ADXvals[len(ADXvals)-1]:
        StocInd.append([ind.stoc_Oc(Close[i], dataStreamLow1, dataStreamHigh1, ADXvals[0], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow2, dataStreamHigh2, ADXvals[1], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow3, dataStreamHigh3, ADXvals[2], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow4, dataStreamHigh4, ADXvals[3], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow5, dataStreamHigh5, ADXvals[4], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow6, dataStreamHigh6, ADXvals[5], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow7, dataStreamHigh7, ADXvals[6], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow8, dataStreamHigh8, ADXvals[7], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow9, dataStreamHigh9, ADXvals[8], 0),
                        ind.stoc_Oc(Close[i], dataStreamLow10, dataStreamHigh10, ADXvals[9], 0)])
    else:
        StocInd.append([.5,.5,.5,.5,.5,.5,.5,.5,.5,.5])
print("Stochastic Oscillator complete")

ADgraph=[]
dataStream=[]
for i in range(length-period):
    ##Chaikin
    dataStream = flow.dataflow(dataStream, Close, i, y[len(y)-1], y[0])  # appends new piece of data
    dec,ADgraph=ind.Chaikin(Close[i], Low[i], High[i], Volume[i],ADgraph,0)
    ChaikinInd.append(dec)
print("Chaikin complete")


print("Printing")

#true="1,0,"
#false="0,1,"
#notsure="0,0,"
'''for i in range(1,len(SMAind[0])+1):
    TrainSet+="SMA Long "+str(i)+",SMA Short "+str(i)+","
for i in range(1,len(EMAind[0])+1):
    TrainSet+="EMA Long "+str(i)+",EMA Short "+str(i)+","
for i in range(1,len(BBind[0])+1):
    TrainSet += "BB Long " + str(i) + ",BB Short " + str(i) + ","
for i in range(1,len(MACDind[0])+1):
    TrainSet += "MACD Long " + str(i) + ",MACD Short " + str(i) + ","
TrainSet+="CMFV Long,CMFV Short,"
TrainSet+="ADline Long,ADline Short,"
TrainSet+="MFI Long,MFI Short,"
for i in range(1,len(ADXind[0])+1):
    TrainSet+="ADX Long "+ str(i)+",ADX Short "+ str(i)+","
for i in range(1,len(Aroonind[0])+1):
    TrainSet+="Aroon Long "+ str(i)+",Aroon Short "+ str(i)+","
for i in range(1,len(OBVind[0])+1):
    TrainSet += "OBV Long " + str(i) + ",OBV short " + str(i) + ","
for i in range(1,len(StocInd[0])+1):
    TrainSet += "Stoch Osc Long " + str(i) + ",Stoch Osc short " + str(i) + ","
for i in range(1,len(ChaikinInd[0])+1):
    TrainSet += "Chaikin Osc Long " + str(i) + ",Chaikin Osc short " + str(i) + ","
TrainSet+="z\n"'''

true="1,"
false="0,"
notsure=".5,"

for i in range(1,len(SMAind[0])+1):
    TrainSet+="SMA "+str(i)+","
for i in range(1,len(EMAind[0])+1):
    TrainSet+="EMA "+str(i)+","
for i in range(1,len(BBind[0])+1):
    TrainSet += "BB " + str(i) + ","
TrainSet+="RSI_5,RSI_10,RSI_15,"
for i in range(1,len(MACDind[0])+1):
    TrainSet += "MACD " + str(i) + ","
TrainSet+="CMFV,"
TrainSet+="ADline,"
TrainSet+="MFI,"
for i in range(1,len(ADXind[0])+1):
    TrainSet+="ADX "+ str(i)+","
for i in range(1,len(Aroonind[0])+1):
    TrainSet+="Aroon "+ str(i)+","
for i in range(1,len(OBVind[0])+1):
    TrainSet += "OBV " + str(i) + ","
for i in range(1,len(StocInd[0])+1):
    TrainSet += "Stoch Osc " + str(i) + ","
for i in range(1,len(ChaikinInd[0])+1):
    TrainSet += "Chaikin Osc " + str(i) + ","
TrainSet+="z,"
TrainSet+="Close\n"

for i in range(largest,len(z)): ##throw away the first y[9] as the SMA's Max length is y[9]
    for j in range(len(SMAind[0])):  ##21 SMA indicators
        if SMAind[i][j]==0:
            TrainSet+=false
        elif SMAind[i][j]==1:
            TrainSet +=true
        else:
            TrainSet +=notsure
    for j in range(len(EMAind[0])):
        if EMAind[i][j]==0:
            TrainSet+=false
        elif EMAind[i][j]==1:
            TrainSet +=true
        else:
            TrainSet +=notsure
    for j in range(len(BBind[0])):
        if BBind[i][j]==0:
            TrainSet+=false
        elif BBind[i][j]==1:
            TrainSet +=true
        else:
            TrainSet += notsure
    for j in range(len(RSIind[0])):
        if RSIind[i][j]>80:
            TrainSet +=false
        elif RSIind[i][j]<20:
            TrainSet +=true
        else:
            TrainSet+=notsure
    for j in range(len(MACDind[0])):
        if MACDind[i][j]==0:
            TrainSet+=false
        elif MACDind[i][j]==1:
            TrainSet +=true
        else:
            TrainSet += notsure
    if CMFVind[i] == 0:
        TrainSet +=false
    elif CMFVind[i] == 1:
        TrainSet +=true
    else:
        TrainSet +=notsure
    if ADlineInd[i] == 0:
        TrainSet +=false
    elif ADlineInd[i] == 1:
        TrainSet +=true
    else:
        TrainSet +=notsure
    if MFIind[i] < .2:
        TrainSet +=true
    elif MFIind[i] > .8:
        TrainSet +=false
    else:
        TrainSet += notsure
    for j in range(len(ADXind[0])):
        if ADXind[i][j] == 0:
            TrainSet +=false
        elif ADXind[i][j] == 1:
            TrainSet +=true
        else:
            TrainSet += notsure
    #print(len(Aroonind),i)
    for j in range(len(Aroonind[0])):
        if Aroonind[i][j] == 0:
            TrainSet += false
        elif Aroonind[i][j] == 1:
            TrainSet += true
        else:
            TrainSet += notsure
    for j in range(len(OBVind[0])):
        if OBVind[i][j] == 0:
            TrainSet += false
        elif OBVind[i][j] == 1:
            TrainSet += true
        else:
            TrainSet += notsure
    for j in range(len(StocInd[0])):
        if StocInd[i][j] == 0:
            TrainSet += false
        elif StocInd[i][j] == 1:
            TrainSet += true
        else:
            TrainSet += notsure
    for j in range(len(ChaikinInd[0])):
        if ChaikinInd[i][j] == 0:
            TrainSet += false
        elif ChaikinInd[i][j] == 1:
            TrainSet += true
        else:
            TrainSet += notsure
    ##Expected output
    if z[i]=="0":
        TrainSet +="0"+","
    elif z[i]=="1":
        TrainSet +="1"+","
    TrainSet+=str(Close[i])+"\n"

if Average:
    with open(f"C:/Users/conor/Desktop/Final year project/Output/trainAv{period}minutestype11.csv", 'a+') as out:
        out.write(TrainSet)
else:
    with open(f"C:/Users/conor/Desktop/Final year project/Output/train{period}minutestype1.csv", 'a+') as out:
        out.write(TrainSet)
