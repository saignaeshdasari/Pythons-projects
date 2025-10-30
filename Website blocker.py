import datetime
import time
end_time = datetime.datetime(2025,10,24)
site_block = [input("Enter site link to block: ")]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        with open(host_path, 'r+') as file:
            content = file.read()
            for site in site_block:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines() 
            file.seek(0)
            for line in content:
                if not any(site in line for site in site_block):
                    file.write(line)
            file.truncate()
            time.sleep(5)
   