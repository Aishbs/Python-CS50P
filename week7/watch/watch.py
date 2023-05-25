import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    if re.search(r'src=.+', s):
        # extract youtube ID
        if link := re.search(r"(https?://)?(www\.)?youtube\.com\/embed\/([a-zA-Z0-9_]+)", s):
            yt = link.groups()
            return f"https://youtu.be/{yt[2]}"
        else:
            return None

if __name__ == "__main__":
    main()