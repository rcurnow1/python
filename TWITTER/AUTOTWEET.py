import twitter, sqlite3, urllib2, time
while True:
	pass

	#call the history 
	console = sqlite3.connect("C:\\Users\\rcurnow1\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
	cursor = console.cursor()

	cursor.execute("SELECT urls.title FROM urls")
	GrabData = cursor.fetchall()

	HistoryList = []

	for row in GrabData:
		HistoryList.append(row)
		#grabbing the last entry frm the list turning into a string storing to get parsed 
	RecentHistory = str(HistoryList[-1])
	#this trims the text down to so it just the clean text
	Trim = RecentHistory[3:-3]
	console.close

	file = open("accesstokens.txt")
	creds = file.read().split('\n')
	api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
	response = api.PostUpdate("Looking at " + str(Trim))
	print("Status updated to: " + response.text)
	time.sleep(30)

