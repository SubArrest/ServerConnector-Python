import json
from collections import OrderedDict
import sys
from pathlib import Path
import os

path_to_json = Path(__file__[0:-int(len(os.path.basename(__file__)))] + "/Users.json")  # Edit Between The "Path()" To Set Custom Users File Directory


class StartLogin:
    def __init__(self, skip_usr):
        global path_to_json
        with open(path_to_json, "r") as f:
            self.data = json.load(f, object_pairs_hook=OrderedDict)
        for l in self.data:
            self.output = l['enabled']
        if self.output == "option":
            self.option(skip_usr)
        elif self.output == False:
            return
        elif self.output == True:
            self.att = 0
            self.login(self.att)
        else:
            print("Error, Json File Contains Incorrect 'enabled' Value!")

    def option(self, skip_usro):
        print("~Enable Login System?~")
        print("----------------------")
        print("1: Enable Login System")
        print("2: Disable Login System")
        print("----------------------")
        ans = input()
        if ans == "1":
            if skip_usro:
                self.jenablen()
            else:
                self.jenable()
        elif ans == "2":
            self.jdisable()
        else:
            print("Not Valid Option")
            if skip_usro:
                self.option(True)
            else:
                self.option(False)

    def jenablen(self):
        global path_to_json
        for l in self.data:
            l['enabled'] = True
        with open(path_to_json, "w") as f:
            json.dump(self.data, f, indent=4)
        print("Login System Enabled Successfully!")

    def jenable(self):
        while True:
            print()
            print("User Setup:")
            print("-----------")
            username = input("Username: ")
            password = input("Password: ")
            print("-----------")
            confirm = input("Submit? (Y/n): ")
            if confirm == "y" or confirm == "" or confirm == "Y":
                break
            elif confirm == "n" or confirm == "N":
                print("Restarting User Setup...")
            else:
                print("Not Valid Option (y/n)")
        self.submituser(username, password)

    def submituser(self, usr, passwd):
        global path_to_json
        for l in self.data:
            l['enabled'] = True
        entry = {usr: [{"password": passwd}]}
        self.data[0]['users'].update(entry)
        with open(path_to_json, "w") as f:
            json.dump(self.data, f, indent=4)
        print("User Setup Complete!")
        print("Login System Enabled Successfully!")

    def jdisable(self):
        global path_to_json
        for l in self.data:
            l['enabled'] = False
        with open(path_to_json, "w") as f:
            json.dump(self.data, f, indent=4)
        print("Login System Disabled Successfully!")

    def login(self, latt):
        if 0 <= latt < 5:
            if latt >= 1:
                print((5-latt), "Attempts Remaining")
            print("~Login~")
            print("-------")
            lusr = input("Username: ")
            lpasswd = input("Password: ")
            print("-------")
            self.submit(lusr, lpasswd)
        else:
            print("0 Attempts Remaining")
            sys.exit()

    def submit(self, susr, spasswd):
        num = 0
        num2 = 0
        for l in self.data[0]['users']:
            num2 = num2 + 1

        for o in self.data[0]['users']:
            num = num + 1
            if susr == o:
                try:
                    for k in self.data[0]['users'][susr]:
                        if spasswd == k['password']:
                            print("~Logged In~")
                            break
                        else:
                            print("Username or Password not recognised!")
                            self.att = self.att + 1
                            self.login(self.att)
                    break
                except:
                    break
            else:
                if num != num2:
                    pass
                else:
                    print("Username or Password not recognised!")
                    self.att = self.att + 1
                    self.login(self.att)


def config():
    global path_to_json
    with open(path_to_json, "r") as f:
        c_data = json.load(f, object_pairs_hook=OrderedDict)
    while True:
        option = input("Keep Current Users (Y/n)? ")
        if option == "Y" or option == "" or option == "y":
            for k in c_data:
                k['enabled'] = "option"
            with open(path_to_json, "w") as f:
                json.dump(c_data, f, indent=4)
            StartLogin(True)
            break
        elif option == "n" or option == "N":
            for k in c_data:
                k['enabled'] = "option"
                k['users'] = {}
            with open(path_to_json, "w") as f:
                json.dump(c_data, f, indent=4)
            StartLogin(False)
            break
        else:
            print("Not Valid Option")