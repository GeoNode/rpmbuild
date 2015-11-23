# Define Constants
%define name geonode
%define version 2.4.0
%define release 0.1%{?dist}
%define _unpackaged_files_terminate_build 0
%define __os_install_post %{nil}
%define debug_package %{nil}

Name:             %{name}
Version:          %{version}
Release:          %{release}
Summary:          Open Source Geospatial Content Management System
Group:            Applications/Engineering
License:          GPLv2
Source0:          geonode-project.zip
Source1:          supervisord.conf
Source2:          geonode.init
Source3:          geonode.conf
Source4:          proxy.conf
Source5:          local_settings.py
Source6:          robots.txt
Source7:          geonode-config
Requires(pre):    /usr/sbin/useradd
Requires(pre):    /usr/bin/getent
Requires(pre):    bash
Requires(postun): /usr/sbin/userdel
Requires(postun): bash
Requires:         gdal = 1.11.1
Requires:         geonode-geoserver = 2.7
Requires:         git
Requires:         httpd
Requires:         postgresql93
Requires:         postgresql93-server
Requires:         postgis21-postgresql93
Requires:         proj
Requires:         python27
Requires:         python27-amqp = 1.4.6
Requires:         python27-anyjson = 0.3.3
Requires:         python27-awesome-slugify = 1.6.2
Requires:         python27-beautifulsoup4 = 4.2.1
Requires:         python27-billiard = 3.3.0.20
Requires:         python27-celery = 3.1.17
Requires:         python27-dateutil = 2.4.2
Requires:         python27-django-activity-stream = 0.4.5beta1
Requires:         python27-django-appconf = 0.5
Requires:         python27-django-autocomplete-light = 2.2.10
Requires:         python27-django-bootstrap3-datetimepicker = 2.2.3
Requires:         python27-django-celery = 3.1.16
Requires:         python27-django-downloadview = 1.2
Requires:         python27-django-extensions = 1.2.5
Requires:         python27-django-forms-bootstrap = 3.0.1
Requires:         python27-django-friendly-tag-loader = 1.1
Requires:         python27-django-geoexplorer = 4.0.5
Requires:         python27-django-guardian = 1.2.0
Requires:         python27-django-haystack = 2.1.0
Requires:         python27-django-jsonfield = 0.9.12
Requires:         python27-django-leaflet = 0.13.7
Requires:         python27-django-modeltranslation = 0.8
Requires:         python27-django-mptt = 0.6.1
Requires:         python27-django-nose = 1.2
Requires:         python27-django-pagination = 1.0.7
Requires:         python27-django-polymorphic = 0.5.6
Requires:         python27-django-taggit = 0.12
Requires:         python27-django-tastypie = 0.11.0
Requires:         python27-django = 1.6.11
Requires:         python27-flake8 = 2.3.0
Requires:         python27-gdal = 1.11.1
Requires:         python27-geonode = 2.4
Requires:         python27-geolinks = 0.0.1
Requires:         python27-geonode-agon-ratings = 0.3.1
Requires:         python27-geonode-announcements = 1.0.5
Requires:         python27-geonode-arcrest = 10.2
Requires:         python27-geonode-avatar = 2.1.4
Requires:         python27-geonode-dialogos = 0.4
Requires:         python27-geonode-notification = 1.1.1
Requires:         python27-geonode-user-accounts = 1.0.10
Requires:         python27-geonode-user-messages = 0.1.2
Requires:         python27-gisdata = 0.5.4
Requires:         python27-gsconfig = 1.0.3
Requires:         python27-gsimporter = 1.0.0
Requires:         python27-httplib2 = 0.8
Requires:         python27-kombu = 3.0.26
Requires:         python27-lxml = 3.4.4
Requires:         python27-mccabe = 0.3.1
Requires:         python27-meld3 = 1.0.2
Requires:         python27-mimeparse = 0.1.4
Requires:         python27-multipartposthandler = 0.1.0
Requires:         python27-nose = 1.0.0
Requires:         python27-numpy = 1.9.2
Requires:         python27-owslib = 0.8.13
Requires:         python27-paver = 1.2.1
Requires:         python27-pep8 = 1.6.2
Requires:         python27-pillow = 2.9.0
Requires:         python27-pinax-theme-bootstrap-account = 1.0b2
Requires:         python27-pinax-theme-bootstrap = 3.0a11
Requires:         python27-psycopg2 = 2.6.1
Requires:         python27-pycsw = 1.10.3
Requires:         python27-pyelasticsearch = 0.6.1
Requires:         python27-pyflakes = 0.9.2
Requires:         python27-pyproj = 1.9.3
Requires:         python27-pytz = 2015.4
Requires:         python27-regex = 2015.07.12
Requires:         python27-requests = 2.7.0
Requires:         python27-setuptools
Requires:         python27-shapely = 1.3.1
Requires:         python27-simplejson = 3.7.3
Requires:         python27-six = 1.9.0
Requires:         python27-supervisor = 3.1.3
Requires:         python27-transifex-client = 0.10
Requires:         python27-unidecode = 0.04.18
Requires:         python27-uwsgi = 2.0.11.1
AutoReqProv:      no
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GeoNode is a web-based application and platform for developing geospatial information systems (GIS) and for deploying spatial data infrastructures (SDI).

%prep

%build

%install
# geonode-project
LIB=$RPM_BUILD_ROOT%{_localstatedir}/lib
mkdir -p $LIB
unzip %{SOURCE0} -d $LIB
pushd $LIB
mv %{name}-project-master %{name}
pushd %{name}
mkdir -p $LIB/%{name}
mv project_name sdi
mkdir -p $LIB/%{name}/sdi/{media,uploaded}
popd && popd
sed -i "s/{{ project_name }}/sdi/g" $LIB/%{name}/manage.py
sed -i "s/{{ project_name }}/sdi/g" $LIB/%{name}/setup.py
sed -i "s/{{ project_name }}/sdi/g" $LIB/%{name}/sdi/wsgi.py
sed -i "s/{{ project_name }}/sdi/g" $LIB/%{name}/sdi/settings.py

# setup supervisord configuration
SUPV_ETC=$RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $SUPV_ETC
install -m 644 %{SOURCE1} $SUPV_ETC/supervisord.conf
GEONODE_LOG=$RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $GEONODE_LOG

# setup init script
INITD=$RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p $INITD
install -m 751 %{SOURCE2} $INITD/%{name}

# setup httpd configuration
HTTPD_CONFD=$RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
mkdir -p $HTTPD_CONFD
install -m 644 %{SOURCE3} $HTTPD_CONFD/%{name}.conf
install -m 644 %{SOURCE4} $HTTPD_CONFD/proxy.conf

# setup geonode configuration directory
GEONODE_CONF=$RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $GEONODE_CONF
# local_settings.py
install -m 775 %{SOURCE5} $GEONODE_CONF/local_settings.py

# additions to geonode directory
# robots.txt
install -m 755 %{SOURCE6} $LIB/%{name}/sdi/templates/robots.txt
# add robots.txt as a TemplateView in django original file is urls.py.bak
sed -i "s|urlpatterns = patterns('',|urlpatterns = patterns('',\\n\
url(r'^/robots\\\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),|" $LIB/%{name}/sdi/urls.py

# geonode-config command
LOCAL_BIN=$RPM_BUILD_ROOT%{_prefix}/local/bin
mkdir -p $LOCAL_BIN
install -m 755 %{SOURCE7} $LOCAL_BIN/

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -d %{_localstatedir}/lib/geonode -g %{name} -s /bin/bash -c "GeoNode Daemon User" %{name}

%post
if [ $1 -eq 1 ] ; then
  ln -s %{_sysconfdir}/%{name}/local_settings.py %{_localstatedir}/lib/%{name}/sdi/local_settings.py
fi

%preun

%postun

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(755,%{name},%{name},755)
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/manage.py
%{_localstatedir}/lib/%{name}/setup.py
%dir %{_localstatedir}/lib/%{name}/sdi
%{_localstatedir}/lib/%{name}/sdi/__init__.py
%{_localstatedir}/lib/%{name}/sdi/settings.py
%{_localstatedir}/lib/%{name}/sdi/static/README
%{_localstatedir}/lib/%{name}/sdi/static/css/site_base.css
%{_localstatedir}/lib/%{name}/sdi/static/img/README
%{_localstatedir}/lib/%{name}/sdi/static/js/README
%{_localstatedir}/lib/%{name}/sdi/templates/robots.txt
%{_localstatedir}/lib/%{name}/sdi/templates/site_base.html
%{_localstatedir}/lib/%{name}/sdi/templates/site_index.html
%{_localstatedir}/lib/%{name}/sdi/urls.py
%{_localstatedir}/lib/%{name}/sdi/wsgi.py
%config(noreplace) %{_sysconfdir}/%{name}/local_settings.py
%defattr(775,%{name},%{name},775)
%dir %{_localstatedir}/lib/%{name}/sdi/media
%dir %{_localstatedir}/lib/%{name}/sdi/uploaded
%defattr(744,%{name},%{name},744)
%dir %{_localstatedir}/log/%{name}
%defattr(644,%{name},%{name},644)
%dir %{_sysconfdir}/%{name}/
%defattr(644,apache,apache,644)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/proxy.conf
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/supervisord.conf
%defattr(-,root,root,-)
%{_prefix}/local/bin/geonode-config
%config %{_sysconfdir}/init.d/%{name}

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.4
- Initial configuration for GeoNode 2.4
