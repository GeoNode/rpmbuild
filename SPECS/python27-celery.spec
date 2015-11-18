%define name python27-celery
%define version 3.1.17
%define realname celery
%define release 1%{?dist}

Summary: Distributed Task Queue
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/c/celery/celery-%{version}.tar.gz
License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
Task queues are used as a mechanism to distribute work across threads or machines. A task queue’s input is a unit of work, called a task, dedicated worker processes then constantly monitor the queue for new work to perform.Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker. A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 3.1.17
- Initial configuration for GeoNode 2.4
