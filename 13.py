import requests
my_file2 = open("urls.txt")
for url in my_file2.readlines():
    current_url = url.strip()
    response = requests.get(current_url)
    print(current_url)
    if response.status_code == 200:
        print(current_url.split('//'))
        print(f"{current_url.split('//')[1]} is up and running")
