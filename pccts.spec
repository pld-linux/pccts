Summary:	The Purdue Compiler-Construction Tools Set
Summary(pl):	Zestaw narzÍdzi do tworzenia kompilatorÛw
Name:		pccts
Version:	1.33MR22
Release:	7
License:	Public Domain
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/NarzÍdzia
Source0:	http://www.polhode.com/%{name}133mr.zip
URL:		http://www.polhode.com/pccts.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Purdue Compiler-Construction Tools Set.

%description -l pl
The Purdue Compiler-Construction Tools Set - zestaw narzÍdzi do
tworzenia kompilatorÛw.

%package devel
Summary:	Headers for pccts
Summary(pl):	Pliki nag≥Ûwkowe dla pccts
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files required to compile programs using pccts.

%description -l pl devel
Ten pakiet zawiera pliki nag≥Ûwkowe niezbÍdne do kompilacji programÛw
korzystaj±cych z pccts.

%prep
%setup -q -n %{name}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name},%{_mandir}/man1}

rm -f bin/empty.txt

install bin/* $RPM_BUILD_ROOT%{_bindir}
install h/* $RPM_BUILD_ROOT%{_includedir}/%{name}
install antlr/antlr.1 $RPM_BUILD_ROOT%{_mandir}/man1
install dlg/dlg.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf *.txt NOTES* RIGHTS history.ps README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
