from urllib.request import urlretrieve
import requests
import wget
from requests.auth import HTTPBasicAuth
def boardselect():
    print("Select a Board.")
    print("[O]ctopus")
    print("[B]rya")
    print("[G]runt")
    print("[D]edede")
    print("[C]oral")
    print("[H]ana")
    board = input("")
    if board == "O":
        print("Beginning the download...")
        print(".")
        print("..")
        print("...")
        print("..")
        print(".")
        v120 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15662.76.0_octopus_recovery_stable-channel_mp-v33.bin.zip"
        v119 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15633.72.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v118 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15604.57.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v117 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15572.63.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v116 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15509.81.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v115 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15474.84.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v114 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15437.63.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v113 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15393.58.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v112 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15359.58.0_octopus_recovery_stable-channel_mp-v32.bin.zip"
        v111 = "https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_15329.44.2_octopus_recovery_stable-channel_mp-v32.bin.zip"
        print("All versions registered!")
        req = requests.get(v120)
        req1 = requests.get(v119)
        req2 = requests.get(v118)
        req3 = requests.get(v117)
        req4 = requests.get(v116)
        req5 = requests.get(v115)
        req6 = requests.get(v114)
        req7 = requests.get(v113)
        req8 = requests.get(v112)
        req9 = requests.get(v111)
        file = req.split('/')[-1]
        file1 = req1.split('/')[-1]
        file2 = req2.split('/')[-1]
        file3 = req3.split('/')[-1]
        file4 = req4.split('/')[-1]
        file5 = req5.split('/')[-1]
        file6 = req6.split('/')[-1]
        file7 = req7.split('/')[-1]
        file8 = req8.split('/')[-1]
        file9 = req9.split('/')[-1]
        with open(file,'wb') as output_file:
            output_file.write(req.content)
        print("v120 done")
        with open(file1,'wb') as output_file1:
            output_file1.write(req1.content)
        print("v119 done")
        with open(file2,'wb') as output_file2:
            output_file2.write(req2.content)
        print("v118 done")
        with open(file3,'wb') as output_file3:
            output_file3.write(req3.content)
        print("v117 done")
        with open(file4,'wb') as output_file4:
            output_file4.write(req4.content)
        print("v116 done")
        with open(file5,'wb') as output_file5:
            output_file5.write(req5.content)
        print("v115 done")
        with open(file6,'wb') as output_file6:
            output_file6.write(req6.content)
        print("v114 done")
        with open(file7,'wb') as output_file7:
            output_file7.write(req7.content)
        print("v113 done")
        with open(file7,'wb') as output_file7:
            output_file7.write(req7.content)
        print("v112 done")
        with open(file8,'wb') as output_file8:
            output_file8.write(req8.content)
        print("v111 done")
        with open(file9,'wb') as output_file9:
            output_file9.write(req9.content)
        print("what the hell 120-10 = 111? What is happening did I count wrong? Idk what file you downloaded. its from the links it might be v111 but who knows")
        print("This is a strange bug I guess, correct my math at https://github.com/Hexine-Network/ and find this repo.")
        
        print("It should have downloaded if it didn't you can read the variables and do it yourself")
        print(v111, v112, v113, v114, v115, v116, v117, v118, v119, v120)
boardselect()
    
