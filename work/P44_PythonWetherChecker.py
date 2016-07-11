import RPI.GPIO asGPIO
from urllib.request import urlopen
from bs4 import BeautifulSoup
GPIO.setmode(GPIO.BOARD)
//databox=urlopen(http://soramame.taiki.go.jp/DataList.php?MstCode=13102010).read()
databox=urlopen(http://soramame.taiki.go.jp/DataList.php?MstCode=24207510).read()

targetUrl="http://soramame.taiki.go.jp/"+htmldatabox.frameset.findAll("frame")[1]["src"]
databox2=urlopen(targetUrl).read()
htmldatabox2=BeautifulSoup(databox2,"html.parser")

yy=htmldatabox2.find("table").find("tr").find("td").find("table").findAdd("td")[0].get_text()
mm=htmldatabox2.find("table").find("tr").find("td").find("table").findAdd("td")[1].get_text()
dd=htmldatabox2.find("table").find("tr").find("td").find("table").findAdd("td")[2].get_text()
hh=htmldatabox2.find("table").find("tr").find("td").find("table").findAdd("td")[3].get_text()
no2=htmldatabox2.find("table").find("tr").find("td").find("table").findAdd("td")[6].get_text()

print("YYMMDDSSNO2:"+str(yy)+"-"+str(mm)+"/"+str(dd)+":"+str(hh)+">"str(no2)+"ppm")
if float(no2) <0.06:
	print ("No problem!")
else:
	print("Attention! Over limit NO2.Please do action !")
	//GPIO.setup(40,GPIO.OUT)
	//GPIO.output(40,0)
GPIO.cleanup()
