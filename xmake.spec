Name:		xmake
Version:	1.06
Release:	%mkrel 7
Summary:	Allows you to easily construct multiple complex dependencies
License:	GPL
Group:		Development/Other

Source0:	%{name}-%{version}.tar.bz2

URL:		http://apollo.backplane.com/xmake/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
XMAKE is similar to other make's out there, but is specifically designed to
allow you to easily construct multiple complex dependencies without getting
screwed by default rulesets. XMake contains a number of features specifically
designed to trivialize the construction of compilation rules.

%prep
%setup -q -n %{name}

%build
%make CFLAGS="$RPM_OPT_FLAGS"
perl -pi -e "s#-g -O2 -Wall -Wstrict-prototypes#$RPM_OPT_FLAGS#g" XMakefile
./%{name}

%install
rm -rf $RPM_BUILD_ROOT

install obj/%{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/xmake.1

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr (644,root,root,755)
%doc README RELEASE_NOTES
%defattr (-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.06-7mdv2010.0
+ Revision: 435133
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.06-6mdv2009.0
+ Revision: 262457
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.06-5mdv2009.0
+ Revision: 257125
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.06-3mdv2008.1
+ Revision: 130279
- kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.06-3mdv2007.0
+ Revision: 108879
- rebuild
- Import xmake

* Fri Oct 21 2005 Olivier Thauvin <nanardon@mandriva.org> 1.06-2mdk
- rebuild

* Sat Jul 31 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.06-1mdk
- 1.06
- really compile with $RPM_OPT_FLAGS
- update url
- cosmetics

