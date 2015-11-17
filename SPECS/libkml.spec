Summary:	A KML library written in C++ with bindings
Name:		libkml
Version:	1.2.0
Release:	1%{?dist}
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}-svn-28-aug-2015.tar.gz
Packager:       Daniel Berry <dberry@boundlessgeo.com>
URL:	        https://code.google.com/p/libkml/	
BuildRequires:	swig >= 1.3.35
BuildRequires:	cppunit
BuildRequires:	expat-devel
BuildRequires:	zlib-devel
BuildRequires:	libcurl-devel
BuildRequires:	expat-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libgcj-devel
Requires:	expat, zlib, minizip

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}

%description
Libkml is an implementation of the OGC KML 2.2 standard. is written in C++ and 
it can be used in applications that want to parse, generate and operate on KML.

%package devel
Summary:	Header file for LIBKML library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the LIBKML library.

%prep
%setup -q -n %{name}

%build
autoreconf -fi
%configure --disable-static --disable-java --disable-python \
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
cd examples; make clean; cd ..
find examples -type f -print | xargs chmod a-x

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%doc AUTHORS
%doc README
%doc ChangeLog
%{_libdir}/*.so*

%files devel
%defattr(-,root,root,-)
%doc examples
%{_includedir}/*
