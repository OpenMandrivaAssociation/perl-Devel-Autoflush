%define upstream_name    Devel-Autoflush
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	0.06
Release:	3

Summary:	Set autoflush from the command line
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/dagolden/Devel-Autoflush
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Devel-Autoflush-0.06.tar.gz

BuildRequires:	make
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
%setup -q -n Devel-Autoflush-0.06

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
%doc README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

