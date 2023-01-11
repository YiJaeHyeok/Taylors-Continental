from django.urls import path
from MyApplication.Api import HtmlTest, JsonTest
 
urlpatterns = [
    path('json/', JsonTest.all_users, name='JsonAllUser'),
    path('json/<username>', JsonTest.specific_user, name='JsonSpecificUser'),
    path('html/', HtmlTest.all_users, name='HtmlAllUser'),
    path('html/<username>', HtmlTest.specific_user, name='HtmlSpecificUser')
]