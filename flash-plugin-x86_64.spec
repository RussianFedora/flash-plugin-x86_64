Summary:	Adobe Flash Player 10
Name:		flash-plugin-x86_64
Version:	10.3.162.29
Release:	1%{?dist}
Epoch:		5

Group:		Applications/Internet
License:	Commercial
URL:		http://www.adobe.com
Source0:	http://download.macromedia.com/pub/labs/flashplayer10/flashplayer10_2_p3_64bit_linux_111710.tar.gz
Source1:	memcpy-10.3.162.29.bsdiff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	bsdiff
ExclusiveArch:	x86_64

%description
Adobe Flash Player "Square" for x86_64

%package -n flash-plugin
Summary:	Adobe Flash Player 10
Group:		Applications/Internet
License:	Commercial
ExclusiveArch:	x86_64

%description -n flash-plugin
Adobe Flash Player "Square" for x86_64

%prep
%setup -q -c -T -a 0

%build

%install
rm -rf %{buildroot}
install -dD  %{buildroot}%{_libdir}/mozilla/plugins/
install -dD  %{buildroot}%{_libdir}/flash-plugin/

bspatch libflashplayer.so \
        %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so \
        %{SOURCE1}

cd %{buildroot}%{_libdir}/mozilla/plugins/
ln -s ../../flash-plugin/libflashplayer.so

%clean
rm -rf %{buildroot}

%files -n flash-plugin
%defattr(-, root, root)
%{_libdir}/flash-plugin/*
%{_libdir}/mozilla/plugins/*.so


%changelog
* Fri Apr  8 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 10.3.162.29-1
- update to 10.3.162.29

* Mon Aug  3 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.32.18-1
- update to 10.0.32.18

* Fri Feb 27 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.22.87-1
- update to 10.0.22.87

* Mon Dec 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.d21.1-1
- we switched to Adobe x86_64 beta flash
- bump epoch
- Obsoletes flash-plugin

* Fri Dec 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-1
- update to 10.0.15.3

* Mon Nov 17 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-2
- remove depends on libflashsupport

* Wed Oct 15 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-1
- update to 10.0.12.36

* Thu May 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.0.124.0-1
- try to do everything for x86_64
