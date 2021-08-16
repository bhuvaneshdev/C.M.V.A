import speech_recognition as sr 
import pyttsx3 #pip install pyttsx3
 #!pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import wolframalpha
import random
import webbrowser
from gnewsclient import gnewsclient 

  
thanks=['Thanks',"it's my pleasure",'Iam always your assistant sir']
stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']

#______________________________________


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Boss")   

    else:
        speak("Good Evening!")  

    speak("Iam your assistant ,jarvis .... How can I help you....")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1

        audio=r.listen(source)
  
    try:   
        print("Wait for few Moments")
        query=r.recognize_google(audio,language='en-in')
        
        
    except Exception as e:
        print(e)
        query="nothing"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
            	q= takeCommand().lower()
            	word='jarvis'
            	query= q.replace(word, "")
            	word4='who is'
            	query=query.replace(word4,'')
            	print('____________________________________________________________'+'	user  :'+q)
    
#says hello
            	if  'hi' in query or  'hello' in query:
            	    		speak('HELLO,SIR ')
            	elif q==word and query=='':
            	    		speak('yes sir tell me')
            	elif 'time' in query:
            	    		speak('The current time is '+(str(datetime.datetime.now().strftime('%I:%M %p'))))   
            	elif "i love you" in query:
            	    		speak('I LOVE YOU TOO...')
            	elif 'exit' in query:
            	    			speak('	jarvis:bye sir')
            	elif 'wikipedia' in query:
            	    				print('	jarvis:Searching Wikipedia...')
            	    				speak('Searching Wikipedia...')
            	    				query = query.replace("wikipedia", "")
            	    				results = wikipedia.summary(query, sentences=2)
            	    				print("		According to Wikipedia")
            	    				speak(results)
            	    				print(results)
            	elif 'open google' in query:
            	    				speak('opening google....')
            	    				webbrowser.open('https://www.google.com/search?gs_ssp=eJzj4tVP1zc0', new=2)
            	elif 'open youtube' in query:
            	    					speak('opening youtube....')
            	    					webbrowser.open('https://www.youtube.com/', new=2)
            	elif 'search on google' in query or 'QUESTION' in query :
            	    					x=input('WHAT IS YOUR QUESTIONS: ')
            	    					webbrowser.open('https://www.google.com/search?q='+x)
            	elif 'search on youtube' in query:  
            	    				y=input('Enter your query to search in youtube: ')
            	    				webbrowser.open('https://m.youtube.com/results?search_query='+y)
            	elif 'amazon' in query:
            	    				speak('opening amazon....')
            	    				webbrowser.open('https://www.amazon.in/')
            	elif 'date' in query:
            	    				d = datetime.datetime.today()
            	    				speak(d.strftime("%d %B %Y"))
            	elif "what\'s up" in query or "how are you" in query:
            	    				speak(random.choice(stMsgs))
            	elif "where is" in query:
            	    				query = query.split(" ")
            	    				location = query[2]
            	    				speak("Hold on   I will show you where " + location + " is.")
            	    				webbrowser.open("http://maps.google.com/?q=" + location)
            	elif 'where i am ' in query:
            	    					speak('Sir I will show you that were are you')
            	    					webbrowser.open("https://www.google.com/maps/place/" + 'where iam')
 
            	elif 'who are you' in query or 'what is your name' in query :
            		speak('sir Iam your assistant ,JARVIS.')
            	elif 'say' in query:
            		word1='say'
            		say= query.replace(word1, "")
            		speak(say)
            		    		
            	elif 'are you ok' in query :
            		speak('	jarvis:yes Iam ok')
            		
            	elif 'super' in query or 'great' in query or 'welldone' in query or 'good job' in query :
            		speak('	jarvis:'+random.choice(thanks))    	
            	elif 'news' in query:
            		try:
            			speak('Yes sir loading')
            			client = gnewsclient.NewsClient(language='tamil',  

                                location='india',  

                                topic='Tamil nadu',  

                                max_results=3)
            			news_list = client.get_news() 
            			for item in news_list:
            				print('____________________________________________________________')
            				speak(item['title']+" And click the link for more info")
            				print("Headlines: ", item['title']+'\n')
            				print("Link : ", item['link'])
            				print('____________________________________________________________')
            		except:
            			speak('			An error occured,so Iam opening in  youtube')
            			webbrowser.open('https://youtu.be/yKMT5aJl7yI')
            	elif 'battery' in query :
            		battery = psutil.sensors_battery()
            		speak("Battery percentage is ", battery.percent,'%')     
            	elif 'bye' in query or 'exit' in query or 'close' in query  :
            		speak('have a nice day and ,bye sir')
            		exit() 	             
    	
    	         
    
            	else:
            		try:
            			print('searching....')
            			app_id = 'Enter your wofram-alpha id'
            			client = wolframalpha.Client(app_id) 
            			res = client.query(query)
            			answer = next(res.results).text
            			print('	Got it sir')
            			print(answer)
            			speak(answer)
        
            		except:
            			speak("I don't know about this,So Iam  searching this in  google ")
            			webbrowser.open('https://www.google.com/search?q='+query)
      		 
