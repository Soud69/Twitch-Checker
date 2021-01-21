try:
    import requests
    from os import system

    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")

print("""

░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝

                        Credit @_agf - Soud#0737
                        
                        """)
print("This is simple tool by Soud to check Twitch User\n")

input("Press any Key to start Checking\n")

a = requests.Session()

ggg = open("User.txt", "r")

co = 0
do = 0
fa = 0

while 1:
    user = ggg.readline().split("\n")[0]
    if user == "":
        break
    url = f"https://m.twitch.tv/{user}"

    head = {
        'Host': 'm.twitch.tv',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://m.twitch.tv/service-worker.js",
        'Connection': 'keep-alive'
    }

    re = a.get(url, headers=head)
    if re.status_code == 404:
        if len(user) >= 4:
            co += 1
            do += 1
            print(f"[+] Found >> {user} | Checked: {co}")
            with open("Found.txt", "a") as result:
                result.write(f"{user}\n")
        else:
            co += 1
            fa += 1
            print(f"[-] Less Than 4 >> {user} | Checked: {co}")
    elif re.status_code == 200:
        co += 1
        fa += 1
        print(f"[-] Taken >> {user} | Checked: {co}")

print(f"Found: {do} | Taken: {fa} | Checked: {co}\nChecker By Soud @_agf Soud#0737\nSaved All in Found.txt <3\n")
input("Press any Key to Exit...\n")
