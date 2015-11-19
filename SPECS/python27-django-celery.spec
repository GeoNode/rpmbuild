%define name python27-django-celery
%define version 3.1.16
%define realname django-celery
%define release 1%{?dist}

Summary: Old django celery integration project.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-celery/django-celery-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
django-celery provides Celery integration for Django; Using the Django ORM and cache backend for storing results, autodiscovery of task modules for applications listed in INSTALLED_APPS, and more.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/\.pyc/d' INSTALLED_FILES

%preun
find /usr/local -type f -name '*pyc' -exec rm {} +

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.1.16
- Initial configuration for GeoNode 2.4
