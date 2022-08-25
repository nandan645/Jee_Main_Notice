import time
import requests

update= open('/root/Programs/Jee_Mains_Notifier/firstScrape', 'r').read()

time_now=time.ctime()

Bot_API_Token = "Your Bot API token"
Chat_Group_Id = "Your Group Id"

base_url= 'https://api.telegram.org/bot'+Bot_API_Token+'/sendMessage?chat_id='+Chat_Group_Id+'&text={}'.format(time_now+update)

requests.get(base_url)
