%define name python27-shapely
%define version 1.3.1
%define realname Shapely
%define release 1%{?dist}

Summary: Geometric objects, predicates, and operations
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/S/Shapely/Shapely-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: geos-devel
Requires: python27
Requires: geos
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Geometric objects, predicates, and operations

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.3.1
- Initial configuration for GeoNode 2.4
