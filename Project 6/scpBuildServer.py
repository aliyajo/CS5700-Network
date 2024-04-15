import os
import subprocess

file_list = ["deployCDN", "runCDN", "stopCDN", 
             "dnsserver", "httpserver", "Makefile", 
             "README.md", "ssh-ed25519-quach.l.priv", 
             "ssh-ed25519-quach.l.pub"
]

build_server_address = "linppa@cs5700cdnproject.ccs.neu.edu:~/"

keyfile = "keys/ssh-ed25519-quach.l.priv"

def scpBuildServer():
    for file in file_list:
        command = f'scp {file} {build_server_address}'
        print(f"Copying file {file} to Build server")
        subprocess.run(command, shell=True)
        print(f"File {file} has been copied to Build server")

if __name__ == "__main__":
    scpBuildServer()
             