# $Id$

# Authority: dag

Summary: Secure file deletion utility.
Name: wipe
Version: 2.2.0
Release: 0
License: GPL
Group: System Environment/Base
URL: http://wipe.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/wipe/wipe-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Wipe is a tool that effectively degauses the surface of a hard
disk, making it virtually impossible to retrieve the data that was
stored on it. This tool is designed to make sure secure data that is
erased from a hard drive is unrecoverable.

%prep
%setup

#%{__perl} -pi.orig -e '
#		s|\$\(prefix\)/man|\$(mandir)|g;
#		s|\$\(prefix\)/doc|\$(datadir)/doc|g;
#	' Makefile.in
#%{__perl} -pi.orig -e 's|(#include <sys/stat.h>)|$1\n#include <errno.h>|g' rand.h

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/wipe/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES copyright LICENSE README TESTING TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 2.2.0-0
- Initial package. (using DAR)
