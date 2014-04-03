from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='/email/')),
    # url(r'^blog/', include('blog.urls')),
	url(r'^email/send/$', 'core.views.sendmail' , name="sendmail"),
	url(r'^email/ok/$', 'core.views.ok' , name="ok"),
	url(r'^email/ko/$', 'core.views.ko' , name="ko"),
	#url(r'^email/ko/$', 'core.views.invalid' , name="invelid"),
	url(r'^email/$', 'core.views.email' , name="email"),
    url(r'^admin/', include(admin.site.urls)),
)
