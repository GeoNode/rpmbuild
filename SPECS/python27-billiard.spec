%define name python27-billiard
%define version 3.3.0.20
%define realname billiard
%define release 1%{?dist}

Summary: Python multiprocessing fork with improvements and bugfixes
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/b/billiard/billiard-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
billiard is a fork of the Python 2.7 multiprocessing package. The multiprocessing package itself is a renamed and updated version of R Oudkerk’s pyprocessing package.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.3.0.20
- Initial configuration for GeoNode 2.4
