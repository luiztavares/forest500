import tweepy
import json

class TwitterAPI:
    def __init__(self):
        self.keys = [['2m2IZIw55y8XMTRLep2gx6van','kcF8ZCrA6yK4zZFVkGYSkEd7W5sopi5GFjJoQLg1n75WA22Vlc'],
                    ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
                    ['IQKbtAYlXLripLGPWd0HUA','GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'],
                    ['CjulERsDeqhhjSme66ECg','IQWdVyqFxghAtURHGeGiWAsmCAGmdW3WmbEx6Hck'],
                    ['3rJOl1ODzm9yZy63FACdg','5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8'],
                    ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
                    ['d0CTc4Zg9pufCnMkteDc7w','z4FMZhP87U5QEwycggDe5JN6TDDh7xEyhnAcEpdWk'],
                    ['CVbiuNGV6MeQCsku7SUZnejVb','AXzQ9ZSxu1JPWbQNXHj4Zn1uI32fMDviLDYyKM6RihwPjGz6i9'],
                    ['53aMoQiFaQfoUtxyJIkGdw','Twnh3SnDdtQZkJwJ3p8Tu5rPbL5Gt1I0dEMBBtQ6w'],
                    ['7Uifmz2gkHF8RcOcMtItTJRoF', 'YmcL95Yy15zvwAfGVaCrbGaUkcWo6wv0OT9RXCOxWfoHwuY1RT'],
                    ]
                    
        self.apis = []
        for x in self.keys:
            try:
                auth = tweepy.AppAuthHandler(x[0], x[1]) 
                authenticated = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
                self.apis.append(authenticated)
            except:
                print(f'Failure on {x[0]}, does not work any more')
    @property
    def keysLen(self,):
        return len(self.keys)

    def splitList(self,alist, wanted_parts=1):
        length = len(alist)
        return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]

    def getFriendsIds(self,user_ids):
        relation = []
        for i,user_id in enumerate(user_ids):
            print(user_id,i)
            if(False):#(i // 15)%2):
                for x in tweepy.Cursor(self.apis[0].friends, user_id=user_id, count=200).items():
                    rel = {'source':user_id, 'target':x.id_str}
                    relation = relation.append(rel,ignore_index = True)
                time.sleep( 5 )
            else:
                try:
                    for x in tweepy.Cursor(self.apis[(i)%self.keysLen].friends_ids, user_id=user_id, count=5000).items():
                        rel = {'source':user_id, 'target':x}
                        relation.append(rel)
                except:
                    pass
        return relation



#apix = api.apis[0]

###############################
# import json
# import threading

# all_data = {}

# def split_list(alist, wanted_parts=1):
#     length = len(alist)
#     return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
#             for i in range(wanted_parts) ]


# def get_tweets(tweets_ids,index):
#     apix = api.apis[index]
#     all_data['{}'.format(index)] = []
#     for i in range(math.ceil(len(tweets_ids)/100)):
#         data = []
#         print("{} of {}".format(i,math.ceil(len(tweets_ids)/100)) )
#         query = tweets_ids[i*100:(i+1)*100:]
#         #client = api.apix.apis[i%self.keysLen]
#         resp = apix.statuses_lookup(id_ = query,tweet_mode='extended',include_entities=True,trim_user=False)
#         data = [x._json for x in resp]
#         all_data['{}'.format(index)] += data
#         if(index > 100):
#             break

# user_id_splited = split_list(tweets_ids,api.keysLen)
# threads = list()

# #create and start trhead execution
# for index in range(api.keysLen):
#     thread = threading.Thread(target=get_tweets, args=(user_id_splited[index],index))
#     threads.append(thread)
#     thread.start()

# #wait all threads end
# for index, thread in enumerate(threads):
#     thread.join()

###########################################
# import json
# apix = api.apis[0]

# for i,id in enumerate(resp):
#     data = []
#     print(id)
    
#     try:
#         for x in tweepy.Cursor(apix.user_timeline, screen_name=id,tweet_mode="extended", count=200).items():
#             data.append(x._json)
#     except:
#         pass
#     with open('tweet/{}.json'.format(id), 'w',encoding='utf-8') as json_file:
#         json.dump(data, json_file)