%global pgmajorversion 95
%global pginstdir /usr/pgsql-9.5
%global sname pgespresso

Summary:	Optional Extension for Barman
Name:		%{sname}%{pgmajorversion}
Version:	1.0.0
Release:	2%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	http://api.pgxn.org/dist/%{sname}/%{version}/%{sname}-%{version}.zip
Patch0:		Makefile-pgxs.patch
URL:		http://pgxn.org/dist/pgespresso/
BuildRequires:	postgresql%{pgmajorversion}-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

pgespresso is an extension that adds functions and views to be used by Barman,
the disaster recovery tool written by 2ndQuadrant and released as open source 
(http://www.pgbarman.org/). Requires at least Barman 1.3.1 and PostgreSQL 9.2.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
make USE_PGXS=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}

make USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}

# Install README file under PostgreSQL installation directory:
install -d %{buildroot}%{pginstdir}/share/extension
install -m 755 README.asciidoc  %{buildroot}%{pginstdir}/share/extension/README-%{sname}.asciidoc

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{pginstdir}/share/extension/README-%{sname}.asciidoc 
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}*.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Tue Apr 29 2014 - Devrim GUNDUZ <devrim@gunduz.org> 1.0.0-2
- Remove barman dependency

* Mon Apr 14 2014 - Devrim GUNDUZ <devrim@gunduz.org> 1.0.0-1
- Initial RPM packaging for PostgreSQL RPM Repository
