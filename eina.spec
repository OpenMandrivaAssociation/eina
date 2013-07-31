%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Data Type Library
Name:		eina
Version:	1.7.8
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

%description
Eina is a data type library.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
%configure2_5x \
	--disable-cpu-sse \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libeina.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/libeina.so
%{_includedir}/*

