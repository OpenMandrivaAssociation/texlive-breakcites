# revision 21014
# category Package
# catalog-ctan /macros/latex/contrib/breakcites
# catalog-date 2010-12-11 10:17:50 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-breakcites
Version:	20101211
Release:	2
Summary:	Ensure that multiple citations may break at line end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/breakcites
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Makes a very minor change to the operation of the \cite
command. Note that the change is not necessary in unmodified
LaTeX; however, there remain packages that restore the
undesirable behaviour of the command as provided in LaTeX 2.09.
(Note that neither cite nor natbib make this mistake.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/breakcites/breakcites.sty
%doc %{_texmfdistdir}/doc/latex/breakcites/README
%doc %{_texmfdistdir}/doc/latex/breakcites/breakcites.pdf
%doc %{_texmfdistdir}/doc/latex/breakcites/breakcites.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
