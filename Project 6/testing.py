#!/usr/bin/env python3
edge_servers = {
    'cdn-http3.khoury.northeastern.edu': '45.33.55.171',
    'cdn-http4.khoury.northeastern.edu': '170.187.142.220', 
    'cdn-http7.khoury.northeastern.edu': '213.168.249.157', 
    'cdn-http11.khoury.northeastern.edu': '139.162.82.207', 
    'cdn-http14.khoury.northeastern.edu': '45.79.124.209', 
    'cdn-http15.khoury.northeastern.edu': '192.53.123.145', 
    'cdn-http16.khoury.northeastern.edu': '192.46.221.203',
}
def main():
    for key,value in edge_servers.items():
        print(value)
    

if __name__ == "__main__":
    main()