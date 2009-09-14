#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Long-Descriptive
Summary:	Getopt::Long::Descriptive - Getopt::Long with usage text
Summary(pl.UTF-8):	Getopt::Long::Descriptive - Getopt::Long z tekstem użycia
Name:		perl-Getopt-Long-Descriptive
Version:	0.077
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a39971f6f138ebe6004438402620d032
URL:		http://search.cpan.org/dist/Getopt-Long-Descriptive/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Params-Validate >= 0.74
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convenient wrapper for Getopt::Long and program usage output

%description -l pl.UTF-8
Wygodne opakowanie Getopt::Long i wyjścia o użyciu programu

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
%{perl_vendorlib}/Getopt/Long/*.pm
%dir %{perl_vendorlib}/Getopt/Long/Descriptive
%{perl_vendorlib}/Getopt/Long/Descriptive/Usage.pm
%{_mandir}/man3/*
