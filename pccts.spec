Summary:	The Purdue Compiler-Construction Tools Set
Summary(pl):	Zestaw narzêdzi do tworzenia kompilatorów
Name:		pccts
Version:	1.33MR22
Release:	7
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.polhode.com/%{name}133mr.zip
URL:		http://www.polhode.com/pccts.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Purdue Compiler-Construction Tools Set.

%description -l pl
The Purdue Compiler-Construction Tools Set - zestaw narzêdzi do
tworzenia kompilatorów.

%package devel
Summary:	Headers for pccts
Summary(pl):	Pliki nag³ówkowe dla pccts
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required to compile programs using pccts.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilacji programów
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
