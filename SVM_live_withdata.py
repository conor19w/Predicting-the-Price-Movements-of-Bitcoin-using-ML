import bitmex
import numpy as np
import pandas as pd
from joblib import dump, load
from Super_svm import SuperSVM
import Data_flow as flow
import Gen_inputs as indic


##Train SVM
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
###########Params for generating predictions##################
Time=60 ##interval in seconds to trade over, data was trained over 1-minute periods hence 60 seconds
BBSize=100 ##default 100
type=2 ## Model type

###############################################################
y=[]
X=[]
z=[]


######Params for picking SVM#########
##Bot settings
OrderSize=1000 ##How many 1-dollar contracts to trade
machine=f"DT1type11" ##Machine name for loading a model
stoploss=0 ##Stop losses
stoplossval=250 ##Value to stop losses at
takeprofit=0 ##If on we will take profit above the take profit value below
takeprofitvalue=250

###########################################

machineName=machine
printing=1 ## print to a file

###########################################
totalTime=1440 ##how many minutes to run for

######################################
softopen1=0   ##pretend trade for a certain amount of time before trading on bitmex
softopenTime=10  ##Time to pretend trade over
testtrading=0  #connect to testnet
print("Contracts: ",OrderSize)
print("Time: ",Time)

if stoploss==0:
    stoplossval = 0
if takeprofit==0:
    takeprofitvalue=0
#####################################
print(machine)
svc=f'{machine}.joblib'
with open(f"{machineName}.SL{stoplossval}.TP{takeprofitvalue}.csv",'a+') as out: ##Print headers to file
    out.write("time,     super price,    decision,   Profit,     PV\n")

svclassifier = load(svc)  ##For Loading a model


file=f'{machineName}Mistakes.csv'

if stoploss:
    print("Stop Loss value: ",stoplossval)
#print(machine)
##Live DATA
import asyncio
import time
import websockets
from datetime import datetime, date, timedelta
from json import loads as jsdec
from os import system
if testtrading:
    ##Testnet
    client=bitmex.bitmex(test=True,api_key='',api_secret='') ##need valid api keys to use this

errorCount = 0
data = {}
websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XBTUSD"  ##bitcoin order books
subTopic = "orderBook10:XBTUSD"

## Some other order books we could trade: Etherium, DOGE coin, Cardano, Ripple
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:ETHUSD"
#subTopic = "orderBook10:ETHUSD"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:DOGEUSDT"
#subTopic = "orderBook10:DOGEUSDT"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:ADAH21"
#subTopic = "orderBook10:ADAH21"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XRPUSD"
#subTopic = "orderBook10:XRPUSD"
system('title ' + websocket_url + " channel:" + subTopic)

##Buffer of last n data points needed to calculate signals
OS = load('OpenStream.joblib')
CS = load('CloseStream.joblib')
HS = load('HighStream.joblib')
LS = load('LowStream.joblib')
VS = load('VolumeStream.joblib')
async def runWS():
    async with websockets.connect(websocket_url) as websocket:
        global gCount
        global data
        ######## Variables passed to and from gen inputs to get signals#################
        count = 0
        Open = 0.0
        High = -99999999.0
        Low = 99999999.0
        Close = 0.0
        Volume = 0
        start =datetime.now().time()
        yesterdate = date.today()
        counterHigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        counterLow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        highesthigh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lowestlow = [99999999, 99999999, 99999999, 99999999, 99999999, 99999999, 99999999, 99999999, 99999999,
                     99999999]
        AroonUp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        AroonDown = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        OBV = []
        ADgraphChaikin=[]
        CMFVgraph=[]
        ADgraph=[]
        ADX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pos_DI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        neg_DI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        CTM = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        CDMneg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        CDMpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #####################################################################################

        OpenStream = []
        CloseStream = []
        HighStream = []
        LowStream = []
        VolumeStream = []
        startflag=0  ##just starting simulation
        Profit = 0 ##Keep track of total profit
        prevProfit=0  ##Profit before last trade
        currentPosition = -99  ##initialized as -99 at start
        prevposition=-99    ##initialized as -99 at start
        positionPrice = 0  ##keep track of price we bought/ sold at
        prevpositionPrice=0 ##keep track of price we bought/ sold at last trade
        lookback=300 ##how much of a buffer is needed
        tradesNO=0  ##number of trades weve made
        flag=1  ##print length of datastream if just starting up
        timeCount = 0
        trading = 1  ##Used for switching exiting trading
        previndicators="" ##needed to keep track of mistakes
        softopen=softopen1
        svclassifier = load(svc)  ##For Loading a model

        while True:

            tickerEnc = await websocket.recv()
            tickerEnc = jsdec(tickerEnc)
            data=str(tickerEnc)
            if data[0:4]=="{'ta":
                a = (data.split("'asks': [["))[1]
                b = a.split(", ")
                askprice=float(b[0])
                c=b[1].split("]")
                askvol=float(c[0])
                askvol2=float(b[3].split("]")[0])
                askvol3=float(b[5].split("]")[0])
                askvol4=float(b[7].split("]")[0])
                askvol5=float(b[9].split("]")[0])
                d = (data.split("'bids': [["))[1]
                e = d.split(", ")
                bidprice=float(e[0])
                f=e[1].split("]")
                bidvol=float(f[0])
                bidvol2=float(e[3].split("]")[0])
                bidvol3=float(e[5].split("]")[0])
                bidvol4=float(e[7].split("]")[0])
                bidvol5=float(e[9].split("]")[0])
                totalaskvol=askvol*5+askvol2*4+askvol3*3+askvol4*2+askvol5*1
                totalbidvol=bidvol*5+bidvol2*4+bidvol3*3+bidvol4*2+bidvol5*1
                midprice=(askprice+bidprice)/2
                fee=(midprice*0.001+0.5)/2
                totalvolume=totalaskvol+totalbidvol
                superprice=midprice-fee+(totalbidvol/(totalbidvol+totalaskvol))*fee*2
                g = (data.split("'timestamp': '"))[1]
                h = g.split("'")
                Price=superprice
                rightnow = datetime.now().time()
                sec = timedelta(hours=0, minutes=0, seconds=1)
                if(datetime.combine(date.today(), rightnow)-datetime.combine(yesterdate, start))>sec:
                    start=datetime.now().time()
                    yesterdate=date.today()
                    if count==Time: ##1-minute has passed
                        timeCount+=1 ##how many minutes weve been trading for
                        if startflag==0:
                            OpenStream=flow.dataStream(OS,Open,0,lookback)
                            CloseStream=flow.dataStream(CS, Close,0,lookback)
                            HighStream=flow.dataStream(HS, High,0,lookback)
                            LowStream=flow.dataStream(LS, Low,0,lookback)
                            VolumeStream=flow.dataStream(VS, Volume,0,lookback)
                            startflag=1
                        else:
                            OpenStream = flow.dataStream(OpenStream, Open,0,lookback)
                            CloseStream = flow.dataStream(CloseStream, Close,0,lookback)
                            HighStream = flow.dataStream(HighStream, High,0,lookback)
                            LowStream = flow.dataStream(LowStream, Low,0,lookback)
                            VolumeStream = flow.dataStream(VolumeStream, Volume,0,lookback)

                        if flag != 0:
                            print("Buffer Length: " ,len(OpenStream))
                            print(machine,": ","time, super price, decision, Profit, PV")
                        #print(OpenStream)
                        #print("Close", Close)
                        if (len(OpenStream)>BBSize and type!=6) or (len(OpenStream)>233 and type==6):
                            flag = 0
                            if trading:
                                indicators,ADgraphChaikin,OBV,AroonDown,AroonUp,lowestlow,highesthigh,counterLow,counterHigh,CMFVgraph,ADgraph,ADX,pos_DI,neg_DI,CTM,CDMneg,CDMpos=\
                                indic.gen(OpenStream,CloseStream,HighStream,LowStream,VolumeStream,ADgraphChaikin,OBV,AroonDown,AroonUp,
                                      lowestlow,highesthigh,counterLow,counterHigh,CMFVgraph,ADgraph,ADX,pos_DI,neg_DI,CTM,CDMneg,CDMpos,type=type)
                                prediction1=svclassifier.predict(indicators)
                                prediction=[prediction1[0]]


                                ##Track positions and profit
                                if takeprofit:
                                    if currentPosition==1 and (Price-positionPrice>takeprofitvalue):
                                        currentPosition=4 ##wait for next 0 signal
                                        if  testtrading and not softopen:
                                            client.Order.Order_new(symbol='XBTUSD',orderQty=-OrderSize, price=round(superprice*2/2)).result()
                                        Profit += (Price - positionPrice)*OrderSize/Price  ##This will be positive if the price went up
                                        positionPrice =Price

                                    elif currentPosition==0 and (positionPrice-Price>takeprofitvalue):
                                        currentPosition=3 ##wait for next 1 signal
                                        if  testtrading and not softopen:
                                            client.Order.Order_new(symbol='XBTUSD', orderQty=OrderSize, price=round(superprice*2/2)).result()
                                        Profit += (positionPrice-Price)*OrderSize/Price  ##This will be positive if the price went up
                                        positionPrice =Price


                                if currentPosition == -99 and prediction[0] == 0:
                                    if  testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=-OrderSize, price=round(superprice*2/2)).result()
                                    positionPrice = Price
                                    currentPosition = 0
                                    tradesNO+=1
                                    previndicators = ""
                                    for x in indicators.to_numpy()[0]:
                                        previndicators += str(x) + ","
                                    if prediction[0] == 1:
                                        previndicators += "0,0\n"
                                    else:
                                        previndicators += "1,0\n"
                                ##currentposition==-99 simulation just starting &&
                                ##Day1_pred[i]==1 we want to enter long position
                                elif currentPosition == -99 and prediction[0] == 1:
                                    if  testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=OrderSize, price=round(superprice*2/2)).result()
                                    positionPrice = Price
                                    currentPosition = 1
                                    tradesNO += 1
                                    previndicators = ""
                                    for x in indicators.to_numpy()[0]:
                                        previndicators += str(x) + ","
                                    if prediction[0] == 1:
                                        previndicators += "0,0\n"
                                    else:
                                        previndicators += "1,0\n"
                                ##currentPosition==1 we are currently in a long position &&
                                ##Day1_pred[i]==0 we want to enter short position
                                elif currentPosition == 1 and prediction[0] == 0:
                                    if testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=-2*OrderSize, price=round(superprice*2/2)).result()
                                    Profit += (Price - positionPrice)*OrderSize/Price  ##This will be positive if the price went up
                                    positionPrice = Price
                                    currentPosition = 0
                                    tradesNO += 1
                                    if Profit < prevProfit:
                                        with open(
                                                file,
                                                'a+') as out:
                                            out.write(previndicators)
                                        previndicators = ""
                                        for x in indicators.to_numpy()[0]:
                                            previndicators += str(x) + ","
                                        if prediction[0] == 1:
                                            previndicators += "0,0\n"
                                        else:
                                            previndicators += "1,0\n"


                                ##currentPosition==0 we are currently in a short position &&
                                ##Day1_pred[i]==1 we want to enter long position
                                elif currentPosition == 0 and prediction[0] == 1:
                                    if testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=2*OrderSize, price=round(superprice*2/2)).result()
                                    Profit += (positionPrice-Price)*OrderSize/Price ##This will be positive if the price went down
                                    positionPrice = Price
                                    currentPosition = 1
                                    tradesNO += 1
                                    if Profit < prevProfit:
                                        with open(
                                                file,
                                                'a+') as out:
                                            out.write(previndicators)
                                        previndicators = ""
                                        for x in indicators.to_numpy()[0]:
                                            previndicators += str(x) + ","
                                        if prediction[0] == 1:
                                            previndicators += "0,0\n"
                                        else:
                                            previndicators += "1,0\n"


                                if currentPosition == 0 and (Price-positionPrice>stoplossval) and stoploss:
                                    print(Price - positionPrice)
                                    ##Price went up stop loss
                                    if testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=2*OrderSize).result()
                                    Profit += (positionPrice-Price)*OrderSize/Price  ##This will be positive if the price went down
                                    positionPrice = 0
                                    currentPosition = 3 ## 3 wait for prediction[0] == 1
                                    tradesNO += 1
                                    if Profit<prevProfit:
                                        with open(file,
                                                'a+') as out:
                                            out.write(previndicators)
                                        previndicators = ""
                                elif currentPosition == 1 and (Price - positionPrice < -1*stoplossval) and stoploss:
                                    print(Price-positionPrice)
                                    if  testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=-2*OrderSize).result()
                                    Profit += (Price - positionPrice)*OrderSize/Price ##This will be positive if the price went up
                                    positionPrice = 0
                                    currentPosition = 4 ## 4 wait for prediction[0] == 0
                                    tradesNO += 1
                                    if Profit<prevProfit:
                                        with open(file,
                                                'a+') as out:
                                            out.write(previndicators)
                                        previndicators = ""
                                if currentPosition==3 and prediction[0] == 1:
                                    if  testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=OrderSize, price=round(superprice*2/2)).result()
                                    positionPrice = Price
                                    currentPosition = 1
                                    tradesNO += 1
                                    previndicators = ""
                                    for x in indicators.to_numpy()[0]:
                                        previndicators += str(x) + ","
                                    if prediction[0] == 1:
                                        previndicators += "0,0\n"
                                    else:
                                        previndicators += "1,0\n"
                                elif currentPosition==4 and prediction[0] == 0:
                                    if  testtrading and not softopen:
                                        client.Order.Order_new(symbol='XBTUSD', orderQty=-OrderSize, price=round(superprice*2/2)).result()
                                    positionPrice = Price
                                    currentPosition = 0
                                    tradesNO += 1
                                    previndicators = ""
                                    for x in indicators.to_numpy()[0]:
                                        previndicators += str(x) + ","
                                    if prediction[0] == 1:
                                        previndicators += "0,0\n"
                                    else:
                                        previndicators += "1,0\n"


                                if currentPosition!=prevposition:
                                    print(machine,": ",rightnow,",",Price,",",currentPosition,",",Profit,",",(Profit/tradesNO)*100/OrderSize)
                                    with open(f"{machineName}.SL{stoplossval}.TP{takeprofitvalue}.csv",
                                                  'a+') as out:
                                                out.write(str(rightnow)+","+str(Price)+","+str(currentPosition)+","+str(Profit)+","+str((Profit/tradesNO)*100/OrderSize)+"\n")

                                prevposition = currentPosition
                                prevProfit = Profit
                                if timeCount>totalTime:
                                    trading=0
                                if softopen and timeCount>softopenTime:
                                    softopen=0
                                    Profit=0
                                    prevProfit=0
                                    currentPosition=-99
                                    positionPrice=0
                                    tradesNO=0
                                    print("Soft Open Over...")
                            else:
                                print("Finished")

                        count=0
                        Open=0.0
                        High=-99999999.0
                        Low=99999999.0
                        Close=0.0
                        Volume=0

                    if count==0:
                        Open=superprice
                    if superprice>High:
                        High=superprice
                    if superprice<Low:
                        Low=superprice
                    if count==Time-1:
                        Close=superprice
                    Volume+=totalvolume
                    count+=1


def run():
    try:
        asyncio.get_event_loop().run_until_complete(runWS())
    except Exception as e:
        global x
        x=e
        print(e)
        global errorCount
        errorCount +=1
        print("Error in websocket, retrying, attempt #" + str(errorCount) + "\n" + str(type(e)) + "\t" +str(e))
        time.sleep(1)
        run()

run()