#ini adalah tools seadanya karena saya dalam tahap belajar

import random
import os
import sys
os.system("clear ")
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0)
mengetik("|---------------||-----------||---------------|")
mengetik("|---------------||- loading -||---------------|")
mengetik("|---------------||-----------||---------------|")
print("")
print("------------------------------------------")
print ("anda menggunakan tools ini")
print ("pada :")
os.system("date")
print("------------------------------------------")

import sys,time
def run(teks):
    putih = "\033[0m"
    merah = "\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write('\r%s%s%s%s' % (putih,char.lower(),merah,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.5)
            num += 1
    except: exit()

run("xxxxxxxxxxx")
print("")
print("|----------------------------------------------|")
os.system("figlet download ")
print("|----------------------------------------------|")
print("")
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.8)
mengetik("  [<^><^><^><^><^><^><^><^><^><^><^><^><^><^>]")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik("  [==========================================]")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik("  [<^><^><^><^><^><^><^><^><^><^><^><^><^><^>]")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik("  [==========================================]")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik("  [<^><^><^><^><^><^><^><^><^><^><^><^><^><^>]")
print("")
print("|----------------------------------------------|")
os.system("figlet selesai")
print("|----------------------------------------------|")

import sys,time
def spin():
        try:
                L="/-\\|"
                for q in range(20):
                        time.sleep(0.2)
                        sys.stdout.write("\r["+L[q % len(L)]+"]")
                        sys.stdout.flush()
        except:
                exit()

spin()

import os
import sys
os.system("clear ")

def main():
	os.system("figlet andhika")
	os.system("date")
	banner="""
	[=================]
	[+]owner : andhika
	[+]tgl   : 29/04/25
	[+]wa    : -
	[=================]
	"""
	print(banner)
main()
def menu():
	print(""" 
	| + |             animasi                  |
        | 1 | api
	| 2 | hujan tulisan
	| 3 | kreta lewat
	| 0 | exit 
	""")
menu()
def melu():
	print(""" 
	| + |            informasi                 |
	| 4 | info hp anda
	| 0 | exit 
	""")
melu()
def meni():
	print(""" 
	| + |              game                    |
	| 1A | main mobil-mobilan
	| 2A | tetris
	| 3A |
	| 4A |
	| 5A |
	| 6A |
	| 7A |
	| 8A | ninvadres
	| 9A | ular
	| 0  | exit 
	""")
meni()
def menu2():
        print("""
        | + |              cuaca                  |
        | A | sidoarjo   
        | B | surabaya 
        | C | ngawi
        | D | blitar
        | E | nganjuk
        | 0 | exit
        """)
menu2()
     
pilih = raw_input("nomor : ")
if pilih =="":
	os.system(" clear")
	print "pilihan tidak ada"
	os.system("python2 andhika.py")
	
if pilih =="1":
    os.system("clear")
    print "download.."
    sleep(1.5)
    os.system("pkg install libcaca")
    os.system("clear")
    os.system("cacafire")
	
if pilih =="2":
    os.system("clear")
    print "download.."
    os.system("pkg install cmatrix")
    os.system("cmatrix")
    
if pilih =="3":
    os.system("clear")
    print "download.."
    os.system("pkg install sl")
    os.system("clear")
    os.system("sl")
    
#============ info =========================

if pilih =="4":
    os.system("clear")
    os.system("figlet download ")
    os.system("pkg install neofetch")
    os.system("clear")
    os.system("neofetch")
    
#============ game =========================
    
if pilih =="1A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install moon-buggy")
    print ("nah udah selesai selamat bermain")
    os.system("moon-buggy")
    
if pilih =="2A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install bastet")
    os.system("clear")
    os.system("bastet")
    
if pilih =="3A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install curseofwar")
    os.system("clear")
    os.system("curseofwar")
    
if pilih =="4A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install gnugo")
    os.system("clear")
    os.system("gnugo")
    
if pilih =="5A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install greed")
    os.system("clear")
    os.system("greed")
    
if pilih =="6A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install nudoku")
    os.system("clear")
    os.system("nudoku")
    
if pilih =="7A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install nethack")
    os.system("clear")
    os.system("nethack")
    
if pilih =="8A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install ninvaders")
    os.system("clear")
    os.system("ninvaders")
    
if pilih =="9A":
    os.system("clear")
    print ("download dulu pak sabar")
    os.system("pkg install nsnake")
    os.system("clear")
    os.system("nsnake")
    
#=========== cuaca ==========================
    
if pilih =="A":
	os.system("clear")
	print ("perkiraan cuaca sidoarjo ")
	os.system("curl http://wttr.in/sidoarjo")
	
if pilih =="B":
	os.system("clear")
	print ("perkiraan cuaca surabaya ")
	os.system("curl http://wttr.in/surabaya")
	
if pilih =="C":
	os.system("clear")
	print ("perkiraan cuaca ngawi")
	os.system("curl http://wttr.in/ngawi")
	
if pilih =="D":
	os.system("clear")
	print ("perkiraan cuaca blitar ")
	os.system("curl http://wttr.in/blitar ")
    
if pilih =="E":
	os.system("clear")
	print ("perkiraan cuaca nganjuk ")
	os.system("curl http://wttr.in/nganjuk ")
    
if pilih =="0":
     os.system("clear")
     print "okhe siap bos"
import sys,time
def spin():
        try:
                L="/-\\|"
                for q in range(20):
                        time.sleep(0.1)
                        sys.stdout.write("\r["+L[q % len(L)]+"]")
                        sys.stdout.flush()
        except:
                exit()

spin()
print ("")