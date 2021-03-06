#Python major version.
%{expand: %%global pybasever %(python -c 'import sys;print(sys.version[0:3])')}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:	Top like application for PostgreSQL server activity monitoring
Name:		pg_activity
Version:	1.2.0
Release:	1%{?dist}
License:	GPLv3
Group:		Applications/Databases
Url:		https://github.com/julmon/pg_activity/
Source0:	https://github.com/julmon/%{name}/archive/v%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	python > 2.6, python-psutil > 0.4.1, python-psycopg2 >= 2.2.1
BuildRequires:	python-setuptools >= 0.6.14

%description
top like application for PostgreSQL server activity monitoring.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --with-man -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{python_sitelib}/%{name}-%{version}-py%{pybasever}.egg-info/
%{_mandir}/man1/%{name}.1.gz
%{python_sitelib}/%{name}-%{version}-py%{pybasever}.egg-info/*
%{python_sitelib}/pgactivity/*.py*

%changelog
* Wed Feb 4 2015 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.2.0-1
- Update to 1.2.0
- Remove patch0
- Fix rpmlint warnings in spec file.

* Thu Feb 27 2014 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.1.1-1
- Update to 1.1.1

* Sat Dec 28 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.1.0-1
- Update to 1.1.0
- Fix packaging issues
- Update description and summary

* Thu Dec 20 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 0.2.0-1
- Initial packaging, based on the spec by Marco Neciarini
