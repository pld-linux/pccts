Summary:	The Purdue Compiler-Construction Tools Set
Name:		pccts
Version:	1.33MR22
Release:	6
License:	Public Domain
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://www.polhode.com/%{name}133mr.zip
URL:		http://www.polhode.com/pccts.html
BuildPrereq:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Purdue Compiler-Construction Tools Set

%package devel
Summary:	Headers for pccts
Summary(pl):	Pliki nag³ówkowe dla pccts
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required to compile programs using pccts.

%description -l pl devel
Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilacji programów
korzystaj±cych z pccts.

%prep
rm -rf %{name}
unzip -qo %{SOURCE0}
%setup -q -D -T -n %{name}

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
