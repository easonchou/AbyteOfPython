import os
import time

source = ['"F:\\0 doning ths"','"F:\\BaiduYunDownload"']
# Notice we had to use double quotes inside the string for names with 10 spaces in it. 

target_dir = "F:\\bak"

today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive 
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

target = today + os.sep + now + '.zip' 

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) 

if os.system(zip_command) == 0: 
    print('Successful backup to', target) 
else:
    print('Backup FAILED')
