from random import choice 

message = "Do you want to play a game of Would You Rather? Or talk to the Text Bot Shiloh? (type WYR or Shiloh, you can alternate between the two at any point.)"
# print "Do you want to play a game of Would You Rather? Or talk to the Text Bot Shiloh? (type WYR or Shiloh, you can alternate between the two at any point.)"
media_links_for_happy = ["https://www.buzzfeed.com/kaelintully/jurassic-park-is-a-gr8-film-raptor-shriek-all-the-damn-time?utm_term=.vnG4WN1zwV#.dj5XPlKv3w", "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww4.pictures.zimbio.com%2Fmp%2FHuMZPUQrZeql.jpg&imgrefurl=http%3A%2F%2Fwww.zimbio.com%2FMovie%2BNews%2Farticles%2FvVqgDGD2AFT%2FEveryone%2BObsessed%2BInsanely%2BCute%2BBaby%2BDory&docid=kD-rxCfvcCdtMM&tbnid=g1G5p7E8gVILmM%3A&w=600&h=400&bih=630&biw=1280&ved=0ahUKEwjmrJOYh5XOAhUSBh4KHUNXCMcQMwhvKBkwGQ&iact=mrc&uact=8"]
media_links_for_sad = ["https://www.google.com/imgres?imgurl=http%3A%2F%2Fmedia.brostrick.com%2Fwp-content%2Fuploads%2F2016%2F03%2F10075517%2Ffunny-donald-trump-president-memes-2016-hair.jpg&imgrefurl=http%3A%2F%2Fwww.brostrick.com%2Fviral%2Ffunny-political-memes-donald-trump-hillary-clinton-sanders-cruz%2F&docid=kyYVY3gYM-nMtM&tbnid=yVn63XKixEuEbM%3A&w=446&h=536&bih=630&biw=1280&ved=0ahUKEwjlkML7h5XOAhWLJB4KHeiYASEQMwheKAAwAA&iact=mrc&uact=8", ]
media_links_for_alright = ["http://www.boredpanda.com/cute-bunnies/", "data:image/jpeg;base64,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", "https://www.youtube.com/watch?v=i3kIpCzLzEo"]

def response_handler(body):
    message = ""
    if body == "wyr":
        message = "For next Would You Rather type in WYR."
        # print "For next Would You Rather type in WYR."
        message = choice(["Would you rather a. live one life that lasts 1,000 years or b. live 10 lives that last 100 years each?", "Would you rather have to a. sneeze but not be able to or b. have something stuck in your eye for an entire year?", "Would you rather a. wear a snow suit in the desert or b. be naked in Antarctica?", "Would you rather a. have no arms or b. no legs?", "Would you rather be filthy rich but suffer depression or be poor but happy?"])
    elif body == "shiloh":
        message = "Hi! My name is Shiloh. How are you?? If you aren't feeling the bestest type :( for some amusing pictures! If you feel as if you are on top of the WOOOORLD type :) for some delightful pictures. If you're feeling just alright type :| for some pleasant pictures."
    if body == ":(":
        return choice(["https://www.google.com/imgres?imgurl=http%3A%2F%2Fmedia.brostrick.com%2Fwp-content%2Fuploads%2F2016%2F03%2F10075517%2Ffunny-donald-trump-president-memes-2016-hair.jpg&imgrefurl=http%3A%2F%2Fwww.brostrick.com%2Fviral%2Ffunny-political-memes-donald-trump-hillary-clinton-sanders-cruz%2F&docid=kyYVY3gYM-nMtM&tbnid=yVn63XKixEuEbM%3A&w=446&h=536&bih=630&biw=1280&ved=0ahUKEwjlkML7h5XOAhWLJB4KHeiYASEQMwheKAAwAA&iact=mrc&uact=8", "https://www.youtube.com/watch?v=kNKu1uNBVkU"])
    elif body == ":)":
        message = choice(["https://www.buzzfeed.com/kaelintully/jurassic-park-is-a-gr8-film-raptor-shriek-all-the-damn-time?utm_term=.vnG4WN1zwV#.dj5XPlKv3w", "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww4.pictures.zimbio.com%2Fmp%2FHuMZPUQrZeql.jpg&imgrefurl=http%3A%2F%2Fwww.zimbio.com%2FMovie%2BNews%2Farticles%2FvVqgDGD2AFT%2FEveryone%2BObsessed%2BInsanely%2BCute%2BBaby%2BDory&docid=kD-rxCfvcCdtMM&tbnid=g1G5p7E8gVILmM%3A&w=600&h=400&bih=630&biw=1280&ved=0ahUKEwjmrJOYh5XOAhUSBh4KHUNXCMcQMwhvKBkwGQ&iact=mrc&uact=8"])
    elif body == ":|":
        message = choice(["http://www.boredpanda.com/cute-bunnies/", "data:image/jpeg;base64,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", "https://www.youtube.com/watch?v=i3kIpCzLzEo"])
    else:
        message = "Invalid command.  Text 'start' to restart the game.  Or text 'pic please' for a random picture"
    return message 

    