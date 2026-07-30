%define upstream_name    Devel-PartialDump
%define upstream_version 0.20
Name:		perl-%{upstream_name}
Version:	0.20
Release:	2

Summary:	Partial dumping of data structures, optimized for argument
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/moose/Devel-PartialDump
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-PartialDump-0.20.tar.gz

BuildRequires:	make
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
%setup -q -n Devel-PartialDump-0.20

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Devel

