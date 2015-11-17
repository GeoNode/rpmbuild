%define name python27-multipartposthandler
%define version 0.1.0
%define realname MultipartPostHandler
%define release 1%{?dist}

Summary: A handler for urllib2 to enable multipart form uploading.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/M/MultipartPostHandler/MultipartPostHandler-%{version}.tar.gz
License: GNU Library or Lesser General Public License (LGPL)
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
A handler for urllib2 to enable multipart form uploading.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.1.0
- Initial configuration for GeoNode 2.4
