Summary:	The Purdue Compiler-Construction Tools Set
Summary(pl):	Zestaw narzêdzi do tworzenia kompilatorów
Summary(pt_BR):	PCCTS - The Purdue Compiler Construction Tool Set
Name:		pccts
Version:	1.33MR33
Release:	2
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.polhode.com/%{name}133mr.zip
Source1:	http://www.polhode.com/pcctsbk2.pdf
Source2:	http://www.antlr.org/1.33/tutorial.zip
URL:		http://www.polhode.com/pccts.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCCTS is a set of public domain software tools designed to facilitate
the implementation of compilers and other translation systems. These
tools currently include antlr, dlg and support code. In many ways,
PCCTS is similar to a highly integrated version of YACC [Joh78] and
LEX [Les75]; where antlr (ANother Tool for Language Recognition)
corresponds to YACC and dlg (DFA-based Lexical analyzer Generator)
functions like LEX. However, PCCTS has many additional features which
make it easier to use for a wider range of translation problems.

%description -l pl
The Purdue Compiler-Construction Tools Set - zestaw narzêdzi do
tworzenia kompilatorów.

%description -l pt_BR
O PCCTS é um conjunto de ferramentas de domínio público projetados
para facilitar a implementação de compiladores e outros sistemas de
tradução. Estas ferramentas atualmente incluem: antlr, dlg e código de
suporte. De muitas maneiras o PCCTS é similar à versão altamente
integrada do YACC [Joh78] e LEX [Les75]; onde o antlr (ANother Tool
for Language Recognition) corresponde ao YACC e o dlg (DFA-based
Lexical analyzer Generator) funciona como o LEX. Entretanto o PCCTS
tem muitas características adicionais que tornam mais fácil seu uso em
um conjunto maior de problemas de tradução.

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
%setup -q -n %{name} -a2

%build
mv -f support/genmk/genmk.c support/genmk/genmk.c.org
sed -e 's#/usr/local/pccts#%{_libdir}/%{name}#g' support/genmk/genmk.c.org > support/genmk/genmk.c
%{__make} CC="%{__cc}" COPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -s %{_bindir} $RPM_BUILD_ROOT%{_libdir}/%{name}/bin
ln -s %{_includedir}/%{name} $RPM_BUILD_ROOT%{_libdir}/%{name}/h

rm -f bin/empty.txt

install bin/* $RPM_BUILD_ROOT%{_bindir}
install h/* $RPM_BUILD_ROOT%{_includedir}/%{name}
install antlr/antlr.1 $RPM_BUILD_ROOT%{_mandir}/man1
install dlg/dlg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.pdf NOTES* RIGHTS history.ps README tutorial
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/genmk
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/genmk
%{_includedir}/%{name}
%{_libdir}/%{name}
