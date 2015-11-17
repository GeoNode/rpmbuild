%define name python27-requests
%define version 2.7.0
%define realname requests
%define release 1%{?dist}

Summary: Python HTTP for Humans.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Python HTTP for Humans.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.7.0
- Initial configuration for GeoNode 2.4
