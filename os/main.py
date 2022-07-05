import os
from datetime import datetime
os.chdir('/Users/ngoduc/Algo')

# mod_time = os.stat('demo.txt').st_ctime

# print(datetime.fromtimestamp(mod_time))

file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')

print(file_path)
