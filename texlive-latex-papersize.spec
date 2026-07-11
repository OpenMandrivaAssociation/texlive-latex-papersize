%global tl_name latex-papersize
%global tl_revision 79316

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.71
Release:	%{tl_revision}.1
Summary:	Calculate LaTeX settings for any font and paper size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-papersize
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-papersize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-papersize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latex-papersize.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package's typical use is when preparing printed material for users
with low vision. The most effective way of doing this is to print on
(notional) small paper, and then to magnify the result. This package
calculates and applies the settings for various font and paper sizes.
Both a modern .sty file and a legacy Python script is included.

