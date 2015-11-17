%define name python27-paver
%define version 1.2.1
%define realname Paver
%define release 1%{?dist}

Summary: Easy build, distribution and deployment scripting
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/P/Paver/Paver-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Paver is a Python-based build/distribution/deployment scripting tool along the lines of Make or Rake. What makes Paver unique is its integration with commonly used Python libraries. Common tasks that were easy before remain easy. More importantly, dealing with your applications specific needs and requirements is also easy.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.2.1
- Initial configuration for GeoNode 2.4
