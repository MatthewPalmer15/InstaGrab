import instaloader

app = instaloader.Instaloader()

#USER = input()#
#PASSWORD = input()
#app.login(USER, PASSWORD)

IGusername = input("Enter Username: ")
app.download_profile(IGusername, profile_pic_only=True)

profile = instaloader.Profile.from_username(app.context, IGusername)
print("Username:", profile.username)
print("User ID:", profile.userid)
print("Post Count:", profile.mediacount)
print("IGTV Count:", profile.igtvcount)
print("Followers:", profile.followers)
print("Followees:", profile.followees)
print("Bio:", profile.biography)
print("Full Name: ", profile.full_name)
print("Private?", profile.is_private)

#for highlight in app.get_highlights(IGusername):
 #   for item in app.get_items():
 #       app.download_storyitem(item, '{}/{}'.format(app.owner_username, app.title))
        
posts = profile.get_posts()

for post in posts:
    print("Profile Post:", post.profile)
    print("Uploaded:", post.date)
    print("One Post Image:", post.mediacount)
    print("Likes:", post.likes)
    print("Description:", post.caption)
    print("Hashtags:", post.caption_hashtags)
    print("Comments:", post.comments)
    print("Date local:", post.date_local)
    #print("Sponsored?", post.is_sponsored)
    print("Location:", post.location)
    print("Tagged Users:", post.tagged_users)
    #priprint("Image Link", post.url)
    print("Duration:", post.video_duration)
    print("Views:", post.video_view_count)
    app.download_post(post, target=f"{profile.username}")
    # instance.download_post(post,target="folderName")
    print("\n")

    #instance.download_hashtag(hashtag="your_hashtag_here",max_count=10)
    #followers = [follower.username for follower in profile.get_followers()]
    #followees = [followee.username for followee in profile.get_followees()]

