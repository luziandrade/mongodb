import pymongo

uri = "mongodb+srv://root:010203@myfirstcluster-ekkz4.mongodb.net/myTestDB?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
database = client['myTestDB']
collection = database['myFirstDB']


def record():
        wizards = collection.find({})
        for person in wizards:
            print ("Are you afraid of what you'll hear?\nYour Animagus is a {}, {}".format(person['first'],person['last']))

record()
