# $Id$

# Authority: dag

Summary: Monitor the progress of data through a pipe.
Name: pv
Version: 0.7.0
Release: 0
License: Artistic
Group: Development/Tools
URL: http://www.ivarch.com/programs/pv.shtml

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ivarch.com/programs/sources/pv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%prep
%setup

### FIXME: When using %%makeinstall macro we get a double buildroot ! (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(RPM_BUILD_ROOT\)||g' autoconf/make/unreal.mk

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README doc/COPYING doc/NEWS doc/TODO doc/*.html doc/*.txt
%doc %{_mandir}/man?/*
%doc %{_infodir}/*
%{_bindir}/*

%changelog
* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Initial package. (using DAR)
