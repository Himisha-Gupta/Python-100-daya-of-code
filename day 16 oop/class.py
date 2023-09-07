class Users:
    def __init__(self , user_id , username,):
        self.id = user_id
        self.username= username
        self.follower = 0
        self.following = 0

    def follow(self, another_user):
        self.following += 1
        another_user.follower += 1


user_1 = Users(101 , "Himisha" )
#important to pass the arguments
# print(user_1.id)
# print(user_1.username)
# print(user_1.follower)
user_2 = Users(102 , "hhjhjhj")
user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_1.follower)
print(user_2.follower)