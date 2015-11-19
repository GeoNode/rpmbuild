%define name python27-geonode-announcements
%define version 1.0.5
%define realname geonode-announcements
%define release 1%{?dist}

Summary: Fork of pinax/django-announcements. Announcements for your Django powered website.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/g/geonode-announcements/geonode-announcements-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Fork of pinax/django-announcements. Announcements for your Django powered website.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/\.pyc/d' INSTALLED_FILES

%preun
find /usr/local -type f -name '*pyc' -exec rm {} +

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.0.5
- Initial configuration for GeoNode 2.4
