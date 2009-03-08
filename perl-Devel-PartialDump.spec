%define module   Devel-PartialDump
%define version    0.07
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Partial dumping of data structures, optimized for argument
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.gz
BuildRequires: perl(Mouse)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module is a data dumper optimized for logging of arbitrary parameters.

It attempts to truncate overly verbose data, in a way that is hopefully
more useful for diagnostics warnings than

	warn Dumper(@stuff);

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Devel

