%global tl_name breakcites
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ensure that multiple citations may break at line end
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/breakcites
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breakcites.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Makes a very minor change to the operation of the \cite command. Note
that the change is not necessary in unmodified LaTeX; however, there
remain packages that restore the undesirable behaviour of the command as
provided in LaTeX 2.09. (Note that neither cite nor natbib make this
mistake.)

