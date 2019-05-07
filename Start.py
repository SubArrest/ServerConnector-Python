#!/usr/bin/env python3
import ServerConnector as sc
import JsonEditor as je
import Login
import json
import sys
from collections import OrderedDict
from pathlib import Path
import os

Login.StartLogin(False)

path_to_json = Path(__file__[0:-int(len(os.path.basename(__file__)))] + "/Users.json")  # Edit Between The "Path()" To Set Custom Users File Directory

with open(path_to_json, "r") as f:
    data = json.load(f, object_pairs_hook=OrderedDict)

loop1 = "y"
while loop1 != "n":
    print("~Server List Manager~")
    print("---------------------")
    print("1: Server Connector")
    print("2: JSON Editor")
    print("3: Login Configurations")
    print("x: Exit")
    print("---------------------")
    ans1 = input()
    if ans1 == "1":
        loop1 = "n"
        sc.Start()
    elif ans1 == "2":
        loop1 = "n"
        je.Start()
    elif ans1 == "3":
        loop1 = "n"
        Login.config()
    elif ans1 == "x":
        loop1 = "n"
        print("Exiting...")
        sys.exit()
    else:
        print("That was not a valid option!")
