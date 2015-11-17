%define name python27-mccabe
%define version 0.3.1
%define realname mccabe
%define release 1%{?dist}

Summary: McCabe checker, plugin for flake8.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
McCabe checker, plugin for flake8.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.3.1
- Initial configuration for GeoNode 2.4
