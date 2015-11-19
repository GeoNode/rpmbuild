Summary: Geospatial Data Abstraction Library
Name: gdal
Version: 1.11.2
Release: 2%{?dist}
License: MIT/X
Group: Applications/Engineering
URL: http://www.gdal.org/

%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
Source0: http://download.osgeo.org/gdal/%{version}/gdal-%{version}.tar.gz
Packager: Daniel Berry <dberry@boundlessgeo.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc
BuildRequires: geos-devel >= 3.3.3
BuildRequires: proj-devel
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: sqlite-devel
BuildRequires: libkml-devel
BuildRequires: postgresql93-devel
BuildRequires: poppler-devel
BuildRequires: xerces-c-devel
BuildRequires: java-1.6.0-openjdk-devel
BuildRequires: openjpeg2-devel
BuildRequires: python-devel
BuildRequires: ant
BuildRequires: chrpath

Requires: geos >= 3.3.3
Requires: swig
Requires: openjpeg2
Requires: proj
Requires: poppler
Requires: postgresql93-libs >= 9.3.2
Requires: expat
Requires: curl
Requires: sqlite
Requires: xerces-c
Requires: libkml

Patch0: gdal_driverpath.patch
Patch1: gdal_ogr_driverpath.patch
Patch2: gdal_GDALmake.opt.in.patch

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying C/C++ API for
accessing raster geospatial data, and currently includes formats like
GeoTIFF, Erdas Imagine, Arc/Info Binary, CEOS, DTED, GXF, and SDTS. It is
intended to provide efficient access, suitable for use in viewer
applications, and also attempts to preserve coordinate systems and
metadata. Perl, C, and C++ interfaces are available.

# gdal-devel
%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h

%prep
%setup
%ifarch x86_64
# In RedHat land, 32-bit libs go in /usr/lib and 64-bit ones go in /usr/lib64.
# The default driver search paths need changing to reflect this.
%patch0
%patch1
%endif
%patch2

%build

sed -i 's|@LIBTOOL@|%{_bindir}/libtool|g' GDALmake.opt.in

%configure --datadir=/usr/share/gdal --disable-static --with-pg=/usr/pgsql-9.3/bin/pg_config  --disable-rpath --with-python --with-poppler=yes --with-openjpeg --with-sqlite3 --with-curl --with-poppler --with-expat --with-xerces --with-libkml=yes
make
make %{?_smp_mflags}

# Java SWIG bindings
cd swig/java
sed -i '1iJAVA_HOME=/usr/lib/jvm/java-openjdk' java.opt
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%ifarch x86_64 # 32-bit libs go in /usr/lib while 64-bit libs go in /usr/lib64
%define lib_dir /usr/lib64
%else
%define lib_dir /usr/lib
%endif
mkdir -p %{buildroot}%{lib_dir}/gdalplugins
# Remove RPATHs
chrpath -d swig/java/*.so
cp swig/java/*.so %{buildroot}%{lib_dir}
cp swig/java/gdal.jar %{buildroot}%{lib_dir}/gdal-%{version}.jar

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/gdal/
%{_libdir}/lib*
%{_libdir}/gdal-%{version}.jar
%{_libdir}/python*/site-packages/*
%{_libdir}/pkgconfig/gdal.pc
