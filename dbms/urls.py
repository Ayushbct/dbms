from django.contrib import admin
from django.urls import path
from dbms import views as dbmsviews
from home import views as homeviews

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('home.urls'))
    path('',dbmsviews.dbmshome,name='dbmshome'),
    # path("dbmsnewapp",dbmsviews.dbmsnewapp,name='dbmsnewapp'),
    # path("newapp",homeviews.newapp,name='newapp'),

    path("dbmsfileslist",dbmsviews.dbmsfileslist,name='dbmsfileslist'),
    # path("dbmsfileslist/dbmsuploadfiles",dbmsviews.dbmsuploadfiles,name='dbmsuploadfiles'),


    path('signup',homeviews.handleSignup,name='handleSignup'),
    path('login',homeviews.handleLogin,name='handleLogin'),
    path('logout',homeviews.handleLogout,name='handleLogout'),
    

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
