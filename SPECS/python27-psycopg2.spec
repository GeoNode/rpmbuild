%define name python27-psycopg2
%define version 2.6.1
%define realname psycopg2
%define release 1%{?dist}
%define debug_package %{nil}

Summary: psycopg2 - Python-PostgreSQL Database Adapter
Name: %{name}
Version: %{version}
Release: %{release}
Source: wget https://pypi.python.org/packages/source/p/psycopg2/psycopg2-%{version}.tar.gz
License: GNU Library or Lesser General Public License (LGPL)
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: postgresql93-devel
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
export PATH=/usr/pgsql-9.3/bin:$PATH
python2.7 setup.py build

%install
export PATH=/usr/pgsql-9.3/bin:$PATH
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/\.pyc/d' INSTALLED_FILES

%preun
find /usr/local -type f -name '*pyc' -exec rm {} +

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.6.1
- Initial configuration for GeoNode 2.4
