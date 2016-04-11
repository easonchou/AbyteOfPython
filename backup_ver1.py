import os
import time

source = ['"F:\\0 doning ths"','"F:\\BaiduYunDownload"']
# Notice we had to use double quotes inside the string for names with 10 spaces in it. 

target_dir = "F:\\bak"

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) 

if os.system(zip_command) == 0: 
    print('Successful backup to', target) 
else:
    print('Backup FAILED')
