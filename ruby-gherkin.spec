%define	pkgname	gherkin
Summary:	Fast Gherkin lexer/parser
Name:		ruby-%{pkgname}
Version:	2.11.6
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	91a79a6a4fe03f51f039f7006581c468
URL:		http://github.com/cucumber/gherkin
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
# .gemspec requires 1.7.5, but we have only 1.5.5 with ruby 1.9
Requires:	ruby-json
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
