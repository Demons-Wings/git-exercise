
terms = ("failed", "invalid user", "authentication")

matches = 10 

with open("/var/log/auth.log", "r", encoding="utf-8") as logfile:
	for event in logfile:
		if any(item in event.lower() for item in terms):
			matches-=1
			print(event.rstrip())

print(f"Matching lines: {matches}!")
