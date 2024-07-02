import praw

#MUST BE REMOVED BEFORE GITHUB PUBLISH
reddit = praw.Reddit(

)

#Args = the number of post to retrieve (No more than 100 at a time)
#returns the top_posts object
def getHotPost(maxPosts):
    subreddit = reddit.subreddit("wallstreetbets")
    return subreddit.hot(limit = maxPosts)


#No args
#Returns the comment object for DDT
def getTopCommentsDDT():
    #getHotPost(1) is always DDT
    DDT = getHotPost(1)
    for post in DDT:
        comments = post.comments
        return comments