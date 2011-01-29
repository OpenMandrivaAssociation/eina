%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: Data Type Library
Name: eina
Version: 1.0.0
Release: %mkrel 1
License: LGPLv2+
Group: Graphical desktop/Enlightenment
Source: http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
URL: http://www.enlightenment.org/
BuildRoot: %{_tmppath}/%{name}-buildroot

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
Requires: %libname = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%setup -qn %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

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
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
