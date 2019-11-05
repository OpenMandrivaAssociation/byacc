Summary:	A public domain Yacc parser generator
Name:		byacc
Version:	20191103
Release:	1
License:	Public Domain
Group:		Development/Other
URL:		http://invisible-island.net/byacc/byacc.html
# old source: ftp://ftp.cs.berkeley.edu/ucb/4bsd/
Source0:	https://invisible-mirror.net/archives/byacc/byacc-%{version}.tgz
Requires(post,preun):	chkconfig

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to
install either this package or bison. Berkeley Yacc is regarded as a
better parser, while bison is more widely used under GNU world.

%prep
%autosetup -p1
%configure

%build
%make_build

%check
make check

%install
%make_install

mv %{buildroot}%{_bindir}/{yacc,byacc}
ln -s yacc.1 %{buildroot}%{_mandir}/man1/byacc.1

%post
%{_sbindir}/update-alternatives --install %{_bindir}/yacc yacc %{_bindir}/byacc 20

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove yacc %{_bindir}/byacc
fi

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%attr(0755,root,root) %{_bindir}/byacc
%{_mandir}/man1/*
