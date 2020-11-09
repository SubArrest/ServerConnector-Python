from pathlib import Path
import json
from collections import OrderedDict
import sys
import os

path_to_json = Path(__file__[0:-int(len(os.path.basename(__file__)))] + "/Servers.json")  # Edit Between The "Path()" To Set Custom Servers File Directory


class Start:
    def addserver(self):
        global path_to_json
        num = self.data['servers'].get('1')
        if num is None:
            servnum = 1
        else:
            servnum = len(self.data['servers'])+1
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        ip = input("IP: ")
        while True:
            submit = input("Submit Details? (Y/n): ")
            if submit == "" or submit == "Y" or submit == "y":
                entry = {str(servnum): {"name": name, "username": username, "password": password, "ip": ip}}
                self.data['servers'].update(entry)
                with open(path_to_json, 'w') as f:
                    json.dump(self.data, f, indent=4)
                break
            elif submit == "n" or submit == "N":
                break
            else:
                print("Invalid Option")

    def deleteserver(self):
        global path_to_json
        back = "n"
        while True:
            print("~Delete Server~")
            print("---------------")
            for m in self.data['servers']:
                name = self.data['servers'][m]['name']
                print(str(m) + ":", name)
            print("b: Back")
            print("---------------")
            ans = input()
            hasFound = False
            for b in self.data['servers']:
                if ans == b:
                    hasFound = True
                    break
                elif ans == "b":
                    back = "y"
                    hasFound = True
                    print()
                    break
            if not hasFound:
                print("That server does not exist!")
            else:
                if back != "y":
                    del self.data['servers'][ans]
                    count = 1
                    for j in list(self.data['servers'].keys()):
                        count += 1
                        if int(j) > int(ans):
                            self.data['servers'][str(count-1)] = self.data['servers'][str(count)]
                            self.data['servers'].pop(str(count))
                        else:
                            pass
                    with open(path_to_json, "w") as f:
                        json.dump(self.data, f, indent=4)
                else:
                    break

    def detailchoice(self, choice):
        loop = "y"
        while loop != "n":
            print("~Editing:", self.data['servers'][choice]['name'] + "~")
            print("-" * int(len(self.data['servers'][choice]['name']) + 11))
            print("1: Server Name")
            print("2: Username")
            print("3: Password")
            print("4: IP")
            print("b: Back")
            print("-" * int(len(self.data['servers'][choice]['name']) + 11))
            ans = input()
            if ans == "1":
                name = input("Server Name: ")
                self.data['servers'][choice]['name'] = name
                print("Server Name Changed")
            elif ans == "2":
                username = input("Username: ")
                self.data['servers'][choice]['username'] = username
                print("Server Username Changed")
            elif ans == "3":
                password = input("Password: ")
                self.data['servers'][choice]['password'] = password
                print("Server Password Changed")
            elif ans == "4":
                ip = input("Ip: ")
                self.data['servers'][choice]['ip'] = ip
                print("Server IP Changed")
            elif ans == "b":
                loop = "n"
                print()
            else:
                print("That was not a valid option!")

    def editserver(self):
        global path_to_json
        back = "n"
        while True:
            print("~Edit Existing Server~")
            print("----------------------")
            for m in self.data['servers']:
                name = self.data['servers'][m]['name']
                print(str(m) + ":", name)
            print("b: Back")
            print("----------------------")
            ans = input()
            hasFound = False
            for b in self.data['servers']:
                if ans == b:
                    hasFound = True
                    break
                elif ans == "b":
                    back = "y"
                    hasFound = "y"
                    print()
                    break
            if not hasFound:
                print("That server does not exist!")
            else:
                if back != "y":
                    self.detailchoice(ans)
                    with open(path_to_json, 'w') as f:
                        json.dump(self.data, f, indent=4)
                else:
                    break

    def __init__(self):
        global path_to_json
        with open(path_to_json, "r") as f:
            self.data = json.load(f, object_pairs_hook=OrderedDict)

        loop = "y"
        while loop != "n":
            print("~JSON Editor~")
            print("-------------")
            print("1: Add Server")
            print("2: Delete Server")
            print("3: Edit Existing Server")
            print("b: Back")
            print("x: Exit")
            print("-------------")
            ans = input()
            if ans == "1":
                self.addserver()
            elif ans == "2":
                self.deleteserver()
            elif ans == "3":
                self.editserver()
            elif ans == "b":
                loop = "n"
                print()
            elif ans == "x":
                print("Exiting...")
                sys.exit()
            else:
                print("That was not a valid option!")
