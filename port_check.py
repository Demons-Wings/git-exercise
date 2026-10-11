

ports = [80, 53, 22, 443, 9999, 34]
services = {80: "http", 53: "DNS", 443: "https", 22: "ssh", 21: "ftp"}


for i in ports:
	print(f"{i} : {services.get(i, "unknown/review")}")