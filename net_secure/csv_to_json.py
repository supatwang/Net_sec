import csv
import json
import random

nodes = []
edges = []
temp = {}
size = {}
color = {}
names = {}

csvfile = open('2018-07-Domestic Exchange - Index.csv', 'r')
jsonfile = open('domestic.json', 'w')

csv_dict = csv.DictReader(csvfile)

for row in csv_dict:
	edge = {}

	if row['ASN'] not in temp:
		size[row['ASN']] = 5
		temp[row['ASN']] = row['ASN']
		names[row['ASN']] = row['Name']
	else:
		size[row['ASN']] = int(size[row['ASN']]) + 5
	
	edge['sourceID'] = row['ASN-source']
	edge['targetID'] = row['ASN']
	edge['attributes'] = {}
	edge['bw'] = row['Bandwidth'] + " " + row['Gb/s'] + "(" + row['Connectivity Type'] + ")"
	edge['size'] = float(row['Bandwidth'])/100 + 1
	edges.append(edge)
	print(edge['bw'])


for i in temp:
	color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
	node = {}
	node['id'] = i
	node['x'] = random.uniform(-1000, 1000)
	node['y'] = random.uniform(-1000, 1000)
	node['size'] = size[i]
	node['attributes'] = {}
	node['label'] = names[i]
	node['color'] = color
	nodes.append(node)

data = {}
data['nodes'] = nodes
data['edges'] = edges


json.dump(data, jsonfile)