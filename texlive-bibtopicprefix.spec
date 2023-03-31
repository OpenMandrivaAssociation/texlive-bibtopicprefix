Name:		texlive-bibtopicprefix
Version:	15878
Release:	2
Summary:	Prefix references to bibliographies produced by bibtopic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibtopicprefix
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
