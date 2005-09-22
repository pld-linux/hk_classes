# TODO: Make python build *.pyo also and include it instead of *.py
# TODO: patch3 should be rewritten to search for .pyc and .py not only .pyc and sent back
#
# Conditional build:
%bcond_without	static_libs # don't build static library
#
%define		_ver	0.8
%define		_test	test2
%define		_rel	0.1
#
Summary:	Non-visual routines for database frontend applications
Summary(pl):	Niegraficzne funkcje dla aplikacji bêd±cych frontendami do baz danych
Name:		hk_classes
Version:	%{_ver}
Release:	0.%{_test}.%{_rel}
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/hk-classes/%{name}-%{_ver}-%{_test}.tar.gz
# Source0-md5:	56bd57f8b633522dc8bea84bef169dc8
Patch0:		%{name}-dir.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		%{name}-PLD-search-for-pyc-and-in-usr-share.patch
URL:		http://hk-classes.sourceforge.net/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.7.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	Firebird-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-backend-devel >= 7.1
BuildRequires:	postgresql-devel >= 7.1
BuildRequires:	sqlite-devel
BuildRequires:	sqlite3-devel
BuildRequires:	unixODBC-devel
BuildRequires:	python-devel
Conflicts:      knoda < 0.7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hk_classes is a set of non-visual routines which allow you to develop
database frontend applications as easy as possible.

%description -l pl
hk_classes to zbiór niegraficznych funkcji, pozwalaj±cych na mo¿liwie
naj³atwiejsze tworzenie aplikacji bêd±cych frontendami do baz danych.

%package devel
Summary:	Header files for hk_classes
Summary(pl):	Pliki nag³ówkowe hk_classes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for hk_classes.

%description devel -l pl
Pliki nag³ówkowe hk_classes.

%package static
Summary:	Static hk_classes library
Summary(pl):	Statyczna biblioteka hk_classes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hk_classes library.

%description static -l pl
Statyczna biblioteka hk_classes.

%package driver-firebird
Summary:	Firebird driver for hk_classes
Summary(pl):	Sterownik Firebird dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-firebird
Firebird driver for hk_classes.

%description driver-firebird -l pl
Sterownik Firebird dla hk_classes.

%package driver-mysql
Summary:	MySQL driver for hk_classes
Summary(pl):	Sterownik MySQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-mysql
MySQL driver for hk_classes.

%description driver-mysql -l pl
Sterownik MySQL dla hk_classes.

%package driver-odbc
Summary:	unixODBC driver for hk_classes
Summary(pl):	Sterownik unixODBC dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-odbc
unixODBC driver for hk_classes.

%description driver-odbc -l pl
Sterownik unixODBC dla hk_classes.

%package driver-postgresql
Summary:	PostgreSQL driver for hk_classes
Summary(pl):	Sterownik PostgreSQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-postgresql
PostgreSQL driver for hk_classes.

%description driver-postgresql -l pl
Sterownik PostgreSQL dla hk_classes.

%package driver-sqlite2
Summary:	SQLite v2 driver for hk_classes
Summary(pl):	Sterownik SQLite v2 dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-sqlite2
SQLite version 2.x driver for hk_classes.

%description driver-sqlite2 -l pl
Sterownik SQLite w wersji 2.x dla hk_classes.

%package driver-sqlite3
Summary:	SQLite v3 driver for hk_classes
Summary(pl):	Sterownik SQLite v3 dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-sqlite3
SQLite version 3.x driver for hk_classes.

%description driver-sqlite3 -l pl
Sterownik SQLite w wersji 3.x dla hk_classes.

%package -n python-%{name}
Summary:        Python interface to %{name}
Summary(pl):    Interfejs do %{name} dla jezyka Python
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
%pyrequires_eq python-libs

%description -n python-%{name}
Python inteface to hk_classes.

%description -n python-%{name} -l pl
Pythonowy interfejs do klass hk_classes.

%package tools
Summary:	Commandline tools
Summary(pl):	Narzêdzia dzia³aj±ce z linii poleceñ
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Command line tools for hk_classes.

%description tools -l pl
Narzêdzia dzia³aj±ce z linii poleceñ dla hk_classes.

%package apidocs 
Summary:	API documentation for hk_classes
Summary(pl):	Dokumentacja API dla hk_classes
Group:		Documentation

%description apidocs 
API documentation for hk_classes.

%description apidocs -l pl
Dokumentacja API dla hk_classes.

%prep
%setup -q -n %{name}-%{_ver}-%{_test}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# supplied libtool is broken (C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-hk_classes-dir=%{_libdir} \
	--with-hk_classes-incdir=%{_includedir}/%{name} \
	--with-hk_classes-drvdir=%{_libdir}/%{name}/drivers \
	%{?with_static_libs:--enable-static=yes}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# drivers are dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/drivers/lib*.{la,a}

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

%files driver-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_firebirddriver.so*

%files driver-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mysqldriver.so*

%files driver-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_odbcdriver.so*

%files driver-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_postgresdriver.so*

%files driver-sqlite2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite2driver.so*

%files driver-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_sqlite3driver.so*

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
%doc apidocs/api apidocs/tutorial
