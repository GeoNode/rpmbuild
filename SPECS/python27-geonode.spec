%define name python27-geonode
%define version 2.4
%define realname GeoNode
%define release 1%{?dist}

Summary: Application for serving and sharing geospatial data
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/G/GeoNode/GeoNode-%{version}.tar.gz
License: GPL
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Application for serving and sharing geospatial data

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/.pyc/d' INSTALLED_FILES

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Nov 19 2015 Daniel Berry <dberry@boundlessgeo.com> 2.4
- Update version to 2.4 Final

* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.4c2
- Initial configuration for GeoNode 2.4
