%define name python27-django-geoexplorer
%define version 4.0.5
%define realname django-geoexplorer
%define release 1%{?dist}

Summary: Use GeoExplorer in your django projects.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-geoexplorer/django-geoexplorer-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Use GeoExplorer in your django projects.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 4.0.5
- Initial configuration for GeoNode 2.4
