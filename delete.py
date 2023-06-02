import ezgmail

ezgmail.init(userId='me', tokenFile='token.json', credentialsFile='credentials.json')
keywords = ['LinkedIn']
for keyword in keywords: 
   threads = ezgmail.search(keyword, maxResults=500)
   with open('/home/francescogrienti/script.txt', 'w') as text:
      text.write(f"There are {len(threads)} emails with the keyword, {keyword}")
   text.close()
   ezgmail.summary(threads) #You can check a summary just to make sure you’re not deleting anything important
   for i in range(len(threads)):
      if len(threads)==0:
         print("No \’{keyword}\’ messages to delete, moving on to the next")
      else:
         threads[i].trash()