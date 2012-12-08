#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/eina eina; \
#cd eina; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf eina-$PKG_VERSION.tar.xz eina/ --exclude .svn --exclude .*ignore

%define snapshot 0
%if %{snapshot}
%define	svndate	20120103
%define	svnrev	66801
%endif

%define	major 1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Data Type Library
Name:		eina
%if %{snapshot}
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.7.2
Release:	1
%endif
Summary:	Data Type Library
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %{snapshot}
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

%description
Eina is a data type library.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif
%configure2_5x \
	--disable-cpu-sse \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.1-1
+ Revision: 806806
- version update 1.2.1

* Tue Jan 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.99.66801-0.20120103.1
+ Revision: 749943
- added missing define
- new svn snapshot 1.1.99.66801
- cleaned up spec and merged with Unity Linux spec
- disabled static build & cpu-sse

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.0.1-1
+ Revision: 681648
- update to new version 1.0.1

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2
+ Revision: 664129
- mass rebuild

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 1.0.0-1
+ Revision: 633900
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta3.1mdv2011.0
+ Revision: 622780
- 1.0 beta3

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta2.1mdv2011.0
+ Revision: 597465
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta.1mdv2011.0
+ Revision: 585278
- 1.0 beta

* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 0.9.9.49898-1mdv2011.0
+ Revision: 549890
- New version 0.9.9.49898

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 0.9.9.063-1mdv2010.1
+ Revision: 478093
- new version 0.9.9.063

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.0.2.062-1mdv2010.0
+ Revision: 411057
- new version 0.0.2.062

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.0.2.061-1mdv2010.0
+ Revision: 392853
- new version 0.0.2.061

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.0.2.060-1mdv2010.0
+ Revision: 370573
- New version 0.0.2.060

* Wed Mar 04 2009 Antoine Ginies <aginies@mandriva.com> 0.0.1-3mdv2009.1
+ Revision: 348382
- SVN SNAPSHOT 20090227, release 0.0.1

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 0.0.1-2mdv2009.1
+ Revision: 347179
- eina mempool is needed in the libraries package

* Fri Feb 27 2009 Antoine Ginies <aginies@mandriva.com> 0.0.1-1mdv2009.1
+ Revision: 345449
- remove epoch
- change group
- add buildroot tag
- import eina

