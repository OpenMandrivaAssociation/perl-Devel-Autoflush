%define upstream_name    Devel-Autoflush%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Set autoflush from the command line
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::CaptureOutput)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module is a hack to set autoflush for STDOUT and STDERR from the
command line or from 'PERL5OPT' for code that needs it but doesn't have it.

This often happens when prompting:

   # guess.pl
   print "Guess a number: ";
   my $n = <STDIN>;

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
%doc README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654311
- rebuild for updated spec-helper

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 624622
- import perl-Devel-Autoflush


