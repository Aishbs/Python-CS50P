import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #CHeck the range of ip address
    if len(ip.split('.')) > 4 or len(ip.split('.')) < 4:
        return False

    if re.search("^(([0-1]?[0-9]?[0-9]?|[0-2][0-4][0-9]|25[0-5])\\.){3}([0-1]?[0-9]?[0-9]?|[0-2][0-4][0-9]|25[0-5]){1}$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()