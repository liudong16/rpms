# $Id$

# Authority: dag
# Archs: i686 i586 i386 athlon
# Soapbox: 0
# Distcc: 0

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname ips
%define rversion 611
%define rrelease 0

%define moduledir /kernel/drivers/misc/ips
%define modules ips.o

Summary: Linux IBM PCI ServeRAID drivers.
Name: kernel-module-ips
Version: 6.11
Release: %{rrelease}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://www-3.ibm.com/pc/support/site.wss/MIGR-39729.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{rname}-%{rversion}.tgz
Source1: ips-Makefile
Source2: ips-kernel-ver.c
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Provides: kernel-modules

%description
Linux IBM PCI ServeRAID drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ips
Release: %{rrelease}_%{kversion}_%{krelease}
Summary: Linux IBM PCI ServeRAID drivers for SMP.
License: GPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules

%description -n kernel-smp-module-ips
Linux IBM PCI ServeRAID drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -c -n %{rname}-%{rversion}
%{__install} -m0644 %{SOURCE1} Makefile
%{__install} -m0644 %{SOURCE2} kernel-ver.c

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{rversion}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
%{__make} clean all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make SMP module.
%{__make} clean all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-ips
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-ips
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.ips README
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ips
%defattr(-, root, root, 0755)
%doc Changelog.ips README
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 6.11-0
- Initial package. (using DAR)
