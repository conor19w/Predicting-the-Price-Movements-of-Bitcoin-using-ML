import Data_flow as flow
import TA_indicators as ind
import pandas as pd
import numpy as np
import math
def gen(Open,Close,High,Low,Volume,ADgraphChaikin,OBV,AroonDown,AroonUp,lowestlow,highesthigh,counterLow,counterHigh,CMFVgraph,ADgraph,ADX,pos_DI,neg_DI,CTM,CDMneg,CDMpos,type):
    if type==1 or type==7:
        y = [4, 5, 6, 7, 8, 9, 10, 13, 15, 20]
        y1 = [4, 5, 6,  7, 8, 9, 10,13, 15, 20]
    elif type==2:
        y=[5,10,15,20,25,30,45,60,75,90]
        y1 = [5, 10, 15, 20, 25, 30, 45, 60, 75, 90]
    elif type==3:
        y = [5, 10, 13, 15, 19, 23, 27, 30, 45, 60]
        y1 = [5, 10, 13, 15, 19, 23, 27, 30, 45, 60]
    elif type==4:
        y =[5, 8, 13, 15, 22, 25, 31, 34, 51, 60]
        y1 = [5, 8, 13, 15, 22, 25, 31, 34, 51, 60]
    elif type==5:
        y = [5, 6, 7, 8, 9, 10, 15, 30, 45, 60]
        y1 = [5, 6, 7, 8, 9, 10, 15, 30, 45, 60]
    elif type==6:
        y = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
        y1 = [3,5,8,13,21,34,55,89,144,233]
    elif type==8:
        y = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        y1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    elif type==9:
        y = [4, 6, 7, 9, 10, 13, 15, 17,20,30]
        y1 = [4, 6, 7, 9, 10, 13, 15, 17,20,30]
    elif type==10:
        y = [2,3,4,5,6,7,8,9,10,11]
        y1 = [2,3,4,5,6,7,8,9,10,11]
    elif type==11:
        y = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
        y1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif type==12:
        y = [3, 5, 7, 9, 11, 13, 15, 20, 23, 30]
        y1 = [3, 5, 7, 9, 11, 13, 15, 20, 23, 30]
    indicators = []

    largest = 0

    length = len(Close)
    #SMA
    SMA1 = ind.SMA(Close, y1[0])
    SMA2 = ind.SMA(Close, y1[1])
    SMA3 = ind.SMA(Close, y1[2])
    SMA4 = ind.SMA(Close, y1[3])
    SMA5 = ind.SMA(Close, y1[4])
    SMA6 = ind.SMA(Close, y1[5])
    SMA7 = ind.SMA(Close, y1[6])
    SMA8 = ind.SMA(Close, y1[7])
    SMA9 = ind.SMA(Close, y1[8])
    SMA10 = ind.SMA(Close, y1[9])
    #indicators of up trend
    compSMA_1_2 = ind.find_SMA_crosslive(SMA1, SMA2)
    compSMA_1_3 = ind.find_SMA_crosslive(SMA1, SMA3)
    compSMA_1_4 = ind.find_SMA_crosslive(SMA1, SMA4)
    compSMA_1_5 = ind.find_SMA_crosslive(SMA1, SMA5)
    compSMA_1_6 = ind.find_SMA_crosslive(SMA1, SMA6)
    compSMA_1_7 = ind.find_SMA_crosslive(SMA1, SMA7)
    compSMA_1_8 = ind.find_SMA_crosslive(SMA1, SMA8)
    compSMA_1_9 = ind.find_SMA_crosslive(SMA1, SMA9)
    compSMA_1_10 = ind.find_SMA_crosslive(SMA1, SMA10)
    compSMA_2_3 = ind.find_SMA_crosslive(SMA2, SMA3)
    compSMA_2_4 = ind.find_SMA_crosslive(SMA2, SMA4)
    compSMA_2_5 = ind.find_SMA_crosslive(SMA2, SMA5)
    compSMA_2_6 = ind.find_SMA_crosslive(SMA2, SMA6)
    compSMA_2_7 = ind.find_SMA_crosslive(SMA2, SMA7)
    compSMA_2_8 = ind.find_SMA_crosslive(SMA2, SMA8)
    compSMA_2_9 = ind.find_SMA_crosslive(SMA2, SMA9)
    compSMA_2_10 = ind.find_SMA_crosslive(SMA2, SMA10)
    compSMA_3_4 = ind.find_SMA_crosslive(SMA3, SMA4)
    compSMA_3_5 = ind.find_SMA_crosslive(SMA3, SMA5)
    compSMA_3_6 = ind.find_SMA_crosslive(SMA3, SMA6)
    compSMA_3_7 = ind.find_SMA_crosslive(SMA3, SMA7)
    compSMA_3_8 = ind.find_SMA_crosslive(SMA3, SMA8)
    compSMA_3_9 = ind.find_SMA_crosslive(SMA3, SMA9)
    compSMA_3_10 = ind.find_SMA_crosslive(SMA3, SMA10)
    compSMA_4_5 = ind.find_SMA_crosslive(SMA4, SMA5)
    compSMA_4_6 = ind.find_SMA_crosslive(SMA4, SMA6)
    compSMA_4_7 = ind.find_SMA_crosslive(SMA4, SMA7)
    compSMA_4_8 = ind.find_SMA_crosslive(SMA4, SMA8)
    compSMA_4_9 = ind.find_SMA_crosslive(SMA4, SMA9)
    compSMA_4_10 = ind.find_SMA_crosslive(SMA4, SMA10)
    compSMA_5_6 = ind.find_SMA_crosslive(SMA5, SMA6)
    compSMA_5_7 = ind.find_SMA_crosslive(SMA5, SMA7)
    compSMA_5_8 = ind.find_SMA_crosslive(SMA5, SMA8)
    compSMA_5_9 = ind.find_SMA_crosslive(SMA5, SMA9)
    compSMA_5_10 = ind.find_SMA_crosslive(SMA5, SMA10)
    compSMA_6_7 = ind.find_SMA_crosslive(SMA6, SMA7)
    compSMA_6_8 = ind.find_SMA_crosslive(SMA6, SMA8)
    compSMA_6_9 = ind.find_SMA_crosslive(SMA6, SMA9)
    compSMA_6_10 = ind.find_SMA_crosslive(SMA6, SMA10)
    compSMA_7_8 = ind.find_SMA_crosslive(SMA7, SMA8)
    compSMA_7_9 = ind.find_SMA_crosslive(SMA7, SMA9)
    compSMA_7_10 = ind.find_SMA_crosslive(SMA7, SMA10)
    compSMA_8_9 = ind.find_SMA_crosslive(SMA8, SMA9)
    compSMA_8_10 = ind.find_SMA_crosslive(SMA8, SMA10)
    compSMA_9_10 = ind.find_SMA_crosslive(SMA9, SMA10)

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
    for x in currentSMA:
        indicators.append(x)

        #EMA
    data = pd.Series(Close)
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
    compEMA_1_2 = ind.find_SMA_crosslive(EMA1, EMA2)
    compEMA_1_3 = ind.find_SMA_crosslive(EMA1, EMA3)
    compEMA_1_4 = ind.find_SMA_crosslive(EMA1, EMA4)
    compEMA_1_5 = ind.find_SMA_crosslive(EMA1, EMA5)
    compEMA_1_6 = ind.find_SMA_crosslive(EMA1, EMA6)
    compEMA_1_7 = ind.find_SMA_crosslive(EMA1, EMA7)
    compEMA_1_8 = ind.find_SMA_crosslive(EMA1, EMA8)
    compEMA_1_9 = ind.find_SMA_crosslive(EMA1, EMA9)
    compEMA_1_10 = ind.find_SMA_crosslive(EMA1, EMA10)
    compEMA_2_3 = ind.find_SMA_crosslive(EMA2, EMA3)
    compEMA_2_4 = ind.find_SMA_crosslive(EMA2, EMA4)
    compEMA_2_5 = ind.find_SMA_crosslive(EMA2, EMA5)
    compEMA_2_6 = ind.find_SMA_crosslive(EMA2, EMA6)
    compEMA_2_7 = ind.find_SMA_crosslive(EMA2, EMA7)
    compEMA_2_8 = ind.find_SMA_crosslive(EMA2, EMA8)
    compEMA_2_9 = ind.find_SMA_crosslive(EMA2, EMA9)
    compEMA_2_10 = ind.find_SMA_crosslive(EMA2, EMA10)
    compEMA_3_4 = ind.find_SMA_crosslive(EMA3, EMA4)
    compEMA_3_5 = ind.find_SMA_crosslive(EMA3, EMA5)
    compEMA_3_6 = ind.find_SMA_crosslive(EMA3, EMA6)
    compEMA_3_7 = ind.find_SMA_crosslive(EMA3, EMA7)
    compEMA_3_8 = ind.find_SMA_crosslive(EMA3, EMA8)
    compEMA_3_9 = ind.find_SMA_crosslive(EMA3, EMA9)
    compEMA_3_10 = ind.find_SMA_crosslive(EMA3, EMA10)
    compEMA_4_5 = ind.find_SMA_crosslive(EMA4, EMA5)
    compEMA_4_6 = ind.find_SMA_crosslive(EMA4, EMA6)
    compEMA_4_7 = ind.find_SMA_crosslive(EMA4, EMA7)
    compEMA_4_8 = ind.find_SMA_crosslive(EMA4, EMA8)
    compEMA_4_9 = ind.find_SMA_crosslive(EMA4, EMA9)
    compEMA_4_10 = ind.find_SMA_crosslive(EMA4, EMA10)
    compEMA_5_6 = ind.find_SMA_crosslive(EMA5, EMA6)
    compEMA_5_7 = ind.find_SMA_crosslive(EMA5, EMA7)
    compEMA_5_8 = ind.find_SMA_crosslive(EMA5, EMA8)
    compEMA_5_9 = ind.find_SMA_crosslive(EMA5, EMA9)
    compEMA_5_10 = ind.find_SMA_crosslive(EMA5, EMA10)
    compEMA_6_7 = ind.find_SMA_crosslive(EMA6, EMA7)
    compEMA_6_8 = ind.find_SMA_crosslive(EMA6, EMA8)
    compEMA_6_9 = ind.find_SMA_crosslive(EMA6, EMA9)
    compEMA_6_10 = ind.find_SMA_crosslive(EMA6, EMA10)
    compEMA_7_8 = ind.find_SMA_crosslive(EMA7, EMA8)
    compEMA_7_9 = ind.find_SMA_crosslive(EMA7, EMA9)
    compEMA_7_10 = ind.find_SMA_crosslive(EMA7, EMA10)
    compEMA_8_9 = ind.find_SMA_crosslive(EMA8, EMA9)
    compEMA_8_10 = ind.find_SMA_crosslive(EMA8, EMA10)
    compEMA_9_10 = ind.find_SMA_crosslive(EMA9, EMA10)

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
    for x in currentEMA:
        indicators.append(x)

    #print("SMA & EMA complete")
    ##Bollinger Bands
    if type==1 or type==5 or type==12:
        BBvals=[5,10,13,15,20,30,40,50,60,100]
    elif type==2:
        BBvals = [5, 10, 15, 20, 25, 30, 45, 60, 75, 90]
    elif type==3 or type==4:
        BBvals = [10,20,30,40,50,60,70,80,90,100]
    elif type==6:
        BBvals = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    elif type==7:
        BBvals = [4, 5, 6, 7, 8, 9, 10, 13, 15, 20]
    elif type==8:
        BBvals = [4,5,6,7,8,9,10,11,12,13]
    elif type==9:
        BBvals = [4, 6, 7, 9, 10, 13, 15, 17,20,30]
    elif type==10 or type==11:
        BBvals = [2,3,4,5,6,7,8,9,10,11]
    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[0])
    decision1 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[1])
    decision2 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[2])
    decision3 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[3])
    decision4 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[4]) ##20
    decision5 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[5]) ##30
    decision6 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[6]) ##40
    decision7 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[7]) ##50
    decision8 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[8]) ##60
    decision9 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    bbupperL1, bblowerU1, bbupperU1, bblowerL1 = ind.BB(Close, BBvals[9]) ##100
    decision10 = ind.find_BB_cross(bbupperL1, bblowerU1, bbupperU1, bblowerL1, Close)

    BB = [decision1[0], decision2[0], decision3[0], decision4[0], decision5[0],
            decision6[0], decision7[0], decision8[0], decision9[0], decision10[0]]

    for x in BB:
        indicators.append(x)

    #print("BB complete")
    ##RSI
    dataStream=[]
    dataStream1=[]
    dataStream2=[]
    if  type==1 or type==8 or type==9:
        rsivals=[5,10,15]
    elif type==2 or type==12:
        rsivals = [10,30,60]
    elif type==3:
        rsivals = [10, 20, 30]
    elif type==4:
        rsivals=[15,30,60]
    elif type==5 or type==6:
        rsivals = [5, 15, 30]
    elif type==7:
        rsivals=[5,10,20]
    elif type==10 or type==11:
        rsivals = [3,4,5]
    dataStream = flow.flowLive(Close, rsivals[0])
    dataStream1 = flow.flowLive(Close, rsivals[1])
    dataStream2 = flow.flowLive(Close, rsivals[2])
    decision1 = ind.RSI(dataStream)
    decision2 = ind.RSI(dataStream1)
    decision3 = ind.RSI(dataStream2)
    rsidecision = [decision1, decision2, decision3]
    #print("RSI complete")
    for x in rsidecision:
        if x > 80:
            indicators.append(0)
        elif x < 20:
            indicators.append(1)
        else:
            indicators.append(.5)

    # MACD
    if type==1 or type==5 or type==6 or type==7 or type == 8 or type==9 or type==10 or type==11 or type==12:
        decision1 = ind.MACDsignal(Close, 6, 4, 3, type=0)
        decision2 = ind.MACDsignal(Close, 7, 5, 4, type=0)
        decision3 = ind.MACDsignal(Close, 8, 5, 4, type=0)
        decision4 = ind.MACDsignal(Close, 9, 5, 4, type=0)
        decision5 = ind.MACDsignal(Close, 10, 6, 5, type=0)
        decision6 = ind.MACDsignal(Close, 13, 9, 7, type=0)
        decision7 = ind.MACDsignal(Close, 15, 10, 8, type=0)
        decision8 = ind.MACDsignal(Close, 26, 12, 9, type=0)
        decision9 = ind.MACDsignal(Close, 12, 6, 5, type=0)
        decision10 = ind.MACDsignal(Close, 18, 14, 9, type=0)
    elif type==2 or type==3 or type==4:
        decision1 = ind.MACDsignal(Close, 16, 12, 9, type=0)
        decision2 = ind.MACDsignal(Close, 27, 18, 14, type=0)
        decision3 = ind.MACDsignal(Close, 8, 5, 4, type=0)
        decision4 = ind.MACDsignal(Close, 9, 5, 4, type=0)
        decision5 = ind.MACDsignal(Close, 50, 42, 35, type=0)
        decision6 = ind.MACDsignal(Close, 13, 9, 7, type=0)
        decision7 = ind.MACDsignal(Close, 52, 24, 16, type=0)
        decision8 = ind.MACDsignal(Close, 26, 12, 9, type=0)
        decision9 = ind.MACDsignal(Close, 12, 6, 5, type=0)
        decision10 = ind.MACDsignal(Close, 18, 14, 9, type=0)

    MACD=[decision1[0], decision2[0], decision3[0], decision4[0], decision5[0],
                    decision6[0], decision7[0], decision8[0], decision9[0], decision10[0]]
    for x in MACD:
        indicators.append(x)

    #print("MACD complete")
    ##CMFV
    CMFVgraph = ind.CMFV(CMFVgraph, Close[len(Close)-1], Low[len(Low)-1], High[len(High)-1], Volume[len(Volume)-1])  ##Calculate A/D Line
    decision1 = ind.CMFVInd(CMFVgraph, Close)
    ##ADline
    ADgraph = ind.ADline(ADgraph, Close[len(Close)-1], Low[len(Low)-1], High[len(High)-1], Volume[len(Volume)-1])  ##Calculate A/D Line
    decision2 = ind.ADlineInd(ADgraph, Close)

    CMFV=decision1[0]
    ADline=decision2[0]
    indicators.append(CMFV)
    indicators.append(ADline)

    #print("CMFV & ADline complete")
    if type==1 or type==4 or type==5 or type==6 or type==7 or type==8 or type==9 or type==10 or type==11 or type==12:
        dataStreamClose = flow.flowLive(Close, 15)  # appends new piece of data
        dataStreamLow = flow.flowLive(Low, 15)  # appends new piece of data
        dataStreamHigh = flow.flowLive(High, 15)  # appends new piece of data
        dataStreamVolume = flow.flowLive(Volume, 15)  # appends new piece of data
    elif type==2 or type==3:
        dataStreamClose = flow.flowLive(Close, 20)  # appends new piece of data
        dataStreamLow = flow.flowLive(Low, 20)  # appends new piece of data
        dataStreamHigh = flow.flowLive(High, 20)  # appends new piece of data
        dataStreamVolume = flow.flowLive(Volume, 20)  # appends new piece of data

    MFI = ind.MFI(dataStreamHigh, dataStreamLow, dataStreamClose, dataStreamVolume,
                  len(dataStreamClose))  ##Calculate MFI
    if MFI<.2:
        indicators.append(1)
    elif MFI>.8:
        indicators.append(0)
    else:
        indicators.append(.5)

    #print("MFI complete")
    ##ADX
    if type==1 or type==7:
        ADXvals = [4, 5, 6, 7, 8, 9, 10, 13, 15, 20]
    elif type==2:
        ADXvals=[5, 10, 15, 20, 25, 30, 45, 60, 75, 90]
    elif type==3:
        ADXvals=[5,10,15,20,25,30,35,40,45,50]
    elif type==4:
        ADXvals = [5, 8, 13, 15, 22, 25, 31, 34, 51, 60]
    elif type==5:
        ADXvals = [5, 6, 7, 8, 9, 10, 15, 30, 45, 60]
    elif type==6:
        ADXvals = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    elif type==8:
        ADXvals = [4,5,6,7,8,9,10,11,12,13]
    elif type==9:
        ADXvals = [4, 6, 7, 9, 10, 13, 15, 17, 20, 30]
    elif type==10 or type==11:
        ADXvals = [2,3,4,5,6,7,8,9,10,11]
    elif type==12:
        ADXvals = [5,10,13,15,20,30,40,50,60,100]

    dataStreamClose1 = flow.flowLive(Close,ADXvals[0])  # appends new piece of data
    dataStreamLow1 = flow.flowLive(Low,ADXvals[0])  # appends new piece of data
    dataStreamHigh1 = flow.flowLive(High,ADXvals[0])  # appends new piece of data
    dataStreamClose2 = flow.flowLive(Close,ADXvals[1])  # appends new piece of data
    dataStreamLow2 = flow.flowLive(Low,ADXvals[1])  # appends new piece of data
    dataStreamHigh2 = flow.flowLive(High,ADXvals[1])  # appends new piece of data
    dataStreamClose3 = flow.flowLive(Close,ADXvals[2])  # appends new piece of data
    dataStreamLow3 = flow.flowLive(Low,ADXvals[2])  # appends new piece of data
    dataStreamHigh3 = flow.flowLive(High,ADXvals[2])  # appends new piece of data
    dataStreamClose4 = flow.flowLive(Close,ADXvals[3])  # appends new piece of data
    dataStreamLow4 = flow.flowLive(Low,ADXvals[3])  # appends new piece of data
    dataStreamHigh4 = flow.flowLive(High,ADXvals[3])  # appends new piece of data
    dataStreamClose5 = flow.flowLive(Close,ADXvals[4])  # appends new piece of data
    dataStreamLow5 = flow.flowLive(Low,ADXvals[4])  # appends new piece of data
    dataStreamHigh5 = flow.flowLive(High,ADXvals[4])  # appends new piece of data
    dataStreamClose6 = flow.flowLive(Close,ADXvals[5])  # appends new piece of data
    dataStreamLow6 = flow.flowLive(Low,ADXvals[5])  # appends new piece of data
    dataStreamHigh6 = flow.flowLive(High,ADXvals[5])  # appends new piece of data
    dataStreamClose7 = flow.flowLive(Close,ADXvals[6])  # appends new piece of data
    dataStreamLow7 = flow.flowLive(Low,ADXvals[6])  # appends new piece of data
    dataStreamHigh7 = flow.flowLive(High,ADXvals[6])  # appends new piece of data
    dataStreamClose8 = flow.flowLive(Close,ADXvals[7])  # appends new piece of data
    dataStreamLow8 = flow.flowLive(Low,ADXvals[7])  # appends new piece of data
    dataStreamHigh8 = flow.flowLive(High,ADXvals[7])  # appends new piece of data
    dataStreamClose9 = flow.flowLive(Close,ADXvals[8])  # appends new piece of data
    dataStreamLow9 = flow.flowLive(Low,ADXvals[8])  # appends new piece of data
    dataStreamHigh9 = flow.flowLive(High,ADXvals[8])  # appends new piece of data
    dataStreamClose10 = flow.flowLive(Close,ADXvals[9])  # appends new piece of data
    dataStreamLow10 = flow.flowLive(Low,ADXvals[9])  # appends new piece of data
    dataStreamHigh10 = flow.flowLive(High,ADXvals[9])  # appends new piece of data
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

    ADXdec=[ind.ADXdec(neg_DI[0], pos_DI[0], ADX[0]),ind.ADXdec(neg_DI[1], pos_DI[1], ADX[1]),
         ind.ADXdec(neg_DI[2], pos_DI[2], ADX[2]),ind.ADXdec(neg_DI[3], pos_DI[3], ADX[3]),
         ind.ADXdec(neg_DI[4], pos_DI[4], ADX[4]),ind.ADXdec(neg_DI[5], pos_DI[5], ADX[5]),
         ind.ADXdec(neg_DI[6], pos_DI[6], ADX[6]), ind.ADXdec(neg_DI[7], pos_DI[7], ADX[7]),
         ind.ADXdec(neg_DI[8], pos_DI[8], ADX[8]),ind.ADXdec(neg_DI[9], pos_DI[9], ADX[9])]
    #print("ADX complete")
    for x in ADXdec:
        indicators.append(x)



    dataStreamLow1 = flow.flowLive(Low,ADXvals[0])  # appends new piece of data
    dataStreamHigh1 = flow.flowLive(High,ADXvals[0])  # appends new piece of data
    AroonUp[0], AroonDown[0], counterHigh[0], counterLow[0], highesthigh[0], lowestlow[0] = ind.Aroon(dataStreamHigh1,
                                                                                                      dataStreamLow1,
                                                                                                      len(
                                                                                                          dataStreamLow1),
                                                                                                      counterHigh[0],
                                                                                                      counterLow[0],
                                                                                                      highesthigh[0],
                                                                                                      lowestlow[0])

    dataStreamLow2 = flow.flowLive(Low,ADXvals[1])  # appends new piece of data
    dataStreamHigh2 = flow.flowLive(High,ADXvals[1])  # appends new piece of data
    AroonUp[1], AroonDown[1], counterHigh[1], counterLow[1], highesthigh[1], lowestlow[1] = ind.Aroon(dataStreamHigh2,
                                                                                                      dataStreamLow2,
                                                                                                      len(
                                                                                                          dataStreamLow2),
                                                                                                      counterHigh[1],
                                                                                                      counterLow[1],
                                                                                                      highesthigh[1],
                                                                                                      lowestlow[1])

    dataStreamLow3 = flow.flowLive(Low,ADXvals[2])  # appends new piece of data
    dataStreamHigh3 = flow.flowLive(High,ADXvals[2])  # appends new piece of data
    AroonUp[2], AroonDown[2], counterHigh[2], counterLow[2], highesthigh[2], lowestlow[2] = ind.Aroon(dataStreamHigh3,
                                                                                                      dataStreamLow3,
                                                                                                      len(
                                                                                                          dataStreamLow3),
                                                                                                      counterHigh[2],
                                                                                                      counterLow[2],
                                                                                                      highesthigh[2],
                                                                                                      lowestlow[2])

    dataStreamLow4 = flow.flowLive(Low,ADXvals[3])  # appends new piece of data
    dataStreamHigh4 = flow.flowLive(High,ADXvals[3])  # appends new piece of data
    AroonUp[3], AroonDown[3], counterHigh[3], counterLow[3], highesthigh[3], lowestlow[3] = ind.Aroon(dataStreamHigh4,
                                                                                                      dataStreamLow4,
                                                                                                      len(
                                                                                                          dataStreamLow4),
                                                                                                      counterHigh[3],
                                                                                                      counterLow[3],
                                                                                                      highesthigh[3],
                                                                                                      lowestlow[3])

    dataStreamLow5 = flow.flowLive(Low,ADXvals[4])  # appends new piece of data
    dataStreamHigh5 = flow.flowLive(High,ADXvals[4])  # appends new piece of data
    AroonUp[4], AroonDown[4], counterHigh[4], counterLow[4], highesthigh[4], lowestlow[4] = ind.Aroon(dataStreamHigh5,
                                                                                                      dataStreamLow5,
                                                                                                      len(
                                                                                                          dataStreamLow5),
                                                                                                      counterHigh[4],
                                                                                                      counterLow[4],
                                                                                                      highesthigh[4],
                                                                                                      lowestlow[4])

    dataStreamLow6 = flow.flowLive(Low,ADXvals[5])  # appends new piece of data
    dataStreamHigh6 = flow.flowLive(High,ADXvals[5])  # appends new piece of data
    AroonUp[5], AroonDown[5], counterHigh[5], counterLow[5], highesthigh[5], lowestlow[5] = ind.Aroon(dataStreamHigh6,
                                                                                                      dataStreamLow6,
                                                                                                      len(
                                                                                                          dataStreamLow6),
                                                                                                      counterHigh[5],
                                                                                                      counterLow[5],
                                                                                                      highesthigh[5],
                                                                                                      lowestlow[5])

    dataStreamLow7 = flow.flowLive(Low,ADXvals[6])  # appends new piece of data
    dataStreamHigh7 = flow.flowLive(High,ADXvals[6])  # appends new piece of data
    AroonUp[6], AroonDown[6], counterHigh[6], counterLow[6], highesthigh[6], lowestlow[6] = ind.Aroon(dataStreamHigh7,
                                                                                                      dataStreamLow7,
                                                                                                      len(
                                                                                                          dataStreamLow7),
                                                                                                      counterHigh[6],
                                                                                                      counterLow[6],
                                                                                                      highesthigh[6],
                                                                                                      lowestlow[6])

    dataStreamLow8 = flow.flowLive(Low,ADXvals[7])  # appends new piece of data
    dataStreamHigh8 = flow.flowLive(High,ADXvals[7])  # appends new piece of data
    AroonUp[7], AroonDown[7], counterHigh[7], counterLow[7], highesthigh[7], lowestlow[7] = ind.Aroon(dataStreamHigh8,
                                                                                                      dataStreamLow8,
                                                                                                      len(
                                                                                                          dataStreamLow8),
                                                                                                      counterHigh[7],
                                                                                                      counterLow[7],
                                                                                                      highesthigh[7],
                                                                                                      lowestlow[7])

    dataStreamLow9 = flow.flowLive(Low,ADXvals[8])  # appends new piece of data
    dataStreamHigh9 = flow.flowLive(High,ADXvals[8])  # appends new piece of data
    AroonUp[8], AroonDown[8], counterHigh[8], counterLow[8], highesthigh[8], lowestlow[8] = ind.Aroon(dataStreamHigh9,
                                                                                                      dataStreamLow9,
                                                                                                      len(
                                                                                                          dataStreamLow9),
                                                                                                      counterHigh[8],
                                                                                                      counterLow[8],
                                                                                                      highesthigh[8],
                                                                                                      lowestlow[8])

    dataStreamLow10 = flow.flowLive(Low,ADXvals[9])  # appends new piece of data
    dataStreamHigh10 = flow.flowLive(High,ADXvals[9])  # appends new piece of data
    AroonUp[9], AroonDown[9], counterHigh[9], counterLow[9], highesthigh[9], lowestlow[9] = ind.Aroon(dataStreamHigh10,
                                                                                                      dataStreamLow10,
                                                                                                      len(
                                                                                                          dataStreamLow10),
                                                                                                      counterHigh[9],
                                                                                                      counterLow[9],
                                                                                                      highesthigh[9],
                                                                                                      lowestlow[9])

    Aroon=[ind.Aroon_dec(AroonUp[0],AroonDown[0]),ind.Aroon_dec(AroonUp[1],AroonDown[1]),
                 ind.Aroon_dec(AroonUp[2],AroonDown[2]),ind.Aroon_dec(AroonUp[3],AroonDown[3]),
                 ind.Aroon_dec(AroonUp[4],AroonDown[4]),ind.Aroon_dec(AroonUp[5],AroonDown[5]),
                 ind.Aroon_dec(AroonUp[6], AroonDown[6]), ind.Aroon_dec(AroonUp[7], AroonDown[7]),
                 ind.Aroon_dec(AroonUp[8], AroonDown[8]), ind.Aroon_dec(AroonUp[9], AroonDown[9])]
    for x in Aroon:
        indicators.append(x)

    #print("Aroon complete")

    ##OBV
    OBV = ind.OBV(Close, OBV,Volume)  ##OBV gets very long should fix
    OBVdec=ind.decOBV(OBV)
    for x in OBVdec:
        indicators.append(x)

    dataStreamLow1 = flow.flowLive(Low,ADXvals[0])  # appends new piece of data
    dataStreamHigh1 = flow.flowLive(High,ADXvals[0])  # appends new piece of data
    dataStreamLow2 = flow.flowLive(Low,ADXvals[1])  # appends new piece of data
    dataStreamHigh2 = flow.flowLive(High,ADXvals[1])  # appends new piece of data
    dataStreamLow3 = flow.flowLive(Low,ADXvals[2])  # appends new piece of data
    dataStreamHigh3 = flow.flowLive(High,ADXvals[2])  # appends new piece of data
    dataStreamLow4 = flow.flowLive(Low,ADXvals[3])  # appends new piece of data
    dataStreamHigh4 = flow.flowLive(High,ADXvals[3])  # appends new piece of data
    dataStreamLow5 = flow.flowLive(Low,ADXvals[4])  # appends new piece of data
    dataStreamHigh5 = flow.flowLive(High,ADXvals[4])  # appends new piece of data
    dataStreamLow6 = flow.flowLive(Low,ADXvals[5])  # appends new piece of data
    dataStreamHigh6 = flow.flowLive(High,ADXvals[5])  # appends new piece of data
    dataStreamLow7 = flow.flowLive(Low,ADXvals[6])  # appends new piece of data
    dataStreamHigh7 = flow.flowLive(High,ADXvals[6])  # appends new piece of data
    dataStreamLow8 = flow.flowLive(Low,ADXvals[7])  # appends new piece of data
    dataStreamHigh8 = flow.flowLive(High,ADXvals[7])  # appends new piece of data
    dataStreamLow9 = flow.flowLive(Low,ADXvals[8])  # appends new piece of data
    dataStreamHigh9 = flow.flowLive(High,ADXvals[8])  # appends new piece of data
    dataStreamLow10 = flow.flowLive(Low,ADXvals[9])  # appends new piece of data ##60
    dataStreamHigh10 = flow.flowLive(High,ADXvals[9])  # appends new piece of data ##60
    StocInd=[ind.stoc_Oc(Close[len(Close)-1], dataStreamLow1, dataStreamHigh1, ADXvals[0], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow2, dataStreamHigh2, ADXvals[1], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow3, dataStreamHigh3, ADXvals[2], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow4, dataStreamHigh4, ADXvals[3], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow5, dataStreamHigh5, ADXvals[4], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow6, dataStreamHigh6, ADXvals[5], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow7, dataStreamHigh7, ADXvals[6], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow8, dataStreamHigh8, ADXvals[7], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow9, dataStreamHigh9, ADXvals[8], 0),
                        ind.stoc_Oc(Close[len(Close)-1], dataStreamLow10, dataStreamHigh10, ADXvals[9], 0)] ##59
    for x in StocInd:
        indicators.append(x)

    #print("OBV complete")
    dataStream = []
    ##Chaikin
    dec, ADgraphChaikin = ind.Chaikin(Close[len(Close)-1], Low[len(Low)-1], High[len(High)-1], Volume[len(Volume)-1], ADgraphChaikin, 0)
    Chaikin=dec
    #print("Chaikin complete")
    for x in Chaikin:
        indicators.append(x)


    df=pd.DataFrame(data={'SMA 1':indicators[0],'SMA 2':indicators[1],'SMA 3':indicators[2],'SMA 4':indicators[3],'SMA 5':indicators[4],
                                'SMA 6':indicators[5],'SMA 7':indicators[6],'SMA 8':indicators[7],'SMA 9':indicators[8],'SMA 10':indicators[9],
                                'SMA 11':indicators[10],'SMA 12':indicators[11],'SMA 13':indicators[12],'SMA 14':indicators[13],'SMA 15':indicators[14],
                                'SMA 16':indicators[15],'SMA 17':indicators[16],'SMA 18':indicators[17],'SMA 19':indicators[18],'SMA 20':indicators[19],
                                'SMA 21':indicators[20],'SMA 22':indicators[21],'SMA 23':indicators[22],'SMA 24':indicators[23],'SMA 25':indicators[24],
                                'SMA 26':indicators[25],'SMA 27':indicators[26],'SMA 28':indicators[27],'SMA 29':indicators[28],'SMA 30':indicators[29],
                                'SMA 31':indicators[30],'SMA 32':indicators[31],'SMA 33':indicators[32],'SMA 34':indicators[33],'SMA 35':indicators[34],
                                'SMA 36':indicators[35],'SMA 37':indicators[36],'SMA 38':indicators[37],'SMA 39':indicators[38],'SMA 40':indicators[39],
                                'SMA 41':indicators[40],'SMA 42':indicators[41],'SMA 43':indicators[42],'SMA 44':indicators[43],'SMA 45':indicators[44],
                                'EMA 1':indicators[45],'EMA 2':indicators[46],'EMA 3':indicators[47],'EMA 4':indicators[48],'EMA 5':indicators[49],
                                'EMA 6':indicators[50],'EMA 7':indicators[51],'EMA 8':indicators[52],'EMA 9':indicators[53],'EMA 10':indicators[54],
                                'EMA 11':indicators[55],'EMA 12':indicators[56],'EMA 13':indicators[57],'EMA 14':indicators[58],'EMA 15':indicators[59],
                                'EMA 16':indicators[60],'EMA 17':indicators[61],'EMA 18':indicators[62],'EMA 19':indicators[63],'EMA 20':indicators[64],
                                'EMA 21':indicators[65],'EMA 22':indicators[66],'EMA 23':indicators[67],'EMA 24':indicators[68],'EMA 25':indicators[69],
                                'EMA 26':indicators[70],'EMA 27':indicators[71],'EMA 28':indicators[72],'EMA 29':indicators[73],'EMA 30':indicators[74],
                                'EMA 31':indicators[75],'EMA 32':indicators[76],'EMA 33':indicators[77],'EMA 34':indicators[78],'EMA 35':indicators[79],
                                'EMA 36':indicators[80],'EMA 37':indicators[81],'EMA 38':indicators[82],'EMA 39':indicators[83],'EMA 40':indicators[4],
                                'EMA 41':indicators[85],'EMA 42':indicators[86],'EMA 43':indicators[87],'EMA 44':indicators[88],'EMA 45':indicators[89],
                                'BB 1':indicators[90],'BB 2':indicators[91],'BB 3':indicators[92],'BB 4':indicators[93],'BB 5':indicators[94],
                                'BB 6':indicators[95],'BB 7':indicators[96],'BB 8':indicators[97],'BB 9':indicators[98],'BB 10':indicators[99],
                                'RSI_5':indicators[100],'RSI_10':indicators[101],'RSI_15':indicators[102],
                                'MACD 1':indicators[103],'MACD 2':indicators[104],'MACD 3':indicators[105],'MACD 4':indicators[106],'MACD 5':indicators[107],
                                'MACD 6':indicators[108],'MACD 7':indicators[109],'MACD 8':indicators[110],'MACD 9':indicators[111],'MACD 10':indicators[112],
                                'CMFV':indicators[113],'ADline':indicators[114],'MFI':indicators[115],
                                'ADX 1':indicators[116],'ADX 2':indicators[117],'ADX 3':indicators[118],'ADX 4':indicators[119],'ADX 5':indicators[120],
                                'ADX 6':indicators[121],'ADX 7':indicators[122],'ADX 8':indicators[123],'ADX 9':indicators[124],'ADX 10':indicators[125],
                                'Aroon 1':indicators[126],'Aroon 2':indicators[127],'Aroon 3':indicators[128],'Aroon 4':indicators[129],'Aroon 5':indicators[130],
                                'Aroon 6':indicators[131],'Aroon 7':indicators[132],'Aroon 8':indicators[133],'Aroon 9':indicators[134],'Aroon 10':indicators[135],
                                'OBV 1':indicators[136],'OBV 2':indicators[137],'OBV 3':indicators[138],'OBV 4':indicators[139],'OBV 5':indicators[140],'OBV 6':indicators[141],'OBV 7':indicators[142],
                                'Stoch Osc 1':indicators[143],'Stoch Osc 2':indicators[144],'Stoch Osc 3':indicators[145],'Stoch Osc 4':indicators[146],'Stoch Osc 5':indicators[147],
                                'Stoch Osc 6':indicators[148],'Stoch Osc 7':indicators[149],'Stoch Osc 8':indicators[150],'Stoch Osc 9':indicators[151],'Stoch Osc 10':indicators[152],
                                'Chaikin Osc 1':indicators[153],'Chaikin Osc 2':indicators[154],'Chaikin Osc 3':indicators[155],'Chaikin Osc 4':indicators[156],'Chaikin Osc 5':indicators[157],
                                'Chaikin Osc 6':indicators[158],'Chaikin Osc 7':indicators[159],'Chaikin Osc 8':indicators[160],'Chaikin Osc 9':indicators[161]},index=[0])


    return df,ADgraphChaikin,OBV,AroonDown,AroonUp,lowestlow,highesthigh,counterLow,counterHigh,CMFVgraph,ADgraph,ADX,pos_DI,neg_DI,CTM,CDMneg,CDMpos