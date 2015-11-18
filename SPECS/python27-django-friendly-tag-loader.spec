%define name python27-django-friendly-tag-loader
%define version 1.1
%define realname django-friendly-tag-loader
%define release 1%{?dist}

Summary: Use templatetag libraries in Django templates to optionally support features.
Name: %{name}
Version: %{version}
Release: %{release}
Source: https://pypi.python.org/packages/source/d/django-friendly-tag-loader/django-friendly-tag-loader-%{version}.zip
License: MIT
Group: Development/Libraries
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRequires: python27
Requires: python27
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
This app provides three template tags {% friendly_load %}, {% if_has_tag %} and {% ifnot_has_tag %}. Used together you can built templates that have optional support for certain template tags. You can use them if they are available and do something else if they are not.

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
* Tue Nov 17 2015 Daniel Berry <dberry@boundlessgeo.com> 1.1
- Initial configuration for GeoNode 2.4
