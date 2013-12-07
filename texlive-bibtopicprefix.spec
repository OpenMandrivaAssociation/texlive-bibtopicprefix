# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bibtopicprefix
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-bibtopicprefix
Version:	1.10
Release:	5
Summary:	Prefix references to bibliographies produced by bibtopic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibtopicprefix
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package permits users to apply prefixes (fixed strings) to
references to entries in bibliographies produced by the
bibtopic package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibtopicprefix/bibtopicprefix.sty
%doc %{_texmfdistdir}/doc/latex/bibtopicprefix/README
%doc %{_texmfdistdir}/doc/latex/bibtopicprefix/bibtopicprefix.pdf
%doc %{_texmfdistdir}/doc/latex/bibtopicprefix/bibtopicprefix.xml
#- source
%doc %{_texmfdistdir}/source/latex/bibtopicprefix/bibtopicprefix.drv
%doc %{_texmfdistdir}/source/latex/bibtopicprefix/bibtopicprefix.dtx
%doc %{_texmfdistdir}/source/latex/bibtopicprefix/bibtopicprefix.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-2
+ Revision: 749697
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.10-1
+ Revision: 717943
- texlive-bibtopicprefix
- texlive-bibtopicprefix
- texlive-bibtopicprefix
- texlive-bibtopicprefix
- texlive-bibtopicprefix

