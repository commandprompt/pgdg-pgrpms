%global pgmajorversion 90
%global pginstdir /usr/pgsql-9.0
%global sname pgsphere

Summary:	R-Tree implementation using GiST for spherical objects
Name:           %{sname}%{pgmajorversion}
Version:	1.1.1
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	http://pgfoundry.org/frs/download.php/2558/%{sname}-%{version}.tar.gz
URL:		http://pgfoundry.org/projects/pgsphere
BuildRequires:	postgresql%{pgmajorversion}-devel
Requires:	postgresql%{pgmajorversion}-server
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
pgSphere is a server side module for PostgreSQL. It contains methods for 
working with spherical coordinates and objects. It also supports indexing of 
spherical objects.

%prep
%setup -q -n %{sname}-%{version}

%build
make PG_CONFIG=%{pginstdir}/bin/pg_config USE_PGXS=1 %{?_smp_mflags} 

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/pgsql/
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_docdir}/%{name}-%{version}

install -m 755 pg_sphere.so %{buildroot}%{_libdir}/pgsql/pg_sphere.so
install -m 644 pg_sphere.sql %{buildroot}%{_datadir}/%{name}/
install -m 644 README.pg_sphere %{buildroot}%{_docdir}/%{name}-%{version}/

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig 

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/README.pg_sphere
%{_datadir}/%{name}/*.sql
%{_libdir}/pgsql/pg_sphere.so

%changelog
* Wed Jan 5 2011 - Devrim GUNDUZ <devrim@gunduz.org> 1.1.1-1
- Update to 1.1.1, per: 
  http://pgfoundry.org/forum/forum.php?forum_id=1665
- Apply 9.0 specific changes

* Tue Jul 28 2009 - Devrim GUNDUZ <devrim@gunduz.org> 1.1.0-1
- Update to 1.1.0

* Wed Aug 20 2008 - Devrim GUNDUZ <devrim@gunduz.org> 1.0.1-1
- Update to 1.0.1

* Wed Apr 9 2008 - Devrim GUNDUZ <devrim@gunduz.org> 1.0.0-1
- Initial RPM packaging for Fedora
