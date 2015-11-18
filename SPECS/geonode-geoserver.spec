# Define Constants
%define name geonode-geoserver
%define realname geoserver
%define version 2.7.5
%define release 0.1%{?dist}
%define _unpackaged_files_terminate_build 0
%define __os_install_post %{nil}

Name:          %{name}
Version:       %{version}
Release:       %{release}
Summary:       A version of GeoServer that is enhanced and designed for use with GeoNode %{version}.
Group:         Development/Libraries
BuildRequires: unzip
Requires:      %{name} = %{version}-%{release}
Requires:      tomcat
Requires:      java-1.7.0-openjdk
Conflicts:     geoserver
Patch0:        geoshape.web.xml.patch
Patch1:        geoshape.context.xml.patch
BuildArch:     noarch

%description
GeoServer is built with the geoserver-geonode-ext, which extends GeoServer
with certain JSON, REST, and security capabilites specifically for GeoNode.

%prep
unzip $RPM_SOURCE_DIR/geoserver.war -d $RPM_SOURCE_DIR/geoserver
pushd $RPM_SOURCE_DIR/geoserver

%patch0 -p1
%patch1 -p1

popd

%build

%install
CX_ROOT=$RPM_BUILD_ROOT%{_sysconfdir}/tomcat/Catalina/localhost
WEBAPPS=$RPM_BUILD_ROOT%{_localstatedir}/lib/tomcat/webapps
GS=$RPM_SOURCE_DIR/geoserver
DATA=$RPM_BUILD_ROOT%{_localstatedir}/lib/geoserver
WAR_DATA=$RPM_BUILD_ROOT%{_localstatedir}/lib/tomcat/webapps/geoserver/data
CX=$RPM_SOURCE_DIR/geoserver/WEB-INF/classes/org/geonode/security/geoserver.xml
SQL=$RPM_SOURCE_DIR/geoserver/WEB-INF/classes/org/geonode/security/geonode_authorize_layer.sql
mkdir -p $CX_ROOT $WEBAPPS
cp -rp $CX $CX_ROOT
cp -rp $GS $WEBAPPS
if [ ! -d $DATA ]; then
  mkdir -p $DATA
  cp -R $WAR_DATA/* $DATA
fi
cp -rp $SQL $DATA

%pre

%post
if [ $1 -eq 1 ] ; then
  # add Java specific options
  echo '# Next line added for geonode service' >> %{_sysconfdir}/tomcat/tomcat.conf
  echo 'JAVA_OPTS="-Xmx1024m -XX:MaxPermSize=256m"' >> %{_sysconfdir}/tomcat/tomcat.conf
fi

%preun
if [ $1 -eq 0 ] ; then
  /sbin/service tomcat stop > /dev/null 2>&1
  rm -fr %{_localstatedir}/lib/tomcat/webapps/geoserver
  rm -f %{_sysconfdir}/tomcat/Catalina/localhost/geoserver.xml
  echo ""
  echo ""
  echo "  -------------------------------"
  echo "           Important!!!          "
  echo "                                 "
  echo "     Uninstall does not delete   "
  echo "   files from /var/lib/geoserver "
  echo "  -------------------------------"
  echo ""
  echo ""
fi

%postun
if [ $1 -eq 1 ] ; then
  /sbin/service tomcat condrestart >/dev/null 2>&1
fi

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}
[ -d $RPM_SOURCE_DIR/geoserver ] && rm -rf $RPM_SOURCE_DIR/geoserver

%files
%defattr(-,root,root,-)
%attr(-,tomcat,tomcat) %{_localstatedir}/lib/tomcat/webapps/geoserver
%attr(-,tomcat,tomcat) %{_localstatedir}/lib/geoserver
%dir %{_sysconfdir}/tomcat/Catalina/localhost
%attr(-,tomcat,tomcat) %{_sysconfdir}/tomcat/Catalina/localhost/geoserver.xml

%changelog
* Sun Nov 8 2015 Daniel Berry <dberry@boundlessgeo.com> 2.7.5
- Initial configuration for GeoNode 2.4
