from collections import Counter
import re


class Parser:
    def __init__(self):
        self.re_tweet='RT'
        self.addresse = '@'
        self.stream_txt='stream.txt'
        self.follows_txt='follows.txt'
        pass


    def read_file(self,file_path):
        follow_list =[]
        f = open(file_path)
        line = f.readline()
        while line:
            follow_list.append(line)
            line = f.readline()
        f.close()
        return  follow_list

    #===========================================task 1==============================================
    def get_most_popular_user(self,users):
        try:
            most_popular_user=[]
            followed_list=[]
            for user in users:
                follow_user=user.split()
                for i in range(0, len(follow_user)):
                    if i!=0 :
                        followed_list.append(follow_user[i])
            most_common = [item for item in Counter(followed_list).most_common()]
            most_popular=most_common[0][1]
            for value_common in most_common:
                if most_popular > value_common[1]:
                    break
                else:
                    most_popular_user.append(value_common[0])
            most_popular_user=sorted(most_popular_user, key=lambda v: v.upper())
            print(most_common)
            print("Popular users are:")
            for popular_user in most_popular_user:
                print(popular_user)
        except :
            raise


    #===================================================task 2==========================================================
    def get_top_n_parrots(self,user_tweet_list):
        try:
            #total count of users to display
            n_count = int(input("Enter top n parrots to display:"))
            #lines that contain retweeted text
            user_retweeted_list = []
            for tweet in user_tweet_list:
                user_tweet = tweet.split()
                for i in range(0, len(user_tweet)):
                    if user_tweet[i] == self.re_tweet:
                        user_retweeted_list.append(user_tweet[i - 1])
            top_user_retweet = [item for item in Counter(user_retweeted_list).most_common()]
            user_tweet_set = set()
            for top_tweet in top_user_retweet:
                user_tweet_set.add(top_tweet[1])
                if len(user_tweet_set)==n_count:
                    break
            self.evaluete_top_n_user_tweets(user_tweet_set,top_user_retweet)
        except:
            print("Only integer value is accepted!")
            raise



    def evaluete_top_n_user_tweets(self,user_tweet_set,top_user_retweet):
        # top n user that has the highest retweet
        top_n_user_tweet_list = []
        # arrange values in descending  order
        sorted_user_tweet_set = sorted(user_tweet_set, key=int, reverse=True)
        for user_retweet_val in sorted_user_tweet_set:
            # list used to sort username that tie with each order in lexicographic order
            sorted_tweet_if_tie_list = []
            sorted_tweet_column_index = []
            first_index = ""
            for top_tweet in top_user_retweet:
                if user_retweet_val == top_tweet[1]:
                    #for column manipulation when their is a tie
                    sorted_tweet_column_index.append(top_tweet[0])
            sorted_tweet_column_index=sorted(sorted_tweet_column_index, key=lambda v: v.upper())
            for sorted_index in sorted_tweet_column_index:
                first_index += (sorted_index + "  ")
            top_tweet_sorted_column = (first_index, user_retweet_val)
            sorted_tweet_if_tie_list.append(top_tweet_sorted_column)
            top_n_user_tweet_list += sorted_tweet_if_tie_list

        for user_retweet in top_n_user_tweet_list:
            print(user_retweet[1], user_retweet[0])

    #==============================================task 3======================================================
    def get_worst_troll(self,user_tweet_list):
        try:
            # total count of users to display
            n_count = int(input("Enter top n troll to display:"))
            # lines that contain retweeted text
            user_retweeted_list = []
            for tweet in user_tweet_list:
                user_tweet = tweet.split()
                for i in range(0, len(user_tweet)):
                    if self.addresse in  user_tweet[i]:
                        #add the user number of times he mentioned others......bc @ shows number of times he mentioned others
                        user_retweeted_list.append(user_tweet[0])
            top_mentioned_user = [item for item in Counter(user_retweeted_list).most_common()]
            user_tweet_set = set()
            for user in top_mentioned_user:
                user_tweet_set.add(user[1])
                if len(user_tweet_set) == n_count:
                    break
            self.evaluete_top_n_trolls(user_tweet_set,top_mentioned_user)
        except:
            print("Only integer value is accepted!")
            raise


    def evaluete_top_n_trolls(self, user_tweet_set, top_mentioned_user):
        # top n user that has the highest retweet
        top_n_user_tweet_list = []
        # arrange values in descending  order
        sorted_user_tweet_set = sorted(user_tweet_set, key=int, reverse=True)
        for user_retweet_val in sorted_user_tweet_set:
            # list used to sort username that tie with each order in lexicographic order
            sorted_tweet_if_tie_list = []
            sorted_tweet_column_index = []
            first_index = ""
            for top_tweet in top_mentioned_user:
                if user_retweet_val == top_tweet[1]:
                    # for column manipulation when their is a tie
                    sorted_tweet_column_index.append(top_tweet[0])
            sorted_tweet_column_index = sorted(sorted_tweet_column_index, key=lambda v: v.upper())
            for sorted_index in sorted_tweet_column_index:
                first_index += (sorted_index + "  ")
            top_tweet_sorted_column = (first_index, user_retweet_val)
            sorted_tweet_if_tie_list.append(top_tweet_sorted_column)
            top_n_user_tweet_list += sorted_tweet_if_tie_list

        for user_retweet in top_n_user_tweet_list:
            print(user_retweet[1], user_retweet[0])




    #================================Task 4==============================
    def the_biggest_influencers(self,follow_txt_list,stream_txt_list):
        try:
            remove_non_alpanumeric_characters = re.compile('[^A-Za-z0-9]+')

            # total count of users to display
            n_count = int(input("Enter top n influencers to display:"))
            users_total_number_of_seen_tweet_list = []
            users_total_tweet=[]
# for each tweet..get the users mentioned ,add all the users mentioned to a set list...
#use the user that made the tweet to get all his followers in follow.txt
#the total  users mentioned and total followers show the total people that can see his tweet per tweet made.
            for tweet in stream_txt_list:
                check_if_user_exist_list = set()
                user_tweet = tweet.split()
                # add user to user total tweet to calculate user total tweet....
                if user_tweet:

                   users_total_tweet.append(user_tweet[0])

                   #neeed serious optimization# use the user that made the tweet to get all his followers in follow.txt
                   for user in follow_txt_list:
                       follow_user = user.split()
                       for x in range(0, len(follow_user)):
                           if x != 0:
                               if user_tweet[0] == follow_user[x]:
                                   check_if_user_exist_list.add(follow_user[0])
                                   break

                for i in range(0, len(user_tweet)):
                    if self.addresse in user_tweet[i]:
                        filtered_user= remove_non_alpanumeric_characters.sub('',user_tweet[i])
                        check_if_user_exist_list.add(filtered_user)


                for user_count in  check_if_user_exist_list:
                    users_total_number_of_seen_tweet_list.append(user_tweet[0])


            top_user_with_highest_seen_tweet = [item for item in Counter(users_total_number_of_seen_tweet_list).most_common()]
            users_total_tweet =[item for item in Counter(users_total_tweet).most_common()]
            user_tweet_with_average_seen=self.get_average_tweet_seen(top_user_with_highest_seen_tweet,users_total_tweet)

            user_tweet_set = set()
            for user in user_tweet_with_average_seen:
                user_tweet_set.add(user[1])
                if len(user_tweet_set) == n_count:
                    break

            self.evaluate_average_tweet_seen(user_tweet_set, user_tweet_with_average_seen)
        except:
            raise



    def get_average_tweet_seen(self,top_user_with_highest_seen_tweet,users_total_tweet):
        user_tweet_with_average_seen=[]
        try:
            for users in users_total_tweet:
                for top_user_with_highest_seen_obj in top_user_with_highest_seen_tweet:
                    if users[0]==top_user_with_highest_seen_obj[0]:
                        #average =totalseen/total tweets
                        total_seen=top_user_with_highest_seen_obj[1]
                        total_tweet=users[1]
                        average_seen=float(total_seen/total_tweet)
                        user_average_array=(users[0],average_seen)
                        user_tweet_with_average_seen.append(user_average_array)
            return user_tweet_with_average_seen
        except:
            raise



    def evaluate_average_tweet_seen(self, user_tweet_set, user_tweet_with_average_seen):
        # top n user that has the highest retweet
        top_n_user_tweet_list = []
        try:
            # arrange values in descending  order
            sorted_user_tweet_set = sorted(user_tweet_set, key=int, reverse=True)
            for user_retweet_val in sorted_user_tweet_set:
                # list used to sort username that tie with each order in lexicographic order
                sorted_tweet_if_tie_list = []
                sorted_tweet_column_index = []
                first_index = ""
                for top_tweet in user_tweet_with_average_seen:
                    if user_retweet_val == top_tweet[1]:
                        # for column manipulation when their is a tie
                        sorted_tweet_column_index.append(top_tweet[0])
                sorted_tweet_column_index = sorted(sorted_tweet_column_index, key=lambda v: v.upper())
                for sorted_index in sorted_tweet_column_index:
                    first_index += (sorted_index + "  ")
                top_tweet_sorted_column = (first_index, user_retweet_val)
                sorted_tweet_if_tie_list.append(top_tweet_sorted_column)
                top_n_user_tweet_list += sorted_tweet_if_tie_list

            for user_retweet in top_n_user_tweet_list:
                print(user_retweet[1], user_retweet[0])
        except:
            raise


if __name__ == '__main__':
    parser=Parser()
    # #parser.get_most_popular_user(parser.read_file("follows.txt"))
    # parser.get_top_n_parrots(parser.read_file(parser.stream_txt))
    # # #parser.get_worst_troll(parser.read_file("parser.stream_txt"))
    parser.the_biggest_influencers(parser.read_file('testing.txt'),parser.read_file('test.txt'))