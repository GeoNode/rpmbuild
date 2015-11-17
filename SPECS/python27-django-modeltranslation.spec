%define name python27-django-modeltranslation
%define version 0.8
%define realname django-modeltranslation
%define release 1%{?dist}

Summary: Translates Django models using a registration approach.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-modeltranslation/django-modeltranslation-%{version}.tar.gz

License: New BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
The modeltranslation application can be used to translate dynamic content of existing models to an arbitrary number of languages without having to change the original model classes. It uses a registration approach (comparable to Django’s admin app) to be able to add translations to existing or new projects and is fully integrated into the Django admin backend.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.8
- Initial configuration for GeoNode 2.4
