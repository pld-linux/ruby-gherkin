%define	pkgname	gherkin
Summary:	Fast Gherkin lexer/parser
Name:		ruby-%{pkgname}
Version:	2.11.6
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	91a79a6a4fe03f51f039f7006581c468
URL:		http://github.com/cucumber/gherkin
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
# .gemspec requires 1.7.5, but we have only 1.5.5 with ruby 1.9
Requires:	ruby-json
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%prep
%setup -q -n %{pkgname}-%{version}

%build
for lexer_dir in ext/%{pkgname}_lexer_*; do
	cd $lexer_dir
		ruby extconf.rb
		%{__make} V=1 \
			CC="%{__cc}" \
			LDFLAGS="%{rpmldflags}" \
			CFLAGS="%{rpmcflags} -fPIC"
	cd -
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

find ext -name '*.so' -exec install -p {} $RPM_BUILD_ROOT%{ruby_vendorarchdir} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%lang(ar) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ar.so
%lang(bg) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_bg.so
%lang(bm) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_bm.so
%lang(ca) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ca.so
%lang(cs) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_cs.so
%lang(cy_GB) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_cy_gb.so
%lang(da) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_da.so
%lang(de) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_de.so
%lang(en) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en.so
%lang(en) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en_lol.so
%lang(en) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en_pirate.so
%lang(en) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en_scouse.so
%lang(en) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en_tx.so
%lang(en_AU) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_en_au.so
%lang(eo) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_eo.so
%lang(es) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_es.so
%lang(et) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_et.so
%lang(fa) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_fa.so
%lang(fi) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_fi.so
%lang(fr) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_fr.so
%lang(he) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_he.so
%lang(hi) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_hi.so
%lang(hr) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_hr.so
%lang(hu) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_hu.so
%lang(id) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_id.so
%lang(is) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_is.so
%lang(it) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_it.so
%lang(ja) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ja.so
%lang(ko) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ko.so
%lang(lt) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_lt.so
%lang(lu) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_lu.so
%lang(lv) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_lv.so
%lang(nl) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_nl.so
%lang(no) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_no.so
%lang(pl) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_pl.so
%lang(pt) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_pt.so
%lang(ro) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ro.so
%lang(ru) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_ru.so
%lang(sk) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_sk.so
%lang(sr@cyrillic) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_sr_cyrl.so
%lang(sr@latin) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_sr_latn.so
%lang(sv) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_sv.so
%lang(tl) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_tl.so
%lang(tr) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_tr.so
%lang(tt) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_tt.so
%lang(uk) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_uk.so
%lang(uz) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_uz.so
%lang(vi) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_vi.so
%lang(zh_CN) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_zh_cn.so
%lang(zh_TW) %attr(755,root,root) %{ruby_vendorarchdir}/gherkin_lexer_zh_tw.so
