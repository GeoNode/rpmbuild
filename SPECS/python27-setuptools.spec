%define name python27-setuptools
%define version 18.0.1
%define realname setuptools
%define release 1%{?dist}

Summary: Easily download, build, install, upgrade, and uninstall Python packages
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
License: PSF or ZPL
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Easily download, build, install, upgrade, and uninstall Python packages.

%define _unpackaged_files_terminate_build 0

%prep

%setup -n setuptools-%{version}

%build
if [ -f 'setuptools/script (dev).tmpl' ]; then
  mv 'setuptools/script (dev).tmpl' 'setuptools/script(dev).tmpl'
fi
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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 18.0.1
- Initial configuration for GeoNode 2.4
