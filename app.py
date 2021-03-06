import praw
import os

    
popular_post = """
To all who have come from r/popular, welcome to r/Dogs! We are a discussion-based subreddit dedicated to support, inform, and advise dog owners.

Before you post or comment, please **review the subreddit rules [here](https://www.reddit.com/r/dogs/wiki/index)**. Submissions which break the rules will be removed.

r/Dogs has the [ultimate goals](https://www.reddit.com/r/dogs/wiki/index#wiki_purpose) of fostering a better, science-based understanding of dogs among the general public, promoting responsible dog ownership, helping users build better, healthier relationships with their dogs, and providing a space to connect and discuss with others who have dogs and who are involved in various aspects of the dog hobby.

Per our Harm Reduction rules, **we encourage training advice and recommendations to follow “Least Intrusive, Minimally Aversive” protocols**. You can read more about why that’s the case [here](https://m.iaabc.org/about/lima/). While no training tools are excluded from properly framed discussion in r/dogs, we do reserve the right to remove content which does not follow the LIMA approach.

Please note, this sub supports the reputable, ethical, and responsible breeding of dogs as well as adoption. Low effort “adopt don’t shop” comments will be removed and commenters may be subject to temporary or permanent bans upon the discretion of the moderator team.

Finally, r/Dogs has a low tolerance for [disrespectful and antagonistic behavior](https://www.reddit.com/r/dogs/wiki/index#wiki_rules_of_engagement). People come to this sub to learn and discuss, make your comments constructive and respectful even if you feel other users are being antagonistic and disrespectful in return. If you believe another user is engaging in antagonistic behavior, please utilize the report button and a moderator will review the comment(s).

If you wish to stick around, please feel free to comment in our Daily Bark threads, pinned to the top of the sub, to introduce yourself, your dog, and talk about all the little things which may not require a full post to discuss. Thanks for reading and enjoy your stay!

*This is an automated message. If you have questions for the moderators of r/dogs, you can message them [here](https://www.reddit.com/message/compose/?to=/r/dogs).*


"""
def bot_login():
        #put this in env variables
	r = praw.Reddit(username = os.environ.get("username"),
				password = os.environ.get("password"),
				client_id = os.environ.get("client_id"),
				client_secret = os.environ.get("secret"),
				user_agent = os.environ.get("user_agent"))
	print("I logged in")

	return r

                
def run_bot(r):
    with open("posts.txt", mode="w+"):
        for post in r.subreddit("popular").stream.submissions(skip_existing=True):
            if post.subreddit == "dogs":
                newComment = post.reply(popular_post)
                newComment.mod.distinguish(sticky=True)
                print("made popular sticky post")

print("starting to run bot")
r = bot_login()
run_bot(r)
