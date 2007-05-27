#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Client-Keepalive
Summary:	POE::Component::Client::Keepalive - manage connections with keep-alive
Summary(pl.UTF-8):	POE::Component::Client::Keepalive - zarządzanie połączeniami keep-alive
Name:		perl-POE-Component-Client-Keepalive
Version:	0.1000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b44e206d4ab18c2d260c08f3a1dc4639
URL:		http://search.cpan.org/dist/POE-Component-Client-Keepalive/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 1:0.3100
BuildRequires:	perl-POE-Component-Client-DNS >= 0.9801
%endif
Requires:	perl-POE >= 1:0.3100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::Keepalive creates and manages connections for
other components. It maintains a cache of kept-alive connections for
quick reuse. It is written specifically for clients that can benefit
from kept-alive connections, such as HTTP clients. Using it for
one-shot connections would probably be silly.

%description -l pl.UTF-8
POE::Component::Client::Keepalive tworzy i zarządza połączeniami dla
innych komponentów. Utrzymuje cache połączeń keep-alive do szybkiego
ponownego użycia. Jest napisany szczególnie dla klientów
korzystających z połączeń keep-alive, takich jak klienci HTTP.
Używanie go do pojedynczych połączeń byłoby prawdopodobnie głupie.

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
%doc CHANGES README
%{perl_vendorlib}/POE/Component/Client/Keepalive.pm
%dir %{perl_vendorlib}/POE/Component/Connection
%{perl_vendorlib}/POE/Component/Connection/Keepalive.pm
%{_mandir}/man3/*
