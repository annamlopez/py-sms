from random import choice 

print "Do you want to play a game of Would You Rather? Or talk to the Text Bot Shiloh? (type WYR or Shiloh, you can alternate between the two at any point.)"
media_links_for_happy = ["https://www.buzzfeed.com/kaelintully/jurassic-park-is-a-gr8-film-raptor-shriek-all-the-damn-time?utm_term=.vnG4WN1zwV#.dj5XPlKv3w", "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww4.pictures.zimbio.com%2Fmp%2FHuMZPUQrZeql.jpg&imgrefurl=http%3A%2F%2Fwww.zimbio.com%2FMovie%2BNews%2Farticles%2FvVqgDGD2AFT%2FEveryone%2BObsessed%2BInsanely%2BCute%2BBaby%2BDory&docid=kD-rxCfvcCdtMM&tbnid=g1G5p7E8gVILmM%3A&w=600&h=400&bih=630&biw=1280&ved=0ahUKEwjmrJOYh5XOAhUSBh4KHUNXCMcQMwhvKBkwGQ&iact=mrc&uact=8"]
media_links_for_sad = ["https://www.google.com/imgres?imgurl=http%3A%2F%2Fmedia.brostrick.com%2Fwp-content%2Fuploads%2F2016%2F03%2F10075517%2Ffunny-donald-trump-president-memes-2016-hair.jpg&imgrefurl=http%3A%2F%2Fwww.brostrick.com%2Fviral%2Ffunny-political-memes-donald-trump-hillary-clinton-sanders-cruz%2F&docid=kyYVY3gYM-nMtM&tbnid=yVn63XKixEuEbM%3A&w=446&h=536&bih=630&biw=1280&ved=0ahUKEwjlkML7h5XOAhWLJB4KHeiYASEQMwheKAAwAA&iact=mrc&uact=8", ]


def response_handler(body):
    message = ""
    if body == "WYR":
        print "For next Would You Rather type in WYR."
        message = choice(["Would you rather a. live one life that lasts 1,000 years or b. live 10 lives that last 100 years each?", "Would you rather have to a. sneeze but not be able to or b. have something stuck in your eye for an entire year?", "Would you rather a. wear a snow suit in the desert or b. be naked in Antarctica?", "Would you rather a. have no arms or b. no legs?", "Would you rather be filthy rich but suffer depression or be poor but happy?"])
    elif body == "Shiloh":
        message = "Hi! My name is Shiloh. How are you?? If you aren't feeling the bestest type :( for some amusing pictures! If you feel as if you are on top of the WOOOORLD type :) for some delightful pictures. If you're feeling just alright type :| for some pleasant pictures."
    if body == ":(":
        return media_links_for_sad
    elif body == ":)":
        message = choice(["https://www.buzzfeed.com/kaelintully/jurassic-park-is-a-gr8-film-raptor-shriek-all-the-damn-time?utm_term=.vnG4WN1zwV#.dj5XPlKv3w", "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww4.pictures.zimbio.com%2Fmp%2FHuMZPUQrZeql.jpg&imgrefurl=http%3A%2F%2Fwww.zimbio.com%2FMovie%2BNews%2Farticles%2FvVqgDGD2AFT%2FEveryone%2BObsessed%2BInsanely%2BCute%2BBaby%2BDory&docid=kD-rxCfvcCdtMM&tbnid=g1G5p7E8gVILmM%3A&w=600&h=400&bih=630&biw=1280&ved=0ahUKEwjmrJOYh5XOAhUSBh4KHUNXCMcQMwhvKBkwGQ&iact=mrc&uact=8"])
        
    # else:
    #     message = "Invalid command.  Text 'start' to restart the game.  Or text 'pic please' for a random picture"
    return message 

    