Name:		texlive-gsemthesis
Version:	56291
Release:	1
Summary:	Geneva School of Economics and Management PhD thesis format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gsemthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsemthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsemthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gsemthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a PhD thesis template for the Geneva School
of Economics and Management (GSEM), University of Geneva,
Switzerland. The class provides utilities to easily set up the
cover page, the front matter pages, the page headers, etc.,
conformant to the official guidelines of the GSEM Faculty for
writing PhD dissertations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gsemthesis
%{_texmfdistdir}/tex/latex/gsemthesis
%doc %{_texmfdistdir}/doc/latex/gsemthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
