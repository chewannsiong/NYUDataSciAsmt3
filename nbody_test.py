

import os
import time
option = input('Select with version to exection (valid = 1,2,3,4,opt): ')
option_map = {'1':'nbody_1.py', '2':'nbody_2.py', '3':'nbody_3.py', '4':'nbody_4.py', 'opt':'nbody_opt.py'}
file = option_map[option]
print('Executing {}'.format(file))
start_time = time.time()
os.system('python ' + file)
print('Time taken to execute {} = {} seconds'.format(file, time.time()-start_time))