from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    # math
    path("math/", views.MathView.as_view(), name="math"),
    path("math/notation", views.NotationView.as_view(), name="notation"),
    path("math/percent", views.PercentView.as_view(), name="percent"),

    # unit
    path("unit/", views.UnitView.as_view(), name="unit"),
    path("unit/temperature", views.TemperatureView.as_view(), name="temperature"),
    path("unit/area", views.AreaView.as_view(), name="area"),
    path("unit/mass", views.MassView.as_view(), name="mass"),
    
]
