import instaloader

# Get instance
L = instaloader.Instaloader()

USER = "xianggggggggggggggggg"
PASSWORD = "omfgleh"
L.login(USER, PASSWORD)

with open("followers.txt", "r") as ins:
    lineStop = 500
    count = 0
    for line in ins:
        account = str(line.strip())
        followers = []

        try:
            for f in L.get_followers(account):
                followers.append(f['username'])
                lineStop += 1
                count += 1
                print(count)
                #print(lineStop)
                #if lineStop == 40:
                #    break

            if len(followers)>0:
                f1 = open('edgelist.txt', 'a')
                f2 = open('nodelist.txt','a')
                for item in followers:
                    f1.write(item+','+account+'\n')
                    f2.write(item+'\n')
            print("Scraped followers for: " + account)
        except Exception:
            print(Exception)
            print("Skipping this account: " + account)
            continue