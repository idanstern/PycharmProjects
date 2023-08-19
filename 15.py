import requests

try:
    my_file = requests.get("kadfgklansdf:asdnjfk;ansd:asdnfa;sdjf")
except requests.exceptions.InvalidSchema as e:
    print("invalid schema")