# TODO: 
# - Make find mysql. 
#   It claims that mysql is not available even when mysql-devel is installed.
#
# - Package properly hk_classes-libs hk_classess-devel ...
#
# - Make includes go to
#   /usr/include/hk_classes
#
# - Check what it really needs to build. 
#
# - Check if ldconfig is run after install properly
#
# - Rethink /usr/lib/drivers -> /usr/lib 
#   If changed check how it works with knoda.spec


Name:		hk_classes
Summary:	hk_classes -- hk_classes widgets for KDE
Summary(pl):Komponenty okienkowe  hk_classes dla KDE 
Version:	0.5.4
Release:	1.2
License:	GPL
Group:		Applications/Databases
# Source0:	http://knoda.sourceforge.net/%{name}-%{version}.tar.gz

# Left hk-classes in Source0 alone - it's not %{name}
Source0:http://dl.sourceforge.net/sourceforge/hk-classes/%{name}-%{version}.tar.gz
BuildRequires:	postgresql-backend-devel >= 7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A long description
%description -l pl
Zbiór komponentów okienkowych do operacji na bazach danych przeznaczony 
dla KDE. 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

./configure \
    --prefix=%{_libdir} \
    --includedir=%{_includedir}/%{name}

#%{__make}
make 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
# find . -type f -o -type l | sed 's|^\.||' > $RPM_BUILD_ROOT/master.list

%clean
rm -rf $RPM_BUILD_ROOT

# %files -f %{_tmppath}/%{name}-buildroot/master.list
%files
%defattr(644,root,root,755)
%attr (-,root,root) /*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
