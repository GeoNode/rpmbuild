%define name python27-geonode-arcrest
%define version 10.2
%define realname geonode-arcrest
%define release 1%{?dist}

Summary: Wrapper to the ArcGIS REST API, and a Python analogue to the Javascript APIs. Modified to have a version number more pypi friendly by the GeoNode team.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/g/geonode-arcrest/geonode-arcrest-%{version}.tar.gz
License: Apache Software License
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Wrapper to the ArcGIS REST API, and a Python analogue to the Javascript APIs. Modified to have a version number more pypi friendly by the GeoNode team.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 10.2
- Initial configuration for GeoNode 2.4
