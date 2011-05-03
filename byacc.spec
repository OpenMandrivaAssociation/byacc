Summary:	A public domain Yacc parser generator
Name:		byacc
Version:	20101229
Release:	%mkrel 2
License:	Public Domain
Group:		Development/Other
URL:		http://invisible-island.net/byacc/byacc.html
# old source: ftp://ftp.cs.berkeley.edu/ucb/4bsd/
Source:		ftp://invisible-island.net/byacc/byacc-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to
install either this package or bison. Berkeley Yacc is regarded as a
better parser, while bison is more widely used under GNU world.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

mv %{buildroot}%{_bindir}/{yacc,byacc}
ln -s yacc.1 %{buildroot}%{_mandir}/man1/byacc.1

%post
%{_sbindir}/update-alternatives --install %{_bindir}/yacc yacc %{_bindir}/byacc 20

%preun
if [ $1 -eq 0 ]; then
	%{_sbindir}/update-alternatives --remove yacc %{_bindir}/byacc
fi

%triggerpostun -- byacc <= 1.9-16mdk
%{_sbindir}/update-alternatives --install %{_bindir}/yacc yacc %{_bindir}/byacc 20

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%attr(0755,root,root) %{_bindir}/byacc
%{_mandir}/man1/*
