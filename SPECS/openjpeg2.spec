Summary:  An open-source JPEG 2000 codec
Name:   openjpeg2
Version:  2.1.0
Release:  2%{?dist}
License:  BSD
Group:    Libraries
Source0:  http://downloads.sourceforge.net/openjpeg.mirror/openjpeg-%{version}.tar.gz
Patch0:   %{name}-headers.patch
Packager:       Daniel Berry <dberry@boundlessgeo.com>
URL:    http://www.openjpeg.org/
BuildRequires:  cmake >= 2.8.2
BuildRequires:  doxygen
BuildRequires:  lcms2-devel >= 2
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig >= 1:0.22
BuildRequires:  zlib-devel
BuildRoot:  %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}

%description
The OpenJPEG 2 library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%package devel
Summary:  Header file for OpenJPEG 2 library
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the OpenJPEG 2 library.

%prep
%setup -q -n openjpeg-%{version}
%patch0 -p1

%build
%cmake . \
  -DBUILD_DOC=ON \
  -DOPENJPEG_INSTALL_LIB_DIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
  DESTDIR=$RPM_BUILD_ROOT

# packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/openjpeg-2.1
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE NEWS README THANKS
%attr(755,root,root) %{_libdir}/libopenjp2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenjp2.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjp2.so
%{_includedir}/openjpeg-2.1
%dir %{_libdir}/openjpeg-2.1
%{_libdir}/openjpeg-2.1/OpenJPEG*.cmake
%{_libdir}/pkgconfig/libopenjp2.pc
%{_mandir}/man3/libopenjp2.3*
