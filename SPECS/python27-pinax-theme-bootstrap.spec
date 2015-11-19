%define name python27-pinax-theme-bootstrap
%define version 3.0a11
%define realname pinax-theme-bootstrap
%define release 1%{?dist}

Summary: a theme for Pinax based on Bootstrap
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/p/pinax-theme-bootstrap/pinax-theme-bootstrap-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.0a11
- Initial configuration for GeoNode 2.4
