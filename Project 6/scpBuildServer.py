import os
import subprocess

file_list = [
    "deployCDN", "runCDN", "stopCDN", "dnsserver", "httpserver", "Makefile", 
    "README.md", "ssh-ed25519-quach.l.priv", "ssh-ed25519-quach.l.pub"
]

build_server_address = "linppa@cs5700cdnproject.ccs.neu.edu:~/"

keyfile = "ssh-ed25519-quach.l.priv"

def scpBuildServer():
    for file in file_list:
        command = ['scp', '-i', keyfile, file, f'{build_server_address}']
        print(f"Copying file {file} to Khoury server")
        subprocess.run(command)
        print(f"File {file} has been copied to Khoury server")

if __name__ == "__main__":
    scpBuildServer()
