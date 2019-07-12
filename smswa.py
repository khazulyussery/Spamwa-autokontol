from twilio.rest import Client
import os, sys
from time import sleep

print("\033[1;31m\n[!] Opening Tool...")
sleep(1.5)
os.system("clear")
print("\033[1;36mAssalamualaikum ...(^_^)")
sleep(2)
def khazul():

		print("\033[1;37m")
		os.system('clear')
		print("""
      ++++++++++++++++++++
   Unlimited Spam Auto Kontol
      ++++++++++++++++++++
		     """)

		print("[01] Mulai\n[02] Setting\n[03] My Profile")
		pil=input("\nPilih =>> ")
		if pil =="1" or pil =="01":
			os.system('clear')
			account_sid = 'ACc0b8e954a764631a7acb7eab0bbba8ba'
			auth_token = 'ee334872688c8ae43abb8885f389c3c2'
			msg='DASAR KONTOLL!!!'
			no=input("Nomor (use +62):\n> ")
			print("")
		elif pil =="2" or pil =="02":
			os.system('clear')
			print("""	  Information\n
Kenapa toolnya gak work?dan kenapa gak
bisa kirim ke nomor lain?

Nah kalian harus tau kalau tool ini
masih menggunakan trial akun yang
dimana toolnya akan bekerja pada
nomor-nomor yang sudah verif dalam akun
trial tersebut.

lalu bagaimana cara menambahkannya?

Untuk menambahkan nomor lain kalian
bisa langsung mengunjungi website resmi
di https://twillio.com. kalian bisa
daftar terlebih dahulu untuk kalian
yang belum memiliki akun setelah itu
kalian bisa login dan masuk ke
dashbornya. Pada menu bar tepatnya 
pada sisi kiri atas kalian klik dan 
cari bacaannya number setelah itu
kalian tambahkan dan selanjutnya cs
twillio akan mengirimkan sebuah kode
verifikasi. dan kalian bisa
memasukkan kode tersebut pada kolom
verifikasi.

terima kasih...
			""")
			while True:
				a=input("\nMau kembali lagi?(y/n)")
				if a == "y":
					return khazul()
				elif a=="n":
					exit ("\nSampai ketemu lagi..")
		elif pil =="3" or pil =="03":
				os.system('clear')
				print("""	Khazul Yussery Shadiq\n      IT Support & Programming
\nHai guys perkenalkan namaku adalah\nkhazul yussery shadiq aku tamatan dari\nSMK Swasta Teladan Medan jurusan Teknik Komputer dan Jaringan.\nKalau kalian mau kenal lebih dekat\nDenganku, kalian bisa add wa aku\n082360303930\n\nTerima Kasih...""")
				while True:
					ul=input("\nMau kembali?(y/n)")
					if ul=="y":
						return khazul()
					elif ul=="n":
						exit ("\nSampai Jumpa lagi...")
		try:
			for i in range(1000):
				sleep(0.2)
				while True:
					sleep(0.1)
					os.system('clear')
					print("√Sukses terkirim ke >> " + no)
					client=Client(account_sid, auth_token)
					message = client.messages.create(body=msg,from_='whatsapp:+14155238886',to='whatsapp:' + no)
					break
		except KeyboardInterrupt:
			print("\nGoodBye...")
khazul()
