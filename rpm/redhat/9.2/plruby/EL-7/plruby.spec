%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

Summary:	PostgreSQL Ruby Procedural Language
Name:		plruby
Version:	0.5.3
Release:	1%{?dist}
Source0:	ftp://moulon.inra.fr/pub/ruby/%{name}-%{version}.tar.gz
License:	Ruby or GPL+
Group:		Applications/Databases
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url:		http://raa.ruby-lang.org/project/pl-ruby/
BuildRequires:	ruby >= 1.8 ruby-devel >= 1.8 postgresql-devel >= 8.1
Requires:	postgresql-libs, ruby(abi) = 1.8

%description
PL/Ruby is a loadable procedural language for the PostgreSQL database
system that enable the Ruby language to create functions and trigger 
procedures.

%package doc
Summary:	Documentation for plruby
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for plruby.

%prep
%setup -q -n %{name}-%{version}

unset FILE
for f in %{_includedir}/pg_config_*.h
	do
	if grep -q PG_VERSION $f
		then
		FILE=`basename $f`
	fi
done
if [ -n $FILE ]
	then
	%{__sed} -i.pgver -e "s|pg_config.h|${FILE}|" extconf.rb
fi

%build
ruby extconf.rb --with-pgsql-include=%{_includedir}/pgsql/server
CC="%{__cc} -I%{_includedir}/pgsql -I%{_includedir}/pgsql/server" make DESTDIR=%{buildroot} %{?_smp_mflags} install

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README.en plruby.html 
%dir %{ruby_sitearch}/plruby
%{ruby_sitearch}/plruby/plruby_*.so
%{ruby_sitearch}/plruby.so

%files doc
%defattr(-,root,root,-)
%doc docs/plruby.rb

%changelog
* Mon Mar 3 2008 Devrim GUNDUZ <devrim@gunduz.org> - 0.5.3-1
- Update to 0.5.3 to fix PostgreSQL 8.3 + GCC 4.3 problems. 0.5.2 had
  a problem with PostgreSQL version detection, so author kindly released
  0.5.3 for this issue.
- Sync with Fedora spec.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.1-6.1
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.1-5.1
- Rebuilt against PostgreSQL 8.3

* Mon Jan 14 2008 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.1-5
- Use a better BR line for postgresql-devel

* Sat Nov 30 2007 - Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.1-4
- Make spec file actually compile
- Fix license tag

* Sat Oct 15 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.1-3
- More fixes to spec file per bz review #246793

* Sat Oct 6 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.1-2
- Updates to spec file per bz review #246793

* Fri Oct 5 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.1-1
- Update to 0.5.1

* Tue Jul 17 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.0-2
- Minor fixes to spec file.

* Wed Jul 4 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.5.0-1
- Update to 0.5.0

* Sat Jun 16 2007 - Devrim GUNDUZ <devrim@gunduz.org> 0.4.8-1
- Initial packaging for Fedora
