
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        
        
    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
        
    def get_timeline(self):
        timeline = []
        for user in self.following:
            for twit in user.posts:
                timeline.append(twit)
                
        # for user in self.following:
        #     timeline += user.posts
                
                
        timeline = sorted(timeline, key=lambda post: post.timestamp, reverse=False)
        return timeline
        
        # self.following == [User1, User2, User3, User4]
        # User1.posts == [Post1, Post2, Post3]
        # User2.posts == [Post1, Post2, Post3]
        # User3.posts == [Post1, Post2, Post3]
        # User4.posts == [Post1, Post2, Post3]
        # go through the list of people your following (self.following)
        # then ADD/OR append all of their posts to your timeline

    def follow(self, other):
        self.following.append(other)