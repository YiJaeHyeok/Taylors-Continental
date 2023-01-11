from django.http import HttpResponse
from django.template import loader
 
from MyApplication.MongoDbManager import MongoDbManager
 
def specific_user(request, username):
    def get():
       db_user_data = MongoDbManager().get_users_from_collection({'name': username})
 
       user = db_user_data[0]
        del user['_id']
 
        template = loader.get_template('User.html')
        return HttpResponse(template.render({'userData':[user]}, request))
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
 
def all_users(request):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({})
 
       users = []
        for user in dbUserData:
            del user['_id']
           users.append(user)
 
        template = loader.get_template('User.html')
        return HttpResponse(template.render({'userData': users}, request))
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
