import os
import subprocess

file_list = [
    "deployCDN", "runCDN", "stopCDN", "dnsserver", "httpserver", "Makefile", 
    "scpBuildServer.py", "README.md"
]

khoury_address = "linppa@login.khoury.northeastern.edu:~/"

keyfile = "keys/ssh-ed25519-quach.l.priv"

def scpKhoury():
    for file in file_list:
        command = ['scp', '-i', keyfile, file, f'{khoury_address}']
        print(f"Copying file {file} to Khoury server")
        subprocess.run(command)
        print(f"File {file} has been copied to Khoury server")

if __name__ == "__main__":
    scpKhoury()
