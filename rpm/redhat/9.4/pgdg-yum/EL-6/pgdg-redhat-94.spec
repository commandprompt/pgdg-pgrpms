Name:		pgdg-redhat94
Version:	9.4
Release:	2
Summary:	PostgreSQL 9.4.X PGDG RPMs for RHEL - Yum Repository Configuration
Group:		System Environment/Base
License:	BSD
URL:		http://yum.postgresql.org
Source0:	http://yum.postgresql.org/RPM-GPG-KEY-PGDG-94
Source2:	pgdg-94-redhat.repo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	redhat-release

%description
This package contains yum configuration for RHEL, and also the GPG
key for PGDG RPMs.

%prep
%setup -q  -c -T

%build

%install
rm -rf %{buildroot}

install -Dpm 644 %{SOURCE0} \
	%{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-PGDG-94

install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2}  \
	%{buildroot}%{_sysconfdir}/yum.repos.d/

%clean
rm -rf %{buildroot}

%post
/bin/rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-PGDG-94

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/*
%dir %{_sysconfdir}/pki/rpm-gpg
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Oct 21 2015 Devrim Gündüz <devrim@gunduz.org> - 9.4-2
- Point the download URL in repo file to new location.

* Thu May 8 2014 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.4-1
- 9.4 set

* Sun Apr 21 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.3-1
- 9.3 set

* Sun Sep 23 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-7
- Fix name of the GPG key file, per report from Rafael Martinez.

* Sat May 19 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-6
- Fix repo name.

* Fri Sep 23 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-4
- Change the package name, and add PostgreSQL major version number.
  This will let us install the repo RPMs easier. Also, rename RPM key,
  so that --import won't throw any errors.
- Own %%{_sysconfdir}/pki/rpm-gpg
- Trim changelog

* Mon Aug 22 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-3
- Now use http://yum.postgresql.org as the new repo URL.

* Mon Jan 10 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-2
- Use full path for rpm command. Noted while testing 9.0 live CD.

* Thu Sep 9 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 9.2-1
- 9.2 set
