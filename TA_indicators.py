import pandas as pd
import math
############# SMA generate data for a simple moving average of a specified window size ################

def SMA(data,window_size):
    data_series=pd.Series(data)
    windows = data_series.rolling(window_size)
    moving_averages= windows.mean()

    moving_averages_list=moving_averages.tolist()
    #without_nans = moving_averages_list[window_size-1:]
    # return without_nans
    return moving_averages_list #keep nans so graph is correct on return
########################################


############ Find the crosses of two SMA's ##################

def find_SMA_cross(SMA_short,SMA_long):
    if SMA_short[len(SMA_short)-1]>SMA_long[len(SMA_long)-1]:
        return [1,len(SMA_short)-1]
    elif SMA_long[len(SMA_long)-1]>SMA_short[len(SMA_short)-1]:
        return [0,len(SMA_long)-1]
    else:
        return[.5,-99]


def find_SMA_crosslive(SMA_short,SMA_long):
    if (SMA_short[len(SMA_short)-1]>SMA_long[len(SMA_long)-1]) and (SMA_short[len(SMA_short)-2]<SMA_long[len(SMA_long)-2]) :
        return [1,len(SMA_short)-1]
    elif (SMA_long[len(SMA_long)-1]>SMA_short[len(SMA_short)-1]) and (SMA_long[len(SMA_long)-2]<SMA_short[len(SMA_short)-2]):
        return [0,len(SMA_long)-1]
    else:
        return[.5,-99]


   # length = len(SMA_long)
   # decision=-99
   # price=0
    #flag=-99
   # for i in range(length):
    #    #print(SMA_long[i], SMA_short[i])
    #    if (SMA_short[i] < SMA_long[i]) and (flag == 1 or flag==-99):
    #        flag = 0
    #        decision= 0     #false to sell
    #        price=i   #index of cross between SMA's used to determine price to buy at

    #    elif (SMA_short[i] > SMA_long[i]) and (flag == 0 or flag==-99):
    #        flag = 1
    #        decision = 1    #True to buy
    #        price = i         #index of cross between SMA's used to determine price to buy at
   # return [decision,length-price]
##########################################


########## Generate SMA's & make decision #############

def superSMA(data,y):
    SMA1=SMA(data,y[0])
    SMA2=SMA(data,y[1])
    SMA3=SMA(data,y[2])
    SMA4=SMA(data,y[3])
    SMA5=SMA(data,y[4])
    SMA6=SMA(data,y[5])
    buy=-1
    sell=-1

    compSMA_1_2 = find_SMA_cross(SMA1,SMA2)
    compSMA_1_3 = find_SMA_cross(SMA1,SMA3)
    compSMA_1_4 = find_SMA_cross(SMA1, SMA4)
    compSMA_1_5 = find_SMA_cross(SMA1, SMA5)
    compSMA_1_6 = find_SMA_cross(SMA1,SMA6)
    compSMA_2_3 = find_SMA_cross(SMA2, SMA3)
    compSMA_2_4 = find_SMA_cross(SMA2, SMA4)
    compSMA_2_5 = find_SMA_cross(SMA2, SMA5)
    compSMA_2_6 = find_SMA_cross(SMA2,SMA6)
    compSMA_3_4 = find_SMA_cross(SMA3,SMA4)
    compSMA_3_5 = find_SMA_cross(SMA3,SMA5)
    compSMA_3_6 = find_SMA_cross(SMA3,SMA6)
    compSMA_4_5 = find_SMA_cross(SMA4,SMA5)
    compSMA_4_6 = find_SMA_cross(SMA4,SMA6)
    compSMA_5_6 = find_SMA_cross(SMA5,SMA6)
    for x in [compSMA_1_2,compSMA_1_3,compSMA_1_4,
              compSMA_1_5,compSMA_1_6,compSMA_2_3,
              compSMA_2_4,compSMA_2_5,compSMA_2_6,
              compSMA_3_4,compSMA_3_5,compSMA_3_6,
              compSMA_4_5,compSMA_4_6,compSMA_5_6]:
        if x[0]:
            if x[1]>buy:
                buy=x[1]
        elif not(x[0]):
            if x[1]>sell:
                sell=x[1]
    #should return the most recent signal
    if sell > buy >= 0:
        return [1,buy]
    elif buy > sell >= 0:
        return [0,sell]
    else:
        return [-1,0]

#######################################################################

#######################################################################
#######################################################################
#######################################################################

###################### Exponential moving average #####################
def EMA(data,window_size):
    data1= data.ewm(span=window_size,adjust=True).mean()
    return data1.to_numpy()


def superEMA(data,y):
    data=pd.Series(data)
    EMA1=EMA(data,y[0])
    EMA2=EMA(data,y[1])
    EMA3=EMA(data,y[2])
    EMA4=EMA(data,y[3])
    EMA5=EMA(data,y[4])
    EMA6=EMA(data,y[5])
    buy=-1
    sell=-1

    compEMA_1_2 = find_SMA_cross(EMA1,EMA2)
    compEMA_1_3 = find_SMA_cross(EMA1,EMA3)
    compEMA_1_4 = find_SMA_cross(EMA1, EMA4)
    compEMA_1_5 = find_SMA_cross(EMA1, EMA5)
    compEMA_1_6 = find_SMA_cross(EMA1,EMA6)
    compEMA_2_3 = find_SMA_cross(EMA2, EMA3)
    compEMA_2_4 = find_SMA_cross(EMA2, EMA4)
    compEMA_2_5 = find_SMA_cross(EMA2, EMA5)
    compEMA_2_6 = find_SMA_cross(EMA2,EMA6)
    compEMA_3_4 = find_SMA_cross(EMA3,EMA4)
    compEMA_3_5 = find_SMA_cross(EMA3,EMA5)
    compEMA_3_6 = find_SMA_cross(EMA3,EMA6)
    compEMA_4_5 = find_SMA_cross(EMA4,EMA5)
    compEMA_4_6 = find_SMA_cross(EMA4,EMA6)
    compEMA_5_6 = find_SMA_cross(EMA5,EMA6)
    for x in [compEMA_1_2,compEMA_1_3,compEMA_1_4,
              compEMA_1_5,compEMA_1_6,compEMA_2_3,
              compEMA_2_4,compEMA_2_5,compEMA_2_6,
              compEMA_3_4,compEMA_3_5,compEMA_3_6,
              compEMA_4_5,compEMA_4_6,compEMA_5_6]:
        if x[0]:
            if x[1]>buy:
                buy=x[1]
        elif not(x[0]):
            if x[1]>sell:
                sell=x[1]
    #should return the most recent signal
    if sell < buy < 999999:
        return [1,buy]
    elif buy < sell <999999:
        return [0,sell]
    else:
        return [-1,0]

#########################################################################
#########################################################################
#########################################################################
################ Bollinger Bands ####################################

def BB(Data,windowSize):
    ### median band
    data_series = pd.Series(Data)
    sma=SMA(Data,windowSize)
    smaStd=data_series.rolling(window=windowSize).std() ##for calculating upper and lower bands

    Upper_lower=sma+smaStd
    Upper_upper=sma+smaStd*2.4
    Lower_lower=sma-smaStd*1.8
    Lower_upper =sma-smaStd

    return Upper_lower,Lower_upper,Upper_upper,Lower_lower

#################################################################

def find_BB_cross(BBupperL,BBlowerU,BBupperU,BBlowerL,data):
    length = len(BBupperL)
    decision=.5 ##unsure what to do
    price=0


    for i in range(length):
        ## Check if the data is below lowerband
        if (BBlowerL[i] < data[i] < BBlowerU[i]) or (data[i]>BBupperU[i]):
            decision = 0
            price = i
        ##Check if the data is above Upperband
        if (BBupperL[i] < data[i] < BBupperU[i]) or (data[i]<BBlowerL[i]):
            decision = 1
            price = i
        if BBlowerU[i]<data[i]<BBupperL[i]:
            decision = .5
            price = i
    if length<10:
        for i in range(length):
            ##Check if the data is above upper
            if data[i]>BBupperU[i]:
                return [0, i]
            ##Check if the data is below lower
            if data[i]<BBlowerL[i]:
                return [1, i]
    elif length>=10:
        for i in range(length-10,length):
            ##Check if the data is above upper
            if data[i]>BBupperU[i]:
                return [0, i]
            ##Check if the data is below lower
            if data[i]<BBlowerL[i]:
                return [1, i]

    return [decision, price]


#######################################################################################
########################################################################################
############################### RSI ##############################################
## taken from Stack overFlow https://stackoverflow.com/questions/20526414/relative-strength-index-in-python-pandas
def RSI(close):
    down=0
    downcount=0
    up=0
    upcount=0
    for i in range(1,len(close)):
        if close[i]-close[i-1]<0:
            down+=abs(close[i]-close[i-1])
            downcount+=1
        elif close[i]-close[i-1]>0:
            up+=abs(close[i]-close[i-1])
            upcount+=1
    if upcount!=0 and downcount!=0 and up!=0 and down!=0:
        AverageUp=up/upcount
        AverageDown=down/downcount
        RSIval=(100-(100/(1+(AverageUp/AverageDown))))
    else:
        RSIval=50
    return RSIval

#######################################################################################
######################################################################################
######################### MACD #######################################################

def MACDsignal(data1,large,small,sline_len,type):
    data = pd.Series(data1)
    emaLarge = EMA(data, large)
    emaSmall = EMA(data, small)
    mLine = emaSmall-emaLarge
    sLine = EMA(pd.Series(mLine),sline_len)
    if type==0:
        return find_SMA_cross(mLine,sLine)  ##find where they cross
    else:
        return [mLine[len(mLine)-1],sLine[len(sLine)-1]] #mLine,sLine


###########################################################################################
######################### Accumilation Distribution line ##################################
'''def ADline(ADgraph,Close,Low,High,Volume): ##lots of NaNs with this
    ##Scale factor on volume might remove later
    if High - Low != 0:
        CMFV=(((Close-Low)-(High-Close))/(High-Low))*Volume ##Current Money Flow Volume
    #print(CMFV)
    #print(Close,Low,High,Volume)
    if len(ADgraph)==0 and High-Low!=0:
        ADgraph.append(CMFV)
    elif High-Low==0:
        if len(ADgraph)==0:
            ADgraph.append(0)
        else:
            ADgraph.append(ADgraph[len(ADgraph) - 1])
    else:
        ADgraph.append(ADgraph[len(ADgraph) - 1] + CMFV)

    #print(ADgraph[len(ADgraph)-1])
    return ADgraph'''

def ADlineInd(ADgraph,data):
    i=len(ADgraph)-1
    j=len(data)-1
    if i>=2:
        #print(ADgraph[i]-ADgraph[i-1])
        if data[j]<data[j-1]:
            #print("change in data: ",data[j]-data[j-1])
            if ADgraph[i]>ADgraph[i-1]:
                return [1,len(data)-1]
            else:
                return [.5, -99]
        elif data[j]>data[j-1]:
            #print("change in data: ", data[j] - data[j - 1])
            if ADgraph[i]<ADgraph[i-1]:
                return [0,len(data)-1]
            else:
                return [.5, -99]
        else:
            return [.5, -99]
    else:
        return [.5,-99]


def ADline(ADgraph, Close, Low, High, Volume):  ##lots of NaNs with this
    ##Scale factor on volume might remove later
    if High - Low != 0:
        CMFV = (((Close - Low) - (High - Close)) / (High - Low)) * Volume  ##Current Money Flow Volume
    # print(CMFV)
    # print(Close,Low,High,Volume)
    if len(ADgraph) == 0 and High - Low != 0:
        ADgraph.append(CMFV)
    elif High - Low == 0:
        if len(ADgraph) == 0:
            ADgraph.append(0)
        else:
            ADgraph.append(ADgraph[len(ADgraph) - 1])
    else:
        ADgraph.append(ADgraph[len(ADgraph) - 1] + CMFV)
    slidingwindow = []
    if len(ADgraph) >= 100:  ## ensure data doesnt grow too large
        for i in range(len(ADgraph) - 99, len(ADgraph)):
            slidingwindow.append(ADgraph[i])
        return slidingwindow
    # print(ADgraph[len(ADgraph)-1])
    else:
        return ADgraph
############################################################################################
########################### Current Money Flow Volume ######################################
############################################################################################

def CMFV(CMFVgraph,Close,Low,High,Volume): ##lots of NaNs with this
    if High - Low != 0:
        CMFV1 = (((Close - Low) - (High - Close)) / (High - Low)) * Volume  ##Current Money Flow Volume
    if len(CMFVgraph)==0 and High-Low!=0:
        CMFVgraph.append(CMFV1)
    elif High - Low != 0:
        if len(CMFVgraph) == 0:
            CMFVgraph.append(0)
        else:
            CMFVgraph=[CMFVgraph[len(CMFVgraph)-1],CMFV1]
    else:
        if len(CMFVgraph)==0:
            CMFVgraph.append(0)
        else:
            CMFVgraph = [CMFVgraph[len(CMFVgraph) - 1], CMFVgraph[len(CMFVgraph) - 1]]
    return CMFVgraph

def CMFVInd(CMFVgraph,data):
    i=len(CMFVgraph)-1
    if i>=2:
        if CMFVgraph[i]-CMFVgraph[i-1]>0 :
            return [1,len(data)-1]
        elif CMFVgraph[i]-CMFVgraph[i-1]<0 :
            return [0,len(data)-1]
        else:
            return [.5, -99]
    else:
        return [.5,-99]
#############################################################################################
################################## Money Flow Index #########################################
#############################################################################################

def MFI(High,Low,Close,Volume,period):
    Pos_MF=0
    Neg_MF=0
    for i in range(period):
        typical_price=(High[i]+Low[i]+Close[i])/3
        Money_flow=typical_price*Volume[i]
        if Close[i]>Close[i-1]:
            Pos_MF+=Money_flow
        else:
            Neg_MF+=Money_flow

    MF_Ratio=Pos_MF/Neg_MF
    MFI = round((100-(100/(1+MF_Ratio)))/100,3)

    return MFI

#############################################################################################
######################## Directional Movement Index & ADX ###################################
#############################################################################################
def DI(High,Low,Close,CDMpos,CDMneg,CTM,ADX):
    pos_DM=[]
    neg_DM=[]
    TR=[]
    sumDMpos=0
    sumDMneg=0
    sumTR=0
    flag=0
    for i in range(1,len(High)):
        if High[i] - High[i - 1]>Low[i-1]-Low[i]:
            pos_DM.append(High[i]-High[i-1])
            neg_DM.append(0)
        else:
            neg_DM.append(Low[i-1]-Low[i])
            pos_DM.append(0)
        temp=High[i]-Low[i]
        for x in [abs(High[i]-Close[i-1]),abs(Low[i]-Close[i-1])]:
            if temp<x:
                temp=x
        TR.append(temp)
    ##Smooth the DM's
    for x in pos_DM:
        sumDMpos+=x
    smoothDMpos=(sumDMpos+sumDMpos/len(High))+CDMpos  ##Smoothed negative DM
    for x in neg_DM:
        sumDMneg+=x
    smoothDMneg=(sumDMneg+sumDMneg/len(High))+CDMneg  ##Smoothed positive DM
    for x in TR:
        sumTR+=x
    if CTM==0:
        CTM=sumTR ##Initial true range
    else:
        CTM=CTM-(CTM/len(High))+TR[len(TR)-1] ##current smoothed true range
    if CTM!=0:
        pos_DI=(smoothDMpos/CTM)*100 ##positive directional index
        neg_DI=(smoothDMneg/CTM)*100 ##negative directional index
    else:
        neg_DI=0
        pos_DI=0
    if pos_DI==0 and neg_DI==0  or (pos_DI+neg_DI==0):
        DIval=0
    else:
        DIval=(abs(pos_DI-neg_DI)/abs(pos_DI+neg_DI))*100

    if ADX==0:
        ADX=DIval/len(High)
    else:
        ADX=((len(High)-1)*ADX+DIval)/len(High)
    ##If ADX over 25=> strong trend
    ##If ADX below 20=> weak trend
    ##If -DI crosses +DI & ADX>20 signal buy
    ##If +DI crosses -DI & ADX>20 siganl sell

    return ADX,pos_DI,neg_DI,CTM,CDMneg,CDMpos

def ADXdec(neg_DI,pos_DI,ADX):
    dec=.5
    if neg_DI<pos_DI and ADX>20:
        dec=1 ##long
    elif pos_DI<neg_DI and ADX>20:
        dec=0 ##short
    return dec

#############################################################################################
########################        Aroon         ###############################################
#############################################################################################

def Aroon(High,Low,period,counterhigh,counterlow,highesthigh,lowestlow):
    if counterhigh==period:
        counterhigh=0
    if counterlow==period:
        counterlow=0

    for x in High:
        if x>highesthigh:
            highesthigh=x
            counterhigh=0
    for x in Low:
        if x<lowestlow:
            lowestlow=x
            counterlow=0

    AroonUp=((period-counterhigh)/period)*100
    Aroondown = ((period - counterlow) / period) * 100
    counterhigh+=1
    counterlow+=1

    return AroonUp,Aroondown,counterhigh,counterlow,highesthigh,lowestlow

def Aroon_dec(AroonUp,Aroondown):
    if AroonUp>Aroondown:
        return 1
    elif AroonUp<Aroondown:
        return 0
    else:
        return .5


#############################################################################################
########################        On Balance Volume         ###################################
#############################################################################################

def OBV(Close,OBV,Volume):
    if len(OBV)==0:
        OBV.append(0)
        return OBV
    else:
        if Close[len(Close)-1]>Close[len(Close)-2]:
            OBV.append(OBV[len(OBV)-1]+Volume[len(Volume)-1])
        elif Close[len(Close)-1]<Close[len(Close)-2]:
            OBV.append(OBV[len(OBV)-1]-Volume[len(Volume)-1])
        else:
            OBV.append(OBV[len(OBV) - 1])
    slidingwindow=[]
    if len(OBV)>=len(Close): ## ensure data doesnt grow too large
       for i in range(len(OBV)-len(Close)-1,len(OBV)):
           slidingwindow.append(OBV[i])
       return slidingwindow
    else:
        return OBV


def decOBV(OBV):
    dec=[]
    if len(OBV)>1:
        ### One Minute Period
        if OBV[len(OBV) - 1]>OBV[len(OBV) - 2]:
            dec.append(1)
        elif OBV[len(OBV) - 1]<OBV[len(OBV) - 2]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)

    if len(OBV)>2:
        ##two Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 3]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 3]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)

    if len(OBV)>4:
        ##three Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 4]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 4]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)
    if len(OBV)>5:
        ##four Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 5]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 5]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)
    if len(OBV)>7:
        ##seven Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 8]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 8]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)
    if len(OBV)>10:
        ##ten Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 11]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 11]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)
    if len(OBV)>15:
        ##twenty Minute Period
        if OBV[len(OBV) - 1] > OBV[len(OBV) - 21]:
            dec.append(1)
        elif OBV[len(OBV) - 1] < OBV[len(OBV) - 21]:
            dec.append(0)
        else:
            dec.append(.5)
    else:
        dec.append(.5)

    return dec

##############################################################################################
########################## Stochastic Oscillator #############################################
##############################################################################################

def stoc_Oc(Close,Low,High,window,type):
    Lowest1=Low[0]
    for i in range(1,len(Low)):
        if Lowest1>Low[i]:
            Lowest1=Low[i]
    Highest1=High[0]
    for i in range(1, len(High)):
        if Highest1 < High[i]:
            Highest1 = High[i]
    if Highest1 - Lowest1 != 0:
        K=((Close-Lowest1)/(Highest1-Lowest1))*100
    elif Highest1-Lowest1==0:
        K=50
    Lowest2 = Low[len(Low)-1]
    for i in range(len(Low)-window-1, len(Low)-1):
        if Lowest2 > Low[i]:
            Lowest2 = Low[i]
    Highest2 = High[len(High)-1]
    for i in range(len(High)-window-1, len(High)-1):
        if Highest2 < High[i]:
            Highest2 = High[i]
    if Highest2 - Lowest2 != 0:
        D = ((Close - Lowest2) / (Highest2 - Lowest2)) * 100
    elif Highest2-Lowest2==0:
        D=50
    if type==0:
        if K>80 and D>80:
            return 0
        elif K<20 and D<20:
            return 1
        else:
            return .5
    else:
        return [K,D]

##############################################################################################
########################## Chaikin Oscillator ###############################################
##############################################################################################

def Chaikin(Close,Low,High,Volume,ADgraph,type):
    dec=[]
    ADgraph=ADline(ADgraph, Close, Low, High, Volume)
    ADgraph1=pd.Series(ADgraph)
    #print(ADgraph)
    EMA3=EMA(ADgraph1,3)
    EMA10=EMA(ADgraph1,10)

    ChaikinOsc=EMA3-EMA10
    if type==0:
        if len(ChaikinOsc)>20:
            ##1 period
            if ChaikinOsc[len(ChaikinOsc)-1]>ChaikinOsc[len(ChaikinOsc)-2]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc)-1]<ChaikinOsc[len(ChaikinOsc)-2]:
                dec.append(0)
            else:
                dec.append(.5)
            ##2 periods
            if ChaikinOsc[len(ChaikinOsc)-1]>ChaikinOsc[len(ChaikinOsc)-3]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc)-1]<ChaikinOsc[len(ChaikinOsc)-3]:
                dec.append(0)
            else:
                dec.append(.5)
            ##5 periods
            if ChaikinOsc[len(ChaikinOsc)-1]>ChaikinOsc[len(ChaikinOsc)-6]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc)-1]<ChaikinOsc[len(ChaikinOsc)-6]:
                dec.append(0)
            else:
                dec.append(.5)
            ##8 periods
            if ChaikinOsc[len(ChaikinOsc)-1]>ChaikinOsc[len(ChaikinOsc)-9]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc)-1]<ChaikinOsc[len(ChaikinOsc)-9]:
                dec.append(0)
            else:
                dec.append(.5)
            ##10 periods
            if ChaikinOsc[len(ChaikinOsc) - 1] > ChaikinOsc[len(ChaikinOsc) - 11]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc) - 1] < ChaikinOsc[len(ChaikinOsc) - 11]:
                dec.append(0)
            else:
                dec.append(.5)
            ##12 periods
            if ChaikinOsc[len(ChaikinOsc) - 1] > ChaikinOsc[len(ChaikinOsc) - 13]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc) - 1] < ChaikinOsc[len(ChaikinOsc) - 13]:
                dec.append(0)
            else:
                dec.append(.5)
            ##14 periods
            if ChaikinOsc[len(ChaikinOsc) - 1] > ChaikinOsc[len(ChaikinOsc) - 15]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc) - 1] < ChaikinOsc[len(ChaikinOsc) - 15]:
                dec.append(0)
            else:
                dec.append(.5)
            ##16 periods
            if ChaikinOsc[len(ChaikinOsc) - 1] > ChaikinOsc[len(ChaikinOsc) - 17]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc) - 1] < ChaikinOsc[len(ChaikinOsc) - 17]:
                dec.append(0)
            else:
                dec.append(.5)
            ##19 periods
            if ChaikinOsc[len(ChaikinOsc) - 1] > ChaikinOsc[len(ChaikinOsc) - 20]:
                dec.append(1)
            elif ChaikinOsc[len(ChaikinOsc) - 1] < ChaikinOsc[len(ChaikinOsc) - 20]:
                dec.append(0)
            else:
                dec.append(.5)
        else:
            dec=[.5,.5,.5,.5,.5,.5,.5,.5,.5]
    else:
        return ChaikinOsc,ADgraph
        #if len(ChaikinOsc)>17:
            #dec=[ChaikinOsc[len(ChaikinOsc)-1],ChaikinOsc[len(ChaikinOsc)-2],ChaikinOsc[len(ChaikinOsc)-16]]#,ChaikinOsc[len(ChaikinOsc)-6],ChaikinOsc[len(ChaikinOsc)-9]]
        #else:
            #dec=[0,0,0]#,0,0]
    return dec,ADgraph
