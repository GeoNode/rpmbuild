%define name python27-gisdata
%define version 0.5.4
%define realname gisdata
%define release 1%{?dist}

Summary: Sample data and metadata for GIS packages.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/g/gisdata/gisdata-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Sample data and metadata for GIS packages.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n %{realname}-%{version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --prefix=/usr/local --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# needed for files with spaces in the name
sed -i.bak 's/^..*$/"&"/' INSTALLED_FILES

%clean
rm -fr $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.5.4
- Initial configuration for GeoNode 2.4
