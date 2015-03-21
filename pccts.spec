Summary:	The Purdue Compiler-Construction Tools Set
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia kompilatorów
Summary(pt_BR.UTF-8):	PCCTS - The Purdue Compiler Construction Tool Set
Name:		pccts
Version:	1.33MR33
Release:	10
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.polhode.com/%{name}133mr.zip
# Source0-md5:	fd70972b0a6aa2d3cf8b5c66d26d229d
Source1:	http://www.polhode.com/%{name}bk2.pdf
# Source1-md5:	ad0ce95ab5102d0ac89b1980fb5d2788
Source2:	http://www.antlr.org/1.33/tutorial.zip
# Source2-md5:	223c7b096d22c44fd1fbbbd84b392f01
Patch0:		%{name}-antlr.patch
Patch1:		format-security.patch
URL:		http://www.polhode.com/pccts.html
BuildRequires:	unzip
Obsoletes:	pccts-antlr
Obsoletes:	pccts-devel
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

%description -l pl.UTF-8
The Purdue Compiler-Construction Tools Set - zestaw narzędzi public
domain zaprojektowanych do implementowania kompilatorów i innych
systemów tłumaczących. Narzędzia te zawierają antlr, dlg i kod
wspierający. Pod wieloma względami PCCTS jest podobny do wysoko
zintegrowanych wersji YACC [Joh78] i LEX [Les75]; antlr (ANother Tool
for Language Recognition) jest odpowiednikiem YACC, a dlg (DFA-based
Lexical analyzer Generator) działa jak LEX. PCCTS ma jednak wiele
dodatkowych możliwości, które ułatwiają używanie w szerszym zakresie
problemów translacji.

%description -l pt_BR.UTF-8
O PCCTS é um conjunto de ferramentas de domínio público projetados
para facilitar a implementação de compiladores e outros sistemas de
tradução. Estas ferramentas atualmente incluem: antlr, dlg e código de
suporte. De muitas maneiras o PCCTS é similar à versão altamente
integrada do YACC [Joh78] e LEX [Les75]; onde o antlr (ANother Tool
for Language Recognition) corresponde ao YACC e o dlg (DFA-based
Lexical analyzer Generator) funciona como o LEX. Entretanto o PCCTS
tem muitas características adicionais que tornam mais fácil seu uso em
um conjunto maior de problemas de tradução.

%prep
%setup -q -n %{name} -a2
%patch0
%patch1 -p1

sed -i -e 's#/usr/local/pccts#%{_libdir}/%{name}#g' support/genmk/genmk.c
rm bin/empty.txt

cp -p %{SOURCE1} .

%build
%{__make} \
	CC="%{__cc}" \
	COPT="%{rpmcflags} -DPCCTS_USE_STDARG"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/%{name}/{sorcerer,h}}

ln -s %{_bindir} $RPM_BUILD_ROOT%{_libdir}/%{name}/bin
install -p bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p h/* $RPM_BUILD_ROOT%{_libdir}/%{name}/h
cp -p antlr/antlr.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}-antlr.1
cp -p dlg/dlg.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -r sorcerer/{h,lib} $RPM_BUILD_ROOT%{_libdir}/%{name}/sorcerer

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
if [ -L %{_libdir}/%{name}/h ]; then
	rm %{_libdir}/%{name}/h
fi

%files
%defattr(644,root,root,755)
%doc *.txt *.pdf NOTES* RIGHTS history.ps README tutorial
%attr(755,root,root) %{_bindir}/dlg
%attr(755,root,root) %{_bindir}/genmk
%attr(755,root,root) %{_bindir}/pccts-antlr
%attr(755,root,root) %{_bindir}/sor
%{_mandir}/man1/dlg.1*
%{_mandir}/man1/pccts-antlr.1*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/bin
%{_libdir}/%{name}/h
%{_libdir}/%{name}/sorcerer
