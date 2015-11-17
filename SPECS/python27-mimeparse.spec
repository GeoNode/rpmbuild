%define name python27-mimeparse
%define version 0.1.4
%define realname python-mimeparse
%define release 1%{?dist}

Summary: A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/p/python-mimeparse/python-mimeparse-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges..

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.1.4
- Initial configuration for GeoNode 2.4
