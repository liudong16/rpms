# $Id$

# Authority: dag

# Dists: rh62 rh73 rh80

%define rname Digest-HMAC

Name: perl-Digest-HMAC
Version: 1.01
Release: 1
Summary: Digest-HMAC Perl module
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-HMAC/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503

BuildRequires: perl(Digest::SHA1) %{?rh73:, perl(Digest::MD5)}
Requires: perl(Digest::SHA1) %{?rh73:, perl(Digest::MD5)}

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

HMAC follow the common Digest:: interface, but the constructor takes
the secret key and the name of some other simple Digest:: as argument.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}
#{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README rfc2104.txt
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
