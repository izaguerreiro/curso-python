from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'conectedin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'perfis.views.index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir'),
)

