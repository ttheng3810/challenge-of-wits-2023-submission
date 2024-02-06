import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt
import traceback

cwd = os.getcwd()
K = 2254
coordinates = []
invalid = [317, 1768]

for i in range(K):
    if i in invalid: 
        continue
    try:
        filename = cwd + '/log_' + str(i) + '.xml'
        # with open(filename, 'r') as f:
        # read_data = f.read()
        tree = ET.parse(filename)
        root = tree.getroot()
        location_raw = root[0].text
        coordinate = tuple(map(lambda text: int(text), location_raw.split(',')))
        coordinates.append(coordinate)
    except Exception:
        print(traceback.format_exc())
        print(i)

plt.scatter(*zip(*coordinates))
plt.savefig('key.jpeg')
