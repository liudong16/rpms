# $Id$

# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0

%{?rhfc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname madwifi
%define rversion 20040107

%define moduledir /kernel/drivers/net/wireless/madwifi
%define modules ath_hal/ath_hal.o wlan/wlan.o driver/ath_pci.o

Summary: Linux driver for the Multiband Atheros Wifi.
Name: kernel-module-madwifi
Version: 0.0.%{rversion}
Release: 0_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://www.mattfoster.clara.co.uk/madwifi-faq.htm

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/madwifi/%{rname}-%{rversion}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description
Linux driver for the Multiband Atheros Wifi.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-madwifi
Summary: Linux SMP driver for the Multiband Atheros Wifi.
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description -n kernel-smp-module-madwifi
Linux SMP driver for the Multiband Atheros Wifi.

These drivers are build for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

#%package -n madwifi-utils
#Summary: Madwifi utilities.
#Release: %{rrelease}
#Group: System Environment/Base
#
#%description -n madwifi-utils
#Madwifi utilities.

%prep
%setup -n %{rname}-%{rversion}

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
%{__make} %{?_smp_mflags} clean all \
	KERNEL_VERSION="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

#### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

#### Make SMP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_VERSION="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
#### Install utilities
#%{__install} -d -m0755 %{buildroot}%{_bindir}
#%{__install} -m0755 awstats

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-madwifi
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-madwifi
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT README
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-madwifi
%defattr(-, root, root, 0755)
%doc COPYRIGHT README
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

#%files -n madwifi-utils
#%defattr(-, root, root, 0755)
#%doc COPYRIGHT README
#%{_bindir}/*

%changelog
* Wed Jan 07 2004 Dag Wieers <dag@wieers.com> - 0.0.20040107-0
- Initial package. (using DAR)
