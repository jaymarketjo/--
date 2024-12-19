import string
import random
import time
s='good word'
random_list=string.ascii_letters+''
temp=''
for i,word in enumerate(s):
   while temp!=word:
      temp=random.choice(random_list)
      print(s[:i]+temp)
      time.sleep(0.02)
