from pathlib import Path
import json
from collections import OrderedDict
import sys
import os

path_to_json = Path(__file__[0:-int(len(os.path.basename(__file__)))] + "/Servers.json")  # Edit Between The "Path()" To Set Custom Servers File Directory


class Start:
    def addserver(self):
        global path_to_json
        self.num = self.data['servers'].get('1')
        if self.num == None:
            self.servnum = 1
        else:
            for self.num in self.data['servers']:
                self.servnum = int(self.num) + 1
        self.name = input("Name: ")
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.ip = input("IP: ")
        self.entry = {str(self.servnum): [{"name": self.name, "username": self.username, "password": self.password, "ip": self.ip}]}
        self.data['servers'].update(self.entry)
        with open(path_to_json, 'w') as f:
            json.dump(self.data, f, indent=4)

    def deleteserver(self):
        global path_to_json
        self.loop4 = "y"
        while self.loop4 != "n":
            print("~Delete Server~")
            print("---------------")
            for m in self.data['servers']:
                for n in self.data['servers'][m]:
                    self.name = n['name']
                print(str(m) + ":", self.name)
            print("x: Exit")
            print("---------------")
            self.ans4 = input()
            self.hasFound = False
            for b in self.data['servers']:
                if self.ans4 == b:
                    self.hasFound = True
                    self.loop4 = "n"
                    break
                elif self.ans4 == "x":
                    self.loop4 = "n"
                    print("Exiting...")
                    sys.exit()
            if self.hasFound == False:
                print("That server does not exist!")
            else:
                del self.data['servers'][self.ans4]
                count = 1
                for j in list(self.data['servers'].keys()):
                    count += 1
                    if int(j) > int(self.ans4):
                        self.data['servers'][str(count-1)] = self.data['servers'][str(count)]
                        self.data['servers'].pop(str(count))
                    else:
                        pass
            with open(path_to_json, "w") as f:
                json.dump(self.data, f, indent=4)

    def detailchoice(self, choice):
        self.loop6 = "y"
        while self.loop6 != "n":
            print("~Editing:", choice + "~")
            print("-" * int(len(choice) + 11))
            print("1: Server Name")
            print("2: Username")
            print("3: Password")
            print("4: IP")
            print("x: Exit")
            print("-" * int(len(choice) + 11))
            self.ans6 = input()
            if self.ans6 == "1":
                self.loop6 = "n"
                self.name = input("Server Name: ")
                for g in self.data['servers'][self.ans5]:
                    g['name'] = self.name
            elif self.ans6 == "2":
                self.loop6 = "n"
                self.username = input("Username: ")
                for g in self.data['servers'][self.ans5]:
                    g['username'] = self.username
            elif self.ans6 == "3":
                self.loop6 = "n"
                self.password = input("Password: ")
                for g in self.data['servers'][self.ans5]:
                    g['password'] = self.password
            elif self.ans6 == "4":
                self.loop6 = "n"
                self.ip = input("Ip: ")
                for g in self.data['servers'][self.ans5]:
                    g['ip'] = self.ip
            elif self.ans6 == "x":
                self.loop6 = "n"
                print("Exiting...")
                sys.exit()
            else:
                print("That was not a valid option!")

    def editserver(self):
        global path_to_json
        self.loop5 = "y"
        while self.loop5 != "n":
            print("~Edit Existing Server~")
            print("----------------------")
            for m in self.data['servers']:
                for n in self.data['servers'][m]:
                    self.name = n['name']
                print(str(m) + ":", self.name)
            print("x: Exit")
            print("----------------------")
            self.ans5 = input()
            self.hasFound = False
            for b in self.data['servers']:
                if self.ans5 == b:
                    self.hasFound = True
                    for b in self.data['servers'][self.ans5]:
                        self.cuser = b['name']
                    self.detailchoice(self.cuser)
                    with open('../Servers.json', 'w') as f:
                        json.dump(self.data, f, indent=4)
                    self.loop5 = "n"
                    break
                elif self.ans5 == "x":
                    self.loop5 = "n"
                    print("Exiting...")
                    sys.exit()
            if self.hasFound == False:
                print("That server does not exist!")
            with open(path_to_json, "w") as f:
                json.dump(self.data, f, indent=4)

    def __init__(self):
        global path_to_json
        with open(path_to_json, "r") as f:
            self.data = json.load(f, object_pairs_hook=OrderedDict)

        self.loop3 = "y"
        while self.loop3 != "n":
            print("~JSON Editor~")
            print("-------------")
            print("1: Add Server")
            print("2: Delete Server")
            print("3: Edit Existing Server")
            print("x: Exit")
            print("-------------")
            self.ans3 = input()
            if self.ans3 == "1":
                self.loop3 = "n"
                self.addserver()
            elif self.ans3 == "2":
                self.loop3 = "n"
                self.deleteserver()
            elif self.ans3 == "3":
                self.loop3 = "n"
                self.editserver()
            elif self.ans3 == "x":
                self.loop3 = "n"
                print("Exiting...")
                sys.exit()
            else:
                print("That was not a valid option!")
