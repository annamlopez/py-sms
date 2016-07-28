# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from handler import *
from random import choice

######################################################
# Warning: you must replace the values below!
# Find these values at https://twilio.com/user/account
account_sid = "AC6f9854ebea5e96e6aeb74334fc887d98"
auth_token = "49dd2ccc11461e2d5fd8d70354019417"  
fromnumber = "+19782917255"
tonumber = "+19783141229"
body_text = "'ey"
######################################################

client = TwilioRestClient(account_sid, auth_token)

# sends a text from fromnumber to to number consisting of body_text 
def send(fromnumber, tonumber, body_text):
	print "Preparing to send sms text from %s to %s: %s" % (fromnumber, tonumber, body_text)

	message = client.messages.create(to=tonumber, 
									 from_=fromnumber, 
									 body=body_text)

	print "SMS text successfully sent!"

# sends a media text from fromnumber to tonumber consisting of media_links (list of links to media)
def send_media(fromnumber, tonumber, media_links):
	print "Preparing to send media text from %s to %s: %s" % (fromnumber, tonumber, media_links)

	message = client.messages.create(to=tonumber, 
									 from_=fromnumber, 
									 media_url=media_links)

	print "Media text successfully sent!"

# send(fromnumber, tonumber, body_text)

# media_links = ["http://i.telegraph.co.uk/multimedia/archive/03597/POTD_chick_3597497k.jpg", 'https://upload.wikimedia.org/wikipedia/commons/5/55/Phillips_Academy_Andover_Coat_of_Arms.png', 'http://vignette1.wikia.nocookie.net/pokemon/images/f/fc/025Pikachu_OS_anime_5.png/revision/20150101093704', "http://all4desktop.com/data_images/original/4238212-pictures.jpg", "http://i.telegraph.co.uk/multimedia/archive/03519/potd-squirrel_3519920k.jpg", "http://i.telegraph.co.uk/multimedia/archive/03571/potd-squirrel_3571152k.jpg"]
# send_media(fromnumber, tonumber, choice(media_links))

media_links_for_happy = ["https://www.buzzfeed.com/kaelintully/jurassic-park-is-a-gr8-film-raptor-shriek-all-the-damn-time?utm_term=.vnG4WN1zwV#.dj5XPlKv3w", "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww4.pictures.zimbio.com%2Fmp%2FHuMZPUQrZeql.jpg&imgrefurl=http%3A%2F%2Fwww.zimbio.com%2FMovie%2BNews%2Farticles%2FvVqgDGD2AFT%2FEveryone%2BObsessed%2BInsanely%2BCute%2BBaby%2BDory&docid=kD-rxCfvcCdtMM&tbnid=g1G5p7E8gVILmM%3A&w=600&h=400&bih=630&biw=1280&ved=0ahUKEwjmrJOYh5XOAhUSBh4KHUNXCMcQMwhvKBkwGQ&iact=mrc&uact=8"]
media_links_for_sad = ["https://www.google.com/imgres?imgurl=http%3A%2F%2Fmedia.brostrick.com%2Fwp-content%2Fuploads%2F2016%2F03%2F10075517%2Ffunny-donald-trump-president-memes-2016-hair.jpg&imgrefurl=http%3A%2F%2Fwww.brostrick.com%2Fviral%2Ffunny-political-memes-donald-trump-hillary-clinton-sanders-cruz%2F&docid=kyYVY3gYM-nMtM&tbnid=yVn63XKixEuEbM%3A&w=446&h=536&bih=630&biw=1280&ved=0ahUKEwjlkML7h5XOAhWLJB4KHeiYASEQMwheKAAwAA&iact=mrc&uact=8", ]


user = raw_input("Enter a text to send your TWILIO number.  Or enter q to quit: \n> ")
while user != "q":
	response = response_handler(user)
	send(fromnumber, tonumber, response)
	user = raw_input("Enter a text to send your TWILIO number.  Or enter q to quit: \n> ")
