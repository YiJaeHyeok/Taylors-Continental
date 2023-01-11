from django.http import HttpResponse
import json
 
from MyApplication.MongoDbManager import MongoDbManager
 
def specific_user(request, username):
    def get():
       users = MongoDbManager().get_users_from_collection({'name': username})
       response = users[0]
        del response['_id']
 
        return HttpResponse(json.dumps(response), status=200)
 
    def post():
        try:
            age, job = request.POST['age'], request.POST['job']
        except:
            return HttpResponse(status=400)
 
       user = {
            'name': username,
            'age': age,
            'job' : job
        }
 
        result = MongoDbManager().add_user_on_collection(user)
        return HttpResponse(status=201) if result else HttpResponse(status=500)
 
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse(status=405)
 
def all_users( request):
    def get():
       users = MongoDbManager().get_users_from_collection({})
       response = []
        for user in users:
            del user['_id']
           response.append(user)
 
        return HttpResponse(json.dumps(response), status=200)
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
