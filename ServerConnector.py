from pathlib import Path
import json
from subprocess import call
from collections import OrderedDict
import sys
import os

path_to_json = Path(__file__[0:-int(len(os.path.basename(__file__)))] + "/Servers.json")  # Edit Between The "Path()" To Set Custom Servers File Directory

class Start:
    def __init__(self):
        global path_to_json
        with open(path_to_json, "r") as f:
            self.data = json.load(f, object_pairs_hook=OrderedDict)

            self.loop2 = "y"
        while self.loop2 != "n":
            print("~Server Connector~")
            print("------------------")
            self.num = 0
            for q in self.data['servers']:
                self.num = self.num + 1
                for w in self.data['servers'][q]:
                    self.name = w['name']
                print(str(self.num) + ":", self.name)
            print("x: Exit")
            print("------------------")
            self.ans2 = input()
            self.hasFound = False
            for o in self.data['servers']:
                if self.ans2 == o:
                    self.hasFound = True
                    for p in self.data['servers'][self.ans2]:
                        self.username = p['username']
                        self.password = p['password']
                        self.ip = p['ip']
                    print("Connecting...")
                    call(["sshpass", "-p", self.password, "ssh", "-o", "StrictHostKeyChecking=no", self.username + "@" + self.ip])
                    self.loop2 = "n"
                    break
                elif self.ans2 == "x":
                    self.loop2 = "n"
                    self.hasFound = True
                    print("Exiting...")
                    sys.exit()
            self.check = self.data['servers'].get('1')
            if self.check != None and self.hasFound == False:
                print("That server does not exist!")
            elif self.check == None and self.ans2 == "x":
                self.loop2 = "n"
                print("Exiting...")
                sys.exit()
            else:
                print("That server does not exist!")
