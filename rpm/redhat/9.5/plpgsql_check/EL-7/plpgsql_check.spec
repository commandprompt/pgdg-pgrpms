%global pgmajorversion 95
%global pginstdir /usr/pgsql-9.5
%global sname plpgsql_check

Name:		%{sname}_%{pgmajorversion}
Version:	1.0.2
Release:	1%{?dist}
Summary:	Additional tools for PL/pgSQL functions validation

Group:		Applications/Databases
License:	BSD
URL:		https://github.com/okbob/%{sname}
Source0:	https://github.com/okbob/%{sname}/archive/v%{version}.tar.gz
Patch0:		%{sname}-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	postgresql%{pgmajorversion}-devel
Requires:	postgresql%{pgmajorversion}

%description
The plpgsql_check is PostgreSQL extension with functionality for direct
or indirect extra validation of functions in PL/pgSQL language. It verifies
a validity of SQL identifiers used in PL/pgSQL code. It also tries to identify
performance issues.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
USE_PGXS=1 make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make USE_PGXS=1 DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README.md
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}--1.0.sql
%{pginstdir}/share/extension/%{sname}.control


%changelog
* Mon Jul 13 2015 - Devrim Gündüz <devrim@gunduz.org> 1.0.2-1
- Update to 1.0.2

* Tue Jan 20 2015 - Devrim Gündüz <devrim@gunduz.org> 0.9.3-1
- Update to 0.9.3

* Mon Aug 25 2014 - Pavel STEHULE <pavel.stehule@gmail.com> 0.9.2-1
- Initial packaging
