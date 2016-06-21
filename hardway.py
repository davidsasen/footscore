import requests


r = requests.get("https://api-neon.tfl.gov.uk/Place/BikePoints_1")

BikePoints_1 = r.json()

print r.headers
print "\nIn %s" % BikePoints_1["commonName"]

for each in BikePoints_1["additionalProperties"]:
	if each["key"] == "NbBikes":
		print "Number of bikes available %s" % each['value']
	elif each["key"] == "NbEmptyDocks":
		print "Number of empty docks %s" % each['value']