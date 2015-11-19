%define name python27-pyproj
%define version 1.9.3
%define realname pyproj
%define release 1%{?dist}
%define debug_package %{nil}

Summary: Python interface to PROJ.4 library
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/p/pyproj/pyproj-%{version}.tar.gz
License: OSI Approved
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: proj-devel
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
Requires: proj
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Python interface to PROJ.4 library

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.9.3
- Initial configuration for GeoNode 2.4
