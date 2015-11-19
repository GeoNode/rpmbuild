%define name python27-lxml
%define version 3.4.4
%define realname lxml
%define release 1%{?dist}
%define debug_package %{nil}

Summary: MPowerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/l/lxml/lxml-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: libxslt-devel
BuildRequires: libxml2-devel
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
Requires: libxslt
Requires: libxml2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.4.4
- Initial configuration for GeoNode 2.4
