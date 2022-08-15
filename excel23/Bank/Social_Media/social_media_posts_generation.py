from social_media_user import social_media_user_account

class Social_Media_Posts_generation:
    def __init__(self,name,user_account,Social_Media_Post):
        self.name= name
        self.user_account= user_account
        self.Social_Media_Post= Social_Media_Post

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_user_account(self):
        return self.user_account
    def set_user_account(self,user_account):
        self.user_account =user_account
    def get_Social_Media_Post(self):
        return self.Social_Media_Post
    def set_Social_Media_Post(self,Social_Media_Post):
        self.Social_Media_Post =Social_Media_Post
    def __str__(self):
        return f"name:{self.get_name()}  user_account:{self.get_user_account()} Social_Media_Post:{self.get_Social_Media_Post()}"
    
ibim=Social_Media_Posts_generation('ibim','Ibimfingers','picture')
print(ibim)
