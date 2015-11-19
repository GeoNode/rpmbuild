%define name python27-django-activity-stream
%define version 0.4.5beta1
%define realname django-activity-stream
%define release 1%{?dist}

Summary: Generate generic activity streams from the actions on your site. Users can follow any actor's activities for personalized streams.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-activity-stream/django-activity-stream-%{version}.tar.gz

License: BSD
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Generate generic activity streams from the actions on your site. Users can follow any actor's activities for personalized streams.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 0.4.5.beta1
- Initial configuration for GeoNode 2.4
