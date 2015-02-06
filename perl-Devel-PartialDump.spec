%define upstream_name    Devel-PartialDump
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Partial dumping of data structures, optimized for argument
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch

%description
This module is a data dumper optimized for logging of arbitrary parameters.

It attempts to truncate overly verbose data, in a way that is hopefully
more useful for diagnostics warnings than

	warn Dumper(@stuff);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Devel

%changelog
* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 672614
- update to new version 0.15

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 659931
- update to new version 0.14

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 488015
- update buildrequires:
- update to 0.13

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 463144
- update to 0.12

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 461271
- update to 0.11

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 403102
- rebuild using %%perl_convert_version

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2010.0
+ Revision: 391183
- update to new version 0.09

* Mon May 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 377369
- update to new version 0.08

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 352924
- import perl-Devel-PartialDump


* Sun Mar 08 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

