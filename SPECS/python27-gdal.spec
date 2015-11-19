%define name python27-gdal
%define version 1.11.1
%define realname GDAL
%define release 1%{?dist}
%define debug_package %{nil}

Summary: GDAL: Geospatial Data Abstraction Library
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/G/GDAL/GDAL-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: gdal-devel = 1.11.1
Requires: python27
Requires: gdal = 1.11.1
Requires: python27-numpy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
GDAL: Geospatial Data Abstraction Library

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/\.pyc/d' INSTALLED_FILES

%preun
find /usr/local -type f -name '*pyc' -exec rm {} +

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.11.1
- Initial configuration for GeoNode 2.4
