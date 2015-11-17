%define name python27-pycsw
%define version 1.10.3
%define realname pycsw
%define release 1%{?dist}

Summary: pycsw is an OGC CSW server implementation written in Python
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/p/pycsw/pycsw-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
pycsw is an OGC CSW server implementation written in Python.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.10.3
- Initial configuration for GeoNode 2.4
