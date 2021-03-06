%global pgmajorversion 95
%global pginstdir /usr/pgsql-9.5
%global sname pg_stat_kcache

Summary:	A PostgreSQL extension gathering CPU and disk acess statistics
Name:		%{sname}%{pgmajorversion}
Version:	2.0.2
Release:	1%{?dist}
License:	PostgreSQL
Group:		Applications/Databases
Source0:	http://api.pgxn.org/dist/%{sname}/%{version}/%{sname}-%{version}.zip
Patch0:		%{sname}-makefile-pgxs.patch
URL:		http://pgxn.org/dist/pg_stat_kcache/
BuildRequires:	postgresql%{pgmajorversion}-devel
Requires:	postgresql%{pgmajorversion}-server
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Gathers statistics about real reads and writes done by the filesystem layer.
It is provided in the form of an extension for PostgreSQL >= 9.4., and
requires pg_stat_statements extension to be installed. PostgreSQL 9.4 or more
is required as previous version of provided pg_stat_statements didn't expose
the queryid field.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
make USE_PGXS=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

make USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}

# Avoid conflict with some other README files:
%{__mv} %{buildroot}%{pginstdir}/doc/extension/README.rst %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.rst


%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{pginstdir}/doc/extension/README-%{sname}.rst
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}--%{version}.sql
%{pginstdir}/share/extension/%{sname}--2.0.1--2.0.2.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Fri Mar 27 2015 - Devrim Gündüz <devrim@gunduz.org> 2.0.2-1
- Update to 2.0.2

* Tue Mar 17 2015 - Devrim Gündüz <devrim@gunduz.org> 2.0.1-1
- Initial RPM packaging for PostgreSQL RPM Repository
