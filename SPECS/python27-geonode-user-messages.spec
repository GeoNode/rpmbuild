%define name python27-geonode-user-messages
%define version 0.1.2
%define realname geonode-user-messages
%define release 1%{?dist}

Summary: Fork of user-messages: a reusable private user messages application for Django.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/g/geonode-user-messages/geonode-user-messages-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Fork of user-messages: a reusable private user messages application for Django.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.1.2
- Initial configuration for GeoNode 2.4
