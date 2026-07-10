%global tl_name bibtopicprefix
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Prefix references to bibliographies produced by bibtopic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibtopicprefix
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopicprefix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package permits users to apply prefixes (fixed strings) to
references to entries in bibliographies produced by the bibtopic
package.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibtopicprefix
%dir %{_datadir}/texmf-dist/source/latex/bibtopicprefix
%dir %{_datadir}/texmf-dist/tex/latex/bibtopicprefix
%doc %{_datadir}/texmf-dist/doc/latex/bibtopicprefix/README
%doc %{_datadir}/texmf-dist/doc/latex/bibtopicprefix/bibtopicprefix.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibtopicprefix/bibtopicprefix.xml
%doc %{_datadir}/texmf-dist/source/latex/bibtopicprefix/bibtopicprefix.drv
%doc %{_datadir}/texmf-dist/source/latex/bibtopicprefix/bibtopicprefix.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibtopicprefix/bibtopicprefix.ins
%{_datadir}/texmf-dist/tex/latex/bibtopicprefix/bibtopicprefix.sty
