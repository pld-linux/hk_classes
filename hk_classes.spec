# TODO:	- fix 64bit builds
#       - review commented out patches 3 & 4 and update or remove them
#       - make python build *.pyo also and include it instead of *.py
#	- patch3 should be rewritten to search for .pyc and .py not only .pyc and sent back
#  
# Conditional build:
%bcond_without	firebird
%bcond_with	mdb
%bcond_without	mysql
%bcond_without	odbc	
%bcond_without	pgsql
%bcond_without	paradox
%bcond_without	sqlite2
%bcond_without	sqlite3
%bcond_without	xbase
%bcond_without	static_libs # don't build static library
#
Summary:	Non-visual routines for database frontend applications
Summary(pl.UTF-8):	Niegraficzne funkcje dla aplikacji będących frontendami do baz danych
Name:		hk_classes
Version:	0.8.3
Release:	0.5
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/hk-classes/%{name}-%{version}.tar.gz
# Source0-md5:	030ce063fc78a15e351429867d2a6bde
# Patch0:		%{name}-dir.patch
Patch2:		%{name}-iconv-in-libc.patch
URL:		http://hk-classes.sourceforge.net/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.7.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6}
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.1}
%{?with_pgsql:BuildRequires:	postgresql-devel >= 7.1}
%{?with_paradox:BuildRequires:	pxlib-devel}
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%{?with_sqlite2:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xbase:BuildRequires:	xbsql-devel}
Conflicts:	knoda < 0.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hk_classes is a set of non-visual routines which allow you to develop
database frontend applications as easy as possible.

%description -l pl.UTF-8
hk_classes to zbiór niegraficznych funkcji, pozwalających na możliwie
najłatwiejsze tworzenie aplikacji będących frontendami do baz danych.

%package devel
Summary:	Header files for hk_classes
Summary(pl.UTF-8):	Pliki nagłówkowe hk_classes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for hk_classes.

%description devel -l pl.UTF-8
Pliki nagłówkowe hk_classes.

%package static
Summary:	Static hk_classes library
Summary(pl.UTF-8):	Statyczna biblioteka hk_classes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hk_classes library.

%description static -l pl.UTF-8
Statyczna biblioteka hk_classes.

%package driver-firebird
Summary:	Firebird driver for hk_classes
Summary(pl.UTF-8):	Sterownik Firebird dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-firebird
Firebird driver for hk_classes.

%description driver-firebird -l pl.UTF-8
Sterownik Firebird dla hk_classes.

%package driver-mysql
Summary:	MySQL driver for hk_classes
Summary(pl.UTF-8):	Sterownik MySQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-mysql
MySQL driver for hk_classes.

%description driver-mysql -l pl.UTF-8
Sterownik MySQL dla hk_classes.

%package driver-mdb
Summary:	mdb driver for hk_classes
Summary(pl.UTF-8):	Sterownik mdb dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-mdb
mdb driver for hk_classes.

%description driver-mdb -l pl.UTF-8
Sterownik mdb dla hk_classes.

%package driver-odbc
Summary:	unixODBC driver for hk_classes
Summary(pl.UTF-8):	Sterownik unixODBC dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-odbc
unixODBC driver for hk_classes.

%description driver-odbc -l pl.UTF-8
Sterownik unixODBC dla hk_classes.

%package driver-paradox
Summary:	paradox driver for hk_classes
Summary(pl.UTF-8):	Sterownik paradox dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-paradox
paradox driver for hk_classes.

%description driver-paradox -l pl.UTF-8
Sterownik paradox dla hk_classes.

%package driver-postgresql
Summary:	PostgreSQL driver for hk_classes
Summary(pl.UTF-8):	Sterownik PostgreSQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-postgresql
PostgreSQL driver for hk_classes.

%description driver-postgresql -l pl.UTF-8
Sterownik PostgreSQL dla hk_classes.

%package driver-sqlite2
Summary:	SQLite v2 driver for hk_classes
Summary(pl.UTF-8):	Sterownik SQLite v2 dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-sqlite2
SQLite version 2.x driver for hk_classes.

%description driver-sqlite2 -l pl.UTF-8
Sterownik SQLite w wersji 2.x dla hk_classes.

%package driver-sqlite3
Summary:	SQLite v3 driver for hk_classes
Summary(pl.UTF-8):	Sterownik SQLite v3 dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-sqlite3
SQLite version 3.x driver for hk_classes.

%description driver-sqlite3 -l pl.UTF-8
Sterownik SQLite w wersji 3.x dla hk_classes.

%package driver-xbase
Summary:	xbase driver for hk_classes
Summary(pl.UTF-8):	Sterownik xbase dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-xbase
xbase driver for hk_classes.

%description driver-xbase -l pl.UTF-8
Sterownik xbase dla hk_classes.

%package -n python-%{name}
Summary:	Python interface to %{name}
Summary(pl.UTF-8):	Interfejs do %{name} dla jezyka Python
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq python-libs

%description -n python-%{name}
Python inteface to hk_classes.

%description -n python-%{name} -l pl.UTF-8
Pythonowy interfejs do klass hk_classes.

%package tools
Summary:	Commandline tools
Summary(pl.UTF-8):	Narzędzia działające z linii poleceń
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Command line tools for hk_classes.

%description tools -l pl.UTF-8
Narzędzia działające z linii poleceń dla hk_classes.

%package apidocs
Summary:	API documentation for hk_classes
Summary(pl.UTF-8):	Dokumentacja API dla hk_classes
Group:		Documentation

%description apidocs
API documentation for hk_classes.

%description apidocs -l pl.UTF-8
Dokumentacja API dla hk_classes.

%prep
%setup -q
%patch2 -p1

%build
# supplied libtool is broken (C++)
%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}

%configure \
	--with-hk_classes-dir=%{_libdir} \
	--with-hk_classes-incdir=%{_includedir}/%{name} \
	--with-hk_classes-drvdir=%{_libdir}/%{name}/drivers \
	--with%{!?with_firebird:out}-firebird \
	--with%{!?with_mdb:out}-mdb \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_odbc:out}-odbc \
	--with%{!?with_paradox:out}-paradox \
	--with%{!?with_pgsql:out}-postgres \
	--with%{!?with_sqlite2:out}-sqlite \
	--with%{!?with_sqlite3:out}-sqlite3 \
	--with%{!?with_xbase:out}-xbase \
	%{?with_static_libs:--enable-static=yes}
%{__make}
cd python
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Dirty hack to move libs back to /usr/lib
# If you feel not confortable with that please update %{name}-dir.patch 
# and make maintainer accept them
mv -v $RPM_BUILD_ROOT/%{_libdir}/%{name}/libhk_classes.* $RPM_BUILD_ROOT/%{_libdir}/

# drivers ware dlopened by *.so in 0.8 but in 0.8.3  .la is needed to access drivers
# rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/drivers/lib*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/drivers/lib*.a

cp -a documentation apidocs
# remove Makefiles from docs for %%files apidocs simplification
rm -f apidocs/{api,tutorial}/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig 
%postun	-p /sbin/ldconfig 

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/drivers

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with firebird}
%files driver-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_firebirddriver.so*
%attr(644,root,root) %{_libdir}/%{name}/drivers/libhk_firebirddriver.la
%endif

%if %{with mdb}
%files driver-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mdbdriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mdbdriver.la
%endif

%if %{with mysql}
%files driver-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mysqldriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mysqldriver.la
%endif

%if %{with odbc}
%files driver-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_odbcdriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_odbcdriver.la
%endif

%if %{with paradox}
%files driver-paradox
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_paradoxdriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_paradoxdriver.la
%endif

%if %{with pgsql}
%files driver-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_postgresdriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_postgresdriver.la
%endif

%if %{with sqlite2}
%files driver-sqlite2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite2driver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite2driver.la
%endif

%if %{with sqlite3}
%files driver-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite3driver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite3driver.la
%endif

%if %{with xbase}
%files driver-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_xbasedriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_xbasedriver.la
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_dbasedriver.so*
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_dbasedriver.la
%endif

%files -n python-%{name}
%defattr(644,root,root,755)
#%%{py_sitedir}/hk_classes.py[co]
%{py_sitedir}/hk_classes.py*
%attr(755,root,root) %{py_sitedir}/_hk_classes.so

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hk_*
%{_mandir}/man?/*

%files apidocs
%defattr(644,root,root,755)
#%%doc apidocs/api apidocs/tutorial
%doc apidocs/tutorial
