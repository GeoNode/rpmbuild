%define name python27-anyjson
%define version 0.3.3
%define realname anyjson
%define release 1%{?dist}

Summary: Wraps the best available JSON implementation available in a common interface
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/a/anyjson/anyjson-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Anyjson loads whichever is the fastest JSON module installed and provides a uniform API regardless of which JSON implementation is used.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.3.3
- Initial configuration for GeoNode 2.4
