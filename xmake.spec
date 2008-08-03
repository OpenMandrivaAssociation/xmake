Name:		xmake
Version:	1.06
Release:	%mkrel 6
Summary:	XMAKE allows you to easily construct multiple complex dependencies
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


