# $Id$

# Authority: dries

Summary: C++ library for rapid development of database applications
Name: hk_classes
Version: 0.6.3
Release: 1
License: GPL
Group: Development/Libraries
URL: http://hk-classes.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/hk-classes/hk_classes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, postgresql-devel, mysql-devel, unixODBC-devel, python, python-devel

%description
hk_classes is C++ library which allows rapid development of database
applications with all features a modern database application should have
like forms an reports. hk_classes is database and GUI independent.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING NEWS 
%{_bindir}/hk_*
%{_includedir}/hk_classes/*.h
%{_libdir}/hk_classes/drivers/libhk_*driver.*
%{_libdir}/hk_classes/libhk_classes.*
%{_libdir}/python*/site-packages/_hk_classes.*
%{_libdir}/python*/site-packages/hk_classes.*
%{_datadir}/man/man1/hk_*

%changelog
* Tue Dec 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.2a-1
- first packaging for Fedora Core 1
