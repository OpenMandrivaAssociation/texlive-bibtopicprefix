# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bibtopicprefix
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-bibtopicprefix
Version:	1.10
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package permits users to apply prefixes (fixed strings) to
references to entries in bibliographies produced by the
bibtopic package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
