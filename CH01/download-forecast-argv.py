import sys
import urllib3

if len(sys.argv) <= 1:
    print("USAGE: download-forcast-argv <Region Number")
    sys.exit()
regionNumber = sys.argv[1]

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
arg = {
	"stnId" : regionNumber
}

http = urllib3.PoolManager()
r = http.request("GET", url, arg, preload_content=False)

if r.status == 200:
	print(r.read().decode())