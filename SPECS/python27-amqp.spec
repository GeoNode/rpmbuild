%define name python27-amqp
%define version 1.4.6
%define realname amqp
%define release 1%{?dist}

Summary: Low-level AMQP client for Python (fork of amqplib)
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/a/amqp/amqp-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
This is a fork of amqplib which was originally written by Barry Pederson. It is maintained by the Celery project, and used by kombu as a pure python alternative when librabbitmq is not available.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.4.6
- Initial configuration for GeoNode 2.4
