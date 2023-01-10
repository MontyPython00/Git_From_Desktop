import time
import re
li = []
test = '123 nothing'

# while test != 'stop':
#     print('To stop a software insert \'stop\'')
#     test = input('test:')
#
#     time.sleep(1)
#     li.append(test)
#     print(li)

li.append(re.findall("(\d+)?(\D+)?(\d+)", test))
testing = re.findall("(\d+)?(\D+)?(\d+)", test)
print(li, testing[0][1])

