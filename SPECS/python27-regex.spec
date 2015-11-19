%define name python27-regex
%define version 2015.07.12
%define realname regex
%define release 1%{?dist}
%define debug_package %{nil}

Summary: Alternative regular expression module, to replace re.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/r/regex/regex-%{version}.tar.gz
License: Python Software Foundation License
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: gcc
BuildRequires: gcc-c++
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Alternative regular expression module, to replace re.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed --in-place '/\.pyc/d' INSTALLED_FILES

%preun
find /usr/local -type f -name '*pyc' -exec rm {} +

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2015.07.12
- Initial configuration for GeoNode 2.4
