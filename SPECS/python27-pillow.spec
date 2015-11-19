%define name python27-pillow
%define version 2.9.0
%define realname Pillow
%define release 1%{?dist}
%define debug_package %{nil}

Summary: Python Imaging Library (Fork)
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/P/Pillow/Pillow-%{version}.tar.gz
License: Standard PIL License
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
BuildRequires: libjpeg-devel
Requires: python27
Requires: libjpeg
Requires:         liblcms2-2
Requires:         libopenjp2-7
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Python Imaging Library (Fork).

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 2.9.0
- Initial configuration for GeoNode 2.4
