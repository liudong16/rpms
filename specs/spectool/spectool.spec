# $Id$

# Authority: dag
# Upstream: Nils Philippsen <nphilipp@redhat.com>

Summary: Tool to display expanded Source/Patch macros from a SPEC file.
Name: spectool
Version: 1.0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://people.redhat.com/nphilipp/spectool/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://people.redhat.com/nphilipp/spectool/spectool-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl
Requires: perl

%description
spectool is a tool to display expanded Source/Patch macros from a SPEC file.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 spectool %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/*

%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
