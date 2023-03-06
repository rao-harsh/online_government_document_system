from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login_view"),
    path("logout/",views.logout_view,name="logout"),
    path("contact/",views.contact_us,name="contact"),
    path("about/",views.about,name="about"),
    path("required-ncl-docs/",views.required_ncl_docs,name="required-ncl-docs"),
    path("required-income-docs/",views.required_income_certificate_docs,name="required-income-docs"),
    path("income-certificate/",views.income_certificate,name="income-certificate"),
    path("non-creamy-layer/",views.non_creamy_layer,name="non-creamy-layer"),
    path("income-certificate-form/",views.print_income,name="income-certificate-form"),
    path("non-creamy-layer-form/",views.print_non_creamy_layer,name="non-creamy-layer-form"),
    # path("my-profile/",views.my_profile,name="my-profile"),
    # path("income-certificate-data/",views.income_certificate_data,name="income-certificate-data"),
    # path("non-creamy-layer-data/",views.non_creamy_layer_data,name="non_creamy_layer_data"),
    # path("query/",views.query,name="query"),
    # path("query-answer/",views.query_answer,name="query-answer")
]
