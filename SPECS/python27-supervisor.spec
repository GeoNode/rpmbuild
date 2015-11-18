%define name python27-supervisor
%define version 3.1.3
%define realname supervisor
%define release 1%{?dist}

Summary: A system for controlling process state under UNIX
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/s/supervisor/supervisor-%{version}.tar.gz
License: BSD-derived (http://www.repoze.org/LICENSE.txt)
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
A system for controlling process state under UNIX

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.1.3
- Initial configuration for GeoNode 2.4
