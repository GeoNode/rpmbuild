%define name python27-gsconfig
%define version 1.0.3
%define realname gsconfig
%define release 1%{?dist}

Summary: GeoServer REST Configuration
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/g/gsconfig/gsconfig-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
gsconfig is a python library for manipulating a GeoServer instance via the GeoServer RESTConfig API.

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
* Thu Nov 19 2015 Daniel Berry <dberry@boundlessgeo.com> 1.0.3
- Update version to 1.0.3

* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.0.0
- Initial configuration for GeoNode 2.4
