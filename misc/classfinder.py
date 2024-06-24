import csv

csv_file = "ck/class.csv"
prefix = "G:\\Users\\Roelof\\Documents\\School\\TU Delft\\Research Project\\SF110\\.\\SF110-20130704-src\\"

csv_data = []
with open(csv_file, mode ='r')as file:
	csv = csv.reader(file)
	for line in csv:
		csv_data.append(line)
keys = csv_data[0]
data = []
for d in csv_data[1:]:
	di = {}
	if "evosuite" in d[0].lower():
		continue
	for i in range(len(csv_data[0])):
		di[csv_data[0][i]] = d[i]
	data.append(di)

def printc(c):
	# print(type(c))
	if isinstance(c, dict):
		keys = ["class", "fanin", "fanout", "cbo", "wmc", "loc"]
		d = {}
		for k in keys:
			d[k] = c[k]
		d["package"] = c["file"].removeprefix(prefix).split("\\")[0]
		print(d)
	elif hasattr(c, "__iter__"):
		for x in c:
			printc(x)
	else:
		print(c)

csv_data = None
def fun(x):
	filters = [
		["stringutils", "jsecurity"],
		["AbstractNFeAdaptadorBean"],
		["OpMatcher"]
	]
	found = False
	for f in filters:
		m = 0
		for f2 in f:
			if f2.lower() in x["file"].lower() and "test" not in x["file"].lower():
				m += 1
		if m == len(f):
			return True
	return False

def find_filter(c):
	if "test" in c["class"].lower() or int(c["loc"]) > 300 or int(c["wmc"]) < 20 or int(c["cbo"]) > 3 or "liferay" in c["file"]:
		return False
	name = c["class"].lower().split(".")[-1]
	package = c["file"].removeprefix(prefix).split("\\")[0]
	for d in data:
		if name in d["class"].lower() and "test" in d["class"].lower() and package in d["file"].lower():
			return True
	

# def has_tests(c):
	
	
	# for d in data:


# print(keys)
# printc(data[1])
print("\n")
print(len(data))
corpus = list(filter(fun, data))
filtered = list(filter(find_filter, data))
printc(filtered)
# print(data[0])
# print(data[0][7])
# print(data[2][7])
# for d in data[1:]:
# 	if int(d[3]) < 2 and "test" not in d[0].lower():
# 		print(d[1])
	# if d[1].endswith("OpMatcher"):
		# print(d[7])
