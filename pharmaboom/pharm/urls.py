from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('manager_edit/', views.manager_edit, name='manager_edit'),

    path('manager_edit/pharm/', views.PharmListView.as_view(), name='ph_list'),
    path('manager_edit/pharm/detail/<int:pk>/', views.PharmDetailView.as_view(), name='ph_info'),
    path('manager_edit/pharm/create/', views.PharmCreateView.as_view(), name='pharm_create'),
    path('manager_edit/pharm/update/<int:pk>/', views.PharmUpdateView.as_view(), name='pharm_update'),
    path('manager_edit/pharm/delete/<int:pk>/', views.PharmDeleteView.as_view(), name='pharm_delete'),
    path('conf_del_pharm/<int:pk>/', views.confirm_delete_pharm, name='conf_del_pharm'),

    path('manager_edit/drugs/', views.DrugListView.as_view(), name='drugs_list'),
    path('manager_edit/products/', views.ProductListView.as_view(), name='products_list'),
    path('manager_edit/drugs/detail/<int:pk>/', views.DrugDetailView.as_view(), name='drug_detail'),
    path('manager_edit/drugs/create/', views.DrugCreateView.as_view(), name='drug_create'),
    path('manager_edit/drugs/update/<int:pk>/', views.DrugUpdateView.as_view(), name='drug_update'),
    path('conf_del_drug/<int:pk>/', views.confirm_delete_drug, name='conf_del_drug'),
    path('manager_edit/drug/delete/<int:pk>/', views.DrugDeleteView.as_view(), name='drug_delete'),
    path('manager_edit/product_entry/', views.add_prod_entry, name='product_entry'),

    path('order_create/', views.create_order, name='order_create'),
    path('order_delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('order_update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/', views.orders, name='orders_list'),
    path('conf_del_order/<int:pk>/', views.confirm_delete_order, name='conf_del_order'),

    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('sign_up/', views.sign_up, name='sign_up'),

    path('api/pharm/all_products/', views.ProductListAPIView.as_view()),

]
