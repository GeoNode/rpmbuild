%define name python27-django
%define version 1.6.11
%define realname Django
%define release 1%{?dist}

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/D/Django/Django-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
A high-level Python Web framework that encourages rapid development and clean, pragmatic design.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.6.11
- Initial configuration for GeoNode 2.4
