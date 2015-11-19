%define name python27-simplejson
%define version 3.7.3
%define realname simplejson
%define release 1%{?dist}
%define debug_package %{nil}

Summary: Simple, fast, extensible JSON encoder/decoder for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Simple, fast, extensible JSON encoder/decoder for Python.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.7.3
- Initial configuration for GeoNode 2.4
