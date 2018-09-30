#!/usr/bin/env python3
from pathlib import Path
import json
from subprocess import call
import sys

path_to_json = Path(str(Path(__file__).parent) + "/Servers.json")

with open(path_to_json, "r") as f:
	data = json.load(f)

loop1 = "y"
while loop1 != "n":
	print("~Server List Manager~")
	print("---------------------")
	print("1: Server Connector")
	print("2: JSON Editor")
	print("x: Exit")
	print("---------------------")
	ans1 = input()
	if ans1 == "1":
		loop1 = "n"
		loop2 = "y"
		while loop2 != "n":
			print("~Server Connector~")
			print("------------------")
			for q in data['servers']:
				for w in data['servers'][q]:
					name = w['name']
				print(str(q) + ":", name)
			print("x: Exit")
			print("------------------")
			ans2 = input()
			hasFound = False
			for o in data['servers']:
				if ans2 == o:
					hasFound = True
					for p in data['servers'][ans2]:
						username = p['username']
						password = p['password']
						ip = p['ip']
					print("Connecting...")
					call(["sshpass", "-p", password, "ssh", "-o", "StrictHostKeyChecking=no", username + "@" + ip])
					loop2 = "n"
					break
				elif ans2 == "x":
					loop2 = "n"
					hasFound = True
					print("Exiting...")
					sys.exit()
			if hasFound == False:
				print("That server does not exist!")
	elif ans1 == "2":
		loop1 = "n"
		loop3 = "y"
		while loop3 != "n":
			print("~JSON Editor~")
			print("-------------")
			print("1: Add Server")
			print("2: Delete Server")
			print("3: Edit Existing Server")
			print("x: Exit")
			print("-------------")
			ans3 = input()
			if ans3 == "1":
				loop3 = "n"
				num = data['servers'].get('1')
				if num == None:
					servnum = 1
				else:
					for num in data['servers']:
						servnum = int(num) + 1
				name = input("Name: ")
				username = input("Username: ")
				password = input("Password: ")
				ip = input("IP: ")
				entry = {str(servnum): [{"name": name, "username": username, "password": password, "ip": ip}]}
				data['servers'].update(entry)
				with open(path_to_json, 'w') as f:
					json.dump(data, f, indent=4)
			elif ans3 == "2":
				loop3 = "n"
				loop4 = "y"
				while loop4 != "n":
					print("~Delete Server~")
					print("---------------")
					for m in data['servers']:
						for n in data['servers'][m]:
							name = n['name']
						print(str(m) + ":", name)
					print("x: Exit")
					print("---------------")
					ans4 = input()
					hasFound = False
					for b in data['servers']:
						if ans4 == b:
							hasFound = True
							del data['servers'][ans4]
							loop4 = "n"
							break
						elif ans4 == "x":
							loop4 = "n"
							print("Exiting...")
							sys.exit()
					if hasFound == False:
						print("That server does not exist!")
					with open(path_to_json, "w") as f:
						json.dump(data, f, indent=4)
			elif ans3 == "3":
				loop3 = "n"
				loop5 = "y"
				while loop5 != "n":
					print("~Edit Existing Server~")
					print("----------------------")
					for m in data['servers']:
						for n in data['servers'][m]:
							name = n['name']
						print(str(m) + ":", name)
					print("x: Exit")
					print("----------------------")
					ans5 = input()
					hasFound = False
					for b in data['servers']:
						if ans5 == b:
							hasFound = True
							num = data['servers'].get('1')
							if num == None:
								servnum = 1
							else:
								for num in data['servers']:
									servnum = int(num) + 1
							name = input("Name: ")
							username = input("Username: ")
							password = input("Password: ")
							ip = input("IP: ")
							for g in data['servers'][str(servnum)]:
								g['name'] = name
								g['username'] = username
								g['password'] = password
								g['ip'] = ip
							with open('../Servers.json', 'w') as f:
								json.dump(data, f, indent=4)
							loop5 = "n"
							break
						elif ans5 == "x":
							loop5 = "n"
							print("Exiting...")
							sys.exit()
					if hasFound == False:
						print("That server does not exist!")
					with open(path_to_json, "w") as f:
						json.dump(data, f, indent=4)
			elif ans3 == "x":
				loop3 = "n"
				print("Exiting...")
				sys.exit()
			else:
				print("That was not a valid option!")
	elif ans1 == "x":
		loop1 = "n"
		print("Exiting...")
		sys.exit()
	else:
		print("That was not a valid option!")