%define name python27-nose
%define version 1.0.0
%define realname nose
%define release 1%{?dist}

Summary: nose extends unittest to make testing easier.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/n/nose/nose-%{version}.tar.gz
License: GNU Library or Lesser General Public License (LGPL)
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
nose extends unittest to make testing easier.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.0.0
- Initial configuration for GeoNode 2.4
