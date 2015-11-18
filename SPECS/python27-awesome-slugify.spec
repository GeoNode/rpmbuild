%define name python27-awesome-slugify
%define version 1.6.2
%define realname awesome-slugify
%define release 1%{?dist}

Summary: Python flexible slugify function
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/a/awesome-slugify/awesome-slugify-%{version}.tar.gz
License: GNU GPLv3
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Python flexible slugify function.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.6.2
- Initial configuration for GeoNode 2.4
