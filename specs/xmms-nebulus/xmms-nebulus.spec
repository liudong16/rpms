# $Id$

# Authority: dag

# Upstream: Pascal Brochart <pbrochart@tuxfamily.org>

%define plugindir %(xmms-config --visualization-plugin-dir)

Summary: An OpenGL visual plugin for XMMS.
Name: xmms-nebulus
Version: 0.6.0
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://nebulus.tuxfamily.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://nebulus.tuxfamily.org/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: xmms-devel, SDL-devel, SDL_ttf-devel

%description
Nebulus is an OpenGL visual plugin for XMMS.

%prep
%setup

%build
%configure \
	--enable-shared \
	--libdir="%{plugindir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{plugindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{plugindir}/*.so
%exclude %{plugindir}/*.la

%changelog
* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Fri Apr 04 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
