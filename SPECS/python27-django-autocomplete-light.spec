%define name python27-django-autocomplete-light
%define version 2.2.10
%define realname django-autocomplete-light
%define release 1%{?dist}

Summary: Fresh autocompletes for Django
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-autocomplete-light/django-autocomplete-light-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
django-autocomplete-light’s purpose is to enable autocompletes quickly and properly in a django project: it is the fruit of half a decade of R&D and thousands of contributions. It was designed for Django so that every part overridable or reusable independently. It is stable, tested, documented and fully supported: it tries to be a good neighbour in Django ecosystem.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/.pyc/d' INSTALLED_FILES

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.4.14
- Initial configuration for GeoNode 2.4
