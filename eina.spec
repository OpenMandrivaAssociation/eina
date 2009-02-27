%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d
%define release %mkrel 1

Summary: Data Type Library
Name: eina
Version: 0.0.1
Release: %release
License: BSD
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
URL: http://www.enlightenment.org/

%description
Eina is a data type library.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{epoch}:%{version}-%{release}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %name-devel = %{epoch}:%{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.


%prep
%setup -q

%build
./autogen.sh
%configure
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/%name/mp/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/%name/mp/*.la
%{_includedir}/*


