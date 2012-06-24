Summary:	The Purdue Compiler-Construction Tools Set
Summary(pl):	Zestaw narz�dzi do tworzenia kompilator�w
Summary(pt_BR):	PCCTS - The Purdue Compiler Construction Tool Set
Name:		pccts
Version:	1.33MR33
Release:	8
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.polhode.com/%{name}133mr.zip
# Source0-md5:	fd70972b0a6aa2d3cf8b5c66d26d229d
Source1:	http://www.polhode.com/pcctsbk2.pdf
# Source1-md5:	ad0ce95ab5102d0ac89b1980fb5d2788
Source2:	http://www.antlr.org/1.33/tutorial.zip
# Source2-md5:	223c7b096d22c44fd1fbbbd84b392f01
Patch0:		%{name}-antlr.patch
URL:		http://www.polhode.com/pccts.html
BuildRequires:	unzip
Obsoletes:	pccts-devel
Obsoletes:	pccts-antlr
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
The Purdue Compiler-Construction Tools Set - zestaw narz�dzi public
domain zaprojektowanych do implementowania kompilator�w i innych
system�w t�umacz�cych. Narz�dzia te zawieraj� antlr, dlg i kod
wspieraj�cy. Pod wieloma wzgl�dami PCCTS jest podobny do wysoko
zintegrowanych wersji YACC [Joh78] i LEX [Les75]; antlr (ANother Tool
for Language Recognition) jest odpowiednikiem YACC, a dlg (DFA-based
Lexical analyzer Generator) dzia�a jak LEX. PCCTS ma jednak wiele
dodatkowych mo�liwo�ci, kt�re u�atwiaj� u�ywanie w szerszym zakresie
problem�w translacji.

%description -l pt_BR
O PCCTS � um conjunto de ferramentas de dom�nio p�blico projetados
para facilitar a implementa��o de compiladores e outros sistemas de
tradu��o. Estas ferramentas atualmente incluem: antlr, dlg e c�digo de
suporte. De muitas maneiras o PCCTS � similar � vers�o altamente
integrada do YACC [Joh78] e LEX [Les75]; onde o antlr (ANother Tool
for Language Recognition) corresponde ao YACC e o dlg (DFA-based
Lexical analyzer Generator) funciona como o LEX. Entretanto o PCCTS
tem muitas caracter�sticas adicionais que tornam mais f�cil seu uso em
um conjunto maior de problemas de tradu��o.

%prep
%setup -q -n %{name} -a2
%patch0

%build
mv -f support/genmk/genmk.c support/genmk/genmk.c.org
sed -e 's#/usr/local/pccts#%{_libdir}/%{name}#g' support/genmk/genmk.c.org > support/genmk/genmk.c
%{__make} \
	CC="%{__cc}" \
	COPT="%{rpmcflags} -DPCCTS_USE_STDARG"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/%{name}/{sorcerer,h}}

ln -s %{_bindir} $RPM_BUILD_ROOT%{_libdir}/%{name}/bin

rm -f bin/empty.txt

install bin/* $RPM_BUILD_ROOT%{_bindir}
install h/* $RPM_BUILD_ROOT%{_libdir}/%{name}/h
install antlr/antlr.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}-antlr.1

install dlg/dlg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} .
cp -r sorcerer/{h,lib} $RPM_BUILD_ROOT%{_libdir}/%{name}/sorcerer

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{_libdir}/%{name}/h ]; then
	rm -f %{_libdir}/%{name}/h
fi

%files
%defattr(644,root,root,755)
%doc *.txt *.pdf NOTES* RIGHTS history.ps README tutorial
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*
