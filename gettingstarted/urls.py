from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import Activites.urls
from . import views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
admin.site.site_title = "JCI ci :: Admin"
admin.site.site_header = "Back office de JCI Cote d'Ivoire"
urlpatterns = [
	path("", views.index.as_view(), name="home"),
    path("users/", include(profiles.urls)),
    path("", include(accounts.urls)),
    path("activites/", include(Activites.urls)),
    path("details/actualite/<titre>/", views.Details.as_view(), name="details_actu"),
    path("details/publication/<int:id>/", views.Details_pub.as_view(), name="details_publi"),
    path("actulites/", views.ActualitesView.as_view(), name="Actualites"),
    path("a_propos/", views.About.as_view(), name='about'),
    path("mediatheque/gallerie-photo/", views.Gallerie.as_view(), name='Gallerie'),
    path("a_propos/guide_du_membre/", views.Guide.as_view(), name='Guide'),
    path("a_propos/constitution/", views.Constitution.as_view(), name='Constitution'),
    path('presidents/', views.PresidentsView.as_view(), name='presidents'),
    path("recherche/resultats/", views.ResultatRech.as_view(), name='Recherche'),
    path("admin/", admin.site.urls),
]

# User-uploaded files like profile pics need to be served in development
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
