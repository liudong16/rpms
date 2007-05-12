# $Id$
# Authority: dag

%define real_name ntfs-3g

Summary: Linux NTFS userspace driver 
Name: fuse-ntfs-3g
Version: 1.417
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.ntfs-3g.org/

Source: http://www.ntfs-3g.org/ntfs-3g-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.6.3
Requires: fuse >= 2.6.3

Provides: ntfsprogs-fuse = %{version}-%{release}
Obsoletes: ntfsprogs-fuse <= %{version}-%{release}
Provides: ntfs-g3 = %{version}-%{release}
Obsoletes: ntfs-g3 <= %{version}-%{release}

%description
The ntfs-3g driver is an open source, GPL licensed, third generation Linux NTFS
driver. It provides full read-write access to NTFS, excluding access to
encrypted files, writing compressed files, changing file ownership, access
right.

Technically it’s based on and a major improvement to the third generation Linux
NTFS driver, ntfsmount. The improvements include functionality, quality and
performance enhancements.

ntfs-3g features are being merged to ntfsmount. In the meanwhile, ntfs-3g is
currently the only free, as in either speech or beer, NTFS driver for Linux
that supports unlimited file creation and deletion.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-static \
	--disable-ldconfig
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Hardlink different locations
ln -f %{buildroot}%{_bindir}/ntfs-3g %{buildroot}/sbin/mount.ntfs-3g
ln -f %{buildroot}%{_bindir}/ntfs-3g %{buildroot}%{_bindir}/ntfsmount
ln -f %{buildroot}/sbin/mount.ntfs-3g %{buildroot}/sbin/mount.ntfs-fuse

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README
%doc %{_mandir}/man8/*.8*
/sbin/mount.ntfs-3g
/sbin/mount.ntfs-fuse
%{_bindir}/ntfs-3g
%{_bindir}/ntfsmount
%{_libdir}/libntfs-3g.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ntfs-3g/
%exclude %{_libdir}/libntfs-3g.la
%{_libdir}/libntfs-3g.so

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.417-1
- Initial package. (using DAR)
