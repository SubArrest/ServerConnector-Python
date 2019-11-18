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

        loop = "y"
        while loop != "n":
            back = "n"
            print("~Server Connector~")
            print("------------------")
            num = 0
            for q in self.data['servers']:
                num += 1
                name = self.data['servers'][q][0]['name']
                print(str(num) + ":", name)
            print("b: Back")
            print("x: Exit")
            print("------------------")
            ans = input()
            hasFound = False
            for o in self.data['servers']:
                if ans == o:
                    hasFound = True
                    break
                elif ans == "b":
                    loop = "n"
                    back = "y"
                    hasFound = True
                    print()
                    break
                elif ans == "x":
                    loop = "n"
                    hasFound = True
                    print("Exiting...")
                    sys.exit()
            check = self.data['servers'].get('1')
            if check is not None and not hasFound:
                print("Invalid Option")
            elif hasFound:
                if back != "y":
                    username = self.data['servers'][ans][0]['username']
                    password = self.data['servers'][ans][0]['password']
                    ip = self.data['servers'][ans][0]['ip']
                    print("Connecting...")
                    call(["sshpass", "-p", password, "ssh", "-o", "StrictHostKeyChecking=no", username + "@" + ip])
                    loop = "n"
            else:
                print("Invalid Option")
