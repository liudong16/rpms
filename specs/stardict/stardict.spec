# $Id$

# Authority: dag

Summary: A versatile online dictionary.
Name: stardict
Version: 2.4.2
Release: 0
License: GPL
Group: Applications/System
URL: http://stardict.cosoft.org.cn/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://reciteword.cosoft.org.cn/yaoguang/downloadit.php?downloadFile=myapps/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libgnomeui-devel >= 2.2.0
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
StarDict is an international dictionary written for the GNOME environment.
It has powerful features such as "Glob-style pattern matching," "Scan
seletion word," "Fuzzy search," etc.

Please select and download dictionaries from:

	http://stardict.cosoft.org.cn/

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/stardict/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*.desktop
%{_datadir}/stardict/
%{_datadir}/idl/*.idl
%{_datadir}/pixmaps/*
%{_datadir}/omf/stardict/

%changelog
* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 2.4.2-0
- Updated to release 2.4.2.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 2.4.1-0
- Updated to release 2.4.1.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 2.4.0-0
- Updated to release 2.4.0.

* Tue Jul 01 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Updated to release 2.2.1.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.2.0-0
- Initial package. (using DAR)
