# TODO:
# -  dir-patch needs to be altered TIA

Summary:	Non-visual routines for database frontend applications
Summary(pl):	Nie-graficzne funkcje dla aplikacji bêd±cych frontendami do baz danych
Name:		hk_classes
Version:	0.5.5
Release:	0.1
License:	GPL
Group:		Libraries
# Leave hk-classes in Source0 alone - it's not %{name}
Source0:	http://dl.sourceforge.net/sourceforge/hk-classes/%{name}-%{version}.tar.gz
Patch0:		%{name}-dir.patch
URL:		http://hk-classes.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-backend-devel >= 7.1
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hk_classes is a set of non-visual routines which allow you to develop
database frontend applications as easy as possible.

%description -l pl
hk_classes to zbiór nie-graficznych funkcji, pozwalaj±cych na mo¿liwie
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

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
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
