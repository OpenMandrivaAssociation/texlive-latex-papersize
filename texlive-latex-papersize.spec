Name:		texlive-latex-papersize
Version:	53131
Release:	1
Summary:	Calculate LaTeX settings for any font and paper size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-papersize
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-papersize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-papersize.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a Python script, whose typical use is when
preparing printed material for users with low vision. The most
effective way of doing this is to print on (notional) small
paper, and then to magnify the result; the script calculates
the settings for various font and paper sizes. More details are
to be read in the script itself.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/latex-papersize
%doc %{_texmfdistdir}/texmf-dist/doc/support/latex-papersize

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
