import sys

print(sys.path)

# //////////////////////////////////////////////////////////////////////////////

import re

text = 'Mi numero de telefono es 311 324 5678, el codigo del pais en 57, mi numero de la suerte es 4'
result = re.findall('[0-9]+', text)
print(result)



# //////////////////////////////////////////////////////////////////////////////


import time

# formato que la computadora entiende
timestamp = time.time()
print(timestamp)

# formato mas legible para los humanos
local =  time.localtime()
result = time.asctime(local)
print(result)


# //////////////////////////////////////////////////////////////////////////////


import collections

numbers = [1,2,3,3,4,5,6,2,2,1]
counter = collections.Counter(numbers)
print(counter)