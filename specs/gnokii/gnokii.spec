# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Linux/UNIX tool suite for various mobile phones.
Name: gnokii
Version: 0.6.0
Release: 0
License: GPL
Group: Applications/Communications
URL: http://gnokii.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnokii.org/pub/gnokii/gnokii-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gettext, flex, gtk+-devel >= 1.2.0
%{?rhfc1:BuildRequires: bluez-libs-devel}
%{?rhel3:BuildRequires: bluez-libs-devel}
%{?rh90:BuildRequires: bluez-libs-devel}
%{?rh80:BuildRequires: bluez-libs-devel}
%{?rh73:BuildRequires: bluez-libs-devel}
%{?rhel21:BuildRequires: bluez-libs-devel}

%description
Gnokii is a Linux/UNIX tool suite and a modem/fax driver for
Nokia's mobile phones, released under the GPL.

%package gui
Summary: Graphical Linux/UNIX tool suite for Nokia mobile phones.
Group: Applications/Internet
Obsoletes: gnokii-xgnokii, gnokii-gtk

%description gui
Xgnokii is a graphical Linux/UNIX tool suite for Nokia's mobile phones. It
allows you to edit your contacts book, send/read SMS's from/in your
computer and more.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gnokii Mobile Manager
Comment=Access your mobile phone data
Icon=redhat-accessories.png
Exec=xgnokii
Terminal=false
Type=Application
Categories=Application;Utility;
EOF

%build
%configure \
	--with-x \
	--with-gnu-ld \
	--enable-nls \
	--enable-security
%{__make} %{?_smp_mflags}
#%{__make} %{?_smp_mflags} -C smsd all libpq.so libmysql.so libfile.so

%install
%{__rm} -rf %{buildroot}
%makeinstall
#makeinstall -C smsd
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir} \
			%{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_mandir}/man8/
%{__install} -m0644 Docs/sample/gnokiirc %{buildroot}%{_sysconfdir}
%{__install} -m0644 Docs/man/*.1 Docs/man/*.1x %{buildroot}%{_mandir}/man1/
%{__install} -m0644 Docs/man/*.8 %{buildroot}%{_mandir}/man8/

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Utilities/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor net                  \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%pre
/usr/sbin/groupadd -r -f gnokii 2>/dev/null

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null
/usr/sbin/groupdel gnokii 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING MAINTAINERS TODO Docs/Bugs Docs/CREDITS Docs/DataCalls-QuickStart
%doc Docs/FAQ Docs/README* Docs/gnokii-IrDA-Linux Docs/gnokii-ir-howto Docs/ringtones.txt
%doc Docs/protocol/ Docs/sample/
%doc %{_mandir}/man?/gnokii*
%doc %{_mandir}/man?/mgnokii*
%doc %{_mandir}/man?/ppm2nokia*
%doc %{_mandir}/man?/sendsms*
%doc %{_mandir}/man?/todologo*
%config(noreplace) %{_sysconfdir}/gnokiirc
%{_libdir}/*.so.*
%{_bindir}/ppm2nokia
%{_bindir}/sendsms
%{_bindir}/todologo
%{_bindir}/gnokii
%{_sbindir}/gnokiid
%defattr(4750, root, gnokii, 0755)
%{_sbindir}/mgnokiidev

%files gui -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/xgnokii*
%{_bindir}/xgnokii
%{_datadir}/xgnokii/
%if %{dfi}
        %{_datadir}/gnome/apps/Utilities/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/gnokii/

%changelog
* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.5.10-0
- Updated to release 0.5.10.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 0.5.8-0
- Updated to release 0.5.8.

* Sun Dec 21 2003 Dag Wieers <dag@wieers.com> - 0.5.6-0
- Updated to release 0.5.6.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.5.5-0
- Updated to release 0.5.5.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Updated to release 0.5.4.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Fri May 30 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
