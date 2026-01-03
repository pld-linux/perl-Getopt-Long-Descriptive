#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Getopt
%define	pnam	Long-Descriptive
Summary:	Getopt::Long::Descriptive - Getopt::Long with usage text
Summary(pl.UTF-8):	Getopt::Long::Descriptive - Getopt::Long z opisem użycia
Name:		perl-Getopt-Long-Descriptive
Version:	0.116
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Getopt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6ae7b7a4a976966ad49d452994b68c3
URL:		https://metacpan.org/dist/Getopt-Long-Descriptive
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.78
BuildRequires:	perl-devel >= 1:5.12.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-Getopt-Long >= 2.33
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Params-Validate >= 0.97
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Sub-Exporter >= 0.972
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Warnings >= 0.005
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convenient wrapper for Getopt::Long and program usage output.

%description -l pl.UTF-8
Wygodne opakowanie Getopt::Long i wyjścia o sposobie użycia programu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Getopt/Long
%{perl_vendorlib}/Getopt/Long/Descriptive.pm
%dir %{perl_vendorlib}/Getopt/Long/Descriptive
%{perl_vendorlib}/Getopt/Long/Descriptive/Opts.pm
%{perl_vendorlib}/Getopt/Long/Descriptive/Usage.pm
%{_mandir}/man3/Getopt::Long::Descriptive*.3pm*
