# $Id$

# Authority: dag

Summary: Monitors hardware sensors
Name: gnome-sensors
Version: 0.9a
Release: 0
License: GPL
Group: Applications/System
URL: http://vkcorp.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://vedder.homelinux.org:81/%{name}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: lm_sensors-devel

%description
Monitors hardware sensors

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_libdir}/bonobo/servers/*

%changelog
* Tue Jan 28 2003 Dag Wieers <dag@wieers.com> - 0.9a
- Initial package. (using DAR)
