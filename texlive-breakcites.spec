Name:		texlive-breakcites
Version:	20101211
Release:	1
Summary:	Ensure that multiple citations may break at line end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/breakcites
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Makes a very minor change to the operation of the \cite
command. Note that the change is not necessary in unmodified
LaTeX; however, there remain packages that restore the
undesirable behaviour of the command as provided in LaTeX 2.09.
(Note that neither cite nor natbib make this mistake.).

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
