%define date	20040328

Summary:	A public domain Yacc parser generator
Name:		byacc
Version:	1.9
Release:	%mkrel 21
License:	Public Domain
Group:		Development/Other
URL:		http://dickey.his.com/byacc/byacc.html
# old source: ftp://ftp.cs.berkeley.edu/ucb/4bsd/
Source:		ftp://invisible-island.net/byacc/byacc.tar.bz2
Patch0:		byacc-1.9-fixmanpage.patch
Patch1:		byacc-1.9-automake.patch
Patch2:		byacc-1.9-security.patch
Patch3:		byacc-1.9-includes.patch
Patch4:		byacc-20040328-no-recreate-unionfile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to
install either this package or bison. Berkeley Yacc is regarded as a
better parser, while bison is more widely used under GNU world.

%prep

%setup -q -n %{name}-%{date}
%patch4 -p1 -b .unionfile

%build
%configure
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
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS NEW_FEATURES NOTES
%doc NO_WARRANTY README
%{_bindir}/byacc
%{_mandir}/man1/*


