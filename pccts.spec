Summary:	The Purdue Compiler-Construction Tools Set
Name:		pccts
Version:	1.33MR22
Release:	1
Group:		Utilities
Group(pl):	Narzędzia
Copyright:	Public Domain
Source0:	http://www.polhode.com/%{name}133mr.zip
BuildPrereq:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Purdue Compiler-Construction Tools Set

#%description -l pl

%package devel
Summary:	Headers for pccts
Summary(pl):	Pliki nagłówkowe dla pccts
Group:		Development/Libraries
Group(fr):	Development/Librairies
Requires:	%{name} = %{version}

%description devel
Header files required to compile programs using pccts.

%description -l pl devel
Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilacji programów
korzystających z pccts.

%prep
rm -rf %{name}
unzip -qo %{SOURCE0}
%setup -q -D -T -n %{name}

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS=$RPM_OPT_FLAGS; export CFLAGS
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name}}

rm bin/empty.txt

install bin/* $RPM_BUILD_ROOT%{_bindir}
install h/* $RPM_BUILD_ROOT%{_includedir}/%{name}

gzip -9nf *.txt NOTES* RIGHTS history.ps README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
