Summary:	Non-visual routines for database frontend applications
Summary(pl):	Niegraficzne funkcje dla aplikacji bêd±cych frontendami do baz danych
Name:		hk_classes
Version:	0.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/hk-classes/%{name}-%{version}.tar.bz2
# Source0-md5:	9bf3217c35795d83f29a3af7b6bb3ecb
Patch0:		%{name}-dir.patch
URL:		http://hk-classes.sourceforge.net/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake 
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	mysql-devel
BuildRequires:	postgresql-backend-devel >= 7.1
BuildRequires:	postgresql-devel >= 7.1
BuildRequires:	unixODBC-devel
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
Requires:	%{name} = %{version}

%description devel
Header files for hk_classes.

%description devel -l pl
Pliki nag³ówkowe hk_classes.

%package static
Summary:	Static hk_classes library
Summary(pl):	Statyczna biblioteka hk_classes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static hk_classes library.

%description static -l pl
Statyczna biblioteka hk_classes.

%package driver-mysql
Summary:	MySQL driver for hk_classes
Summary(pl):	Sterownik MySQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}

%description driver-mysql
MySQL driver for hk_classes.

%description driver-mysql -l pl
Sterownik MySQL dla hk_classes.

%package driver-odbc
Summary:	unixODBC driver for hk_classes
Summary(pl):	Sterownik unixODBC dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}

%description driver-odbc
unixODBC driver for hk_classes.

%description driver-odbc -l pl
Sterownik unixODBC dla hk_classes.

%package driver-postgresql
Summary:	PostgreSQL driver for hk_classes
Summary(pl):	Sterownik PostgreSQL dla hk_classes
Group:		Libraries
Requires:	%{name} = %{version}

%description driver-postgresql
PostgreSQL driver for hk_classes.

%description driver-postgresql -l pl
Sterownik PostgreSQL dla hk_classes.

%package tools
Summary:	Commandline tools 
Summary(pl):	Narzêdzia dzia³aj±ce z linii poleceñ
Group:		Applications
Requires:	%{name} = %{version}

%description tools
Command line tools for hk_classes.

%description tools  -l pl
Narzêdzia dzia³aj±ce z linii poleceñ dla hk_classes.

%prep
%setup -q
%patch -p1

%build
# supplied libtool is broken (C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
echo "echo" >> Makefile.am
%{__automake}

%configure \
	--with-hk_classes-dir=%{_libdir} \
	--with-hk_classes-incdir=%{_includedir}/%{name} \
	--with-hk_classes-drvdir=%{_libdir}/%{name}/drivers \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/drivers

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files driver-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_mysqldriver.so*
%{_libdir}/%{name}/drivers/libhk_mysqldriver.la

%files driver-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_odbcdriver.so*
%{_libdir}/%{name}/drivers/libhk_odbcdriver.la

%files driver-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/drivers/libhk_postgresdriver.so*
%{_libdir}/%{name}/drivers/libhk_postgresdriver.la

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hk_*
%{_mandir}/man?/*
