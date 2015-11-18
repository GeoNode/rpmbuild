%define name python27-uwsgi
%define version 2.0.11.1
%define realname uwsgi
%define release 1%{?dist}

Summary: The uWSGI server
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/u/uWSGI/uwsgi-%{version}.tar.gz
License: GPL2
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
The uWSGI server

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.0.11.1
- Initial configuration for GeoNode 2.4
