# $Id: pccts.spec,v 1.1 2000-04-19 13:08:43 mkochano Exp $
Summary:	-
Summary(pl):	-
Name:		pccts
Version:	1.33MR22
Release:	1
Group:		-
Group(pl):	-
Copyright:	Public Domain
Source0:	http://www.polhode.com/%{name}133mr.zip
#Patch0:		-
BuildPrereq:	unzip
#Requires:	-
#Prereq:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
unzip -qo %{SOURCE0}
%setup -q -D -T -n %{name}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS=$RPM_OPT_FLAGS; export CFLAGS
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

rm bin/empty.txt

install bin/* $RPM_BUILD_ROOT%{_bindir}

gzip -9nf *.txt NOTES* RIGHTS history.ps README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz

%changelog
$Log: pccts.spec,v $
Revision 1.1  2000-04-19 13:08:43  mkochano
- Initial release. I'm still working on this spec.
