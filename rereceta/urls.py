from django.urls import path
from . import views
app_name = "rereceta"
urlpatterns = [
    path("", views.RecetaListView.as_view(), name="index"),
    path("<int:pk>/", views.RecetaDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.RecetaUpdateView.as_view(), name="update"),
    path("create/", views.RecetaCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.RecetaDeleteView.as_view(), name="delete"),
    path("categoria", views.CategoriaListView.as_view(), name="categoria-index"),
    path("categoria/<int:pk>/", views.CategoriaDetailView.as_view(), name="categoria-detail"),
    path("categoria/<int:pk>/update/", views.CategoriaUpdateView.as_view(), name="categoria-update"),
    path("categoria/create/", views.CategoriaCreateView.as_view(), name="categoria-create"),
    path("categoria/<int:pk>/delete/", views.CategoriaDeleteView.as_view(), name="categoria-delete"),
    path("imagen/create/", views.ImagenCreateView.as_view(), name="imagen-create"),
    path("integrante/create/", views.IntegranteCreateView.as_view(), name="integrante-create"),
]
