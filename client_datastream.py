import asyncio
import time
import websockets
import Data_flow as flow
from datetime import datetime, date, timedelta
from json import loads as jsdec
from os import system
from joblib import dump, load
#client=bitmex.bitmex(test=True,api_key='VKUn3ZGkg2G_IaM5XbBmSiZ8',api_secret='W7thQTv8vT_IOcO4KQWukI9PWu8sq7O4MZZKIQf5rLA2ZgP-')
errorCount = 0
data = {}
websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XBTUSD"
subTopic = "orderBook10:XBTUSD"
Time=60
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:ETHUSD"
#subTopic = "orderBook10:ETHUSD"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:DOGEUSDT"
#subTopic = "orderBook10:DOGEUSDT"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:ADAH21"
#subTopic = "orderBook10:ADAH21"
#websocket_url = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XRPUSD"
#subTopic = "orderBook10:XRPUSD"
print(subTopic)
system('title ' + websocket_url + " channel:" + subTopic)

async def runWS():
    async with websockets.connect(websocket_url) as websocket:
        global gCount
        global data
        count = 0
        Open = 0.0
        High = -99999999.0
        Low = 99999999.0
        Close = 0.0
        Volume = 0
        start =datetime.now().time()
        yesterdate = date.today()
        OpenStream=[]
        CloseStream=[]
        HighStream=[]
        LowStream=[]
        VolumeStream=[]
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
                rightnow = datetime.now().time()
                sec = timedelta(hours=0, minutes=0, seconds=1)
                if(datetime.combine(date.today(), rightnow)-datetime.combine(yesterdate, start))>sec:
                    start=datetime.now().time()
                    yesterdate=date.today()
                    if count==Time:
                        OpenStream=flow.dataStream(OpenStream,Open,0,2880)
                        CloseStream=flow.dataStream(CloseStream, Close,0,2880)
                        HighStream=flow.dataStream(HighStream, High,0,2880)
                        LowStream=flow.dataStream(LowStream, Low,0,2880)
                        VolumeStream=flow.dataStream(VolumeStream, Volume,0,2880)
                        dump(OpenStream, 'OpenStream.joblib')
                        dump(CloseStream, 'CloseStream.joblib')
                        dump(HighStream, 'HighStream.joblib')
                        dump(LowStream, 'LowStream.joblib')
                        dump(VolumeStream, 'VolumeStream.joblib')
                        with open('C:\\Users\\conor\\Desktop\\Final year project\\Output\\extractedBitcoin_13.03.2021.csv', 'a+') as out:
                                out.write(str(datetime.now().replace(second=0,microsecond=0)) + ",")
                                out.write(str(Open) + ", ")
                                out.write(str(High)+", ")
                                out.write(str(Low) + ", ")
                                out.write(str(Close) + ", ")
                                out.write(str(Volume) + "\n")
                        count=0
                        Open=0.0
                        High=-99999999.0
                        Low=99999999.0
                        Close=0.0
                        Volume=0
                        #print("DataStream Size: ",len(OpenStream))
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

