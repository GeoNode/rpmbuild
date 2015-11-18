GeoNode rpmbuild for Enterprise Linux 6
----------------------

__as a non-root user with sudo access on an EL6 Operating System...__

```bash
cd ~
sudo yum -y install rpmdevtools
sudo yum -y install http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo yum -y install http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-centos93-9.3-2.noarch.rpm
sudo yum -y update
sudo yum -y install proj-devel postgresql93-devel libxslt-devel pcre-devel gcc gcc-c++ bzip2-devel db4-devel expat-devel gdbm-devel ncurses-devel openssl-devel readline-devel sqlite-devel tk-devel tcl-devel unzip wget libjpeg-devel
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-setuptools.spec
sudo yum -y install ~/rpmbuild/RPMS/*.rpm
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/libkml.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/openjpeg2.spec
sudo yum -y install ~/rpmbuild/RPMS/*.rpm
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/gdal.spec
sudo yum -y install ~/rpmbuild/RPMS/*.rpm
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-amqp.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-anyjson.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-awesome-slugify.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-beautifulsoup4.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-billiard.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-celery.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-dateutil.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-activity-stream.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-appconf.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-autocomplete-light.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-bootstrap3-datetimepicker.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-celery.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-downloadview.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-extensions.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-forms-bootstrap.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-friendly-tag-loader.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-geoexplorer.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-haystack.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-jsonfield.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-leaflet.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-modeltranslation.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-mptt.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-nose.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-pagination.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-polymorphic.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-taggit.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django-tastypie.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-django.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-flake8.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-gdal.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geolinks.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-agon-ratings.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-announcements.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-arcrest.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-avatar.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-dialogos.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-notification.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-geonode-user-accounts.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/geonode-user-messages.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-gisdata.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-gsconfig.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-gsimporter.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-httplib2.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-kombu.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-lxml.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-mccabe.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-meld3.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-mimeparse.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-multipartposthandler.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-nose.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-numpy.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-owslib.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-paver.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pep8.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pillow.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pinax-theme-bootstrap-account.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pinax-theme-bootstrap.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-psycopg2.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pycsw.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pyelasticsearch.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pyflakes.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pyproj.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-pytz.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-regex.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-requests.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-shapely.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-simplejson.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-six.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-supervisor.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-transifex-client.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-unidecode.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/python27-uwsgi.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/geonode.spec
QA_RPATHS=$[ 0x0001|0x0010 ] rpmbuild -bb ~/rpmbuild/SPECS/geonode-geoserver.spec
```
