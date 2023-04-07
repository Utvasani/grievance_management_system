from . import views
from django.urls import path
urlpatterns = [
    path('', views.super_admin_index,name="super_admin_index"),
    path('manageCollage/', views.manageCollage,name="manageCollage"),
    path('manageDepartment/', views.manageDepartment,name="manageDepartment"),
    path('manageDesignation/',views.manageDesignation,name='manageDesignation'),
    path('manageUsers/',views.manageUsers,name='manageUsers'),
    path('manageRegistration/',views.manageRegistration,name='manageRegistration'),
    path('manageLogin/',views.manageLogin,name='manageLogin'),
    path('manageLogout/',views.manageLogout,name='manageLogout'),
    path('changePassword/',views.changePassword,name='changePassword'),
    path('addCollage/',views.addCollage,name='addCollage'),
    path('deleteCollage/<int:id>', views.deleteCollage, name='deleteCollage'),
    path('updateCollage/<int:id>', views.updateCollage, name='updateCollage'),
    path('login/', views.manageLogin, name='manageLogin'),
    path('functionLogin/', views.functionLogin, name='functionLogin'),


    path('addDesignation/',views.addDesignation,name='addDesignation'),
    path('deleteDesignation/<int:id>', views.deleteDesignation, name='deleteDesignation'),
    path('updateDesignation/<int:id>', views.updateDesignation, name='updateDesignation'),

    path('addDepartment/',views.addDepartment,name='addDepartment'),
    path('deleteDepartment/<int:id>', views.deleteDepartment, name='deleteDepartment'),
    path('updateDepartment/<int:id>', views.updateDepartment, name='updateDepartment'),

    path('addUser/',views.addUser,name='addUser'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('updateUser/<int:id>', views.updateUser, name='updateUser'),

    path('addRegistration/',views.addRegistration,name='addRegistration'),
    path('deleteRegistration/<int:id>', views.deleteRegistration, name='deleteRegistration'),
    path('updateRegistration/<int:id>', views.updateRegistration, name='updateRegistration'),


    
]