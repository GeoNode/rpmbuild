%define name python27-django-mptt
%define version 0.6.1
%define realname django-mptt
%define release 1%{?dist}

Summary: Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-mptt/django-mptt-%{version}.tar.gz
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.6.1
- Initial configuration for GeoNode 2.4
