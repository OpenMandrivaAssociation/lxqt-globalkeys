%define major 0
%define libname %mklibname lxqt-globalkeys %{major}
%define devname %mklibname lxqt-globalkeys -d
%define uiname %mklibname lxqt-globalkeys-ui %{major}
%define uidevname %mklibname lxqt-globalkeys-ui -d

Summary:	Global keys config module for LXQt
Name:		lxqt-globalkeys
Version:	0.7.0
Release:	4
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(lxqt)

%description
Global keys config module for LXQt.

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/lxqt/lxqt-config-globalkeys*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The LXQt globalkeys library
Group:		System/Libraries

%description -n %{libname}
The LXQt globalkeys library.

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{uiname}
Summary:	The LXQt globalkeys UI library
Group:		System/Libraries

%description -n %{uiname}
The LXQt globalkeys UI library.

%files -n %{uiname}
%{_libdir}/liblxqt-globalkeys-ui.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the LXQt globalkeys library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the LXQt globalkeys library.

%files -n %{devname}
%{_libdir}/liblxqt-globalkeys.so
%{_includedir}/lxqt-globalkeys.h
%{_includedir}/lxqt-globalkeys
%{_libdir}/pkgconfig/lxqt-globalkeys.pc
%{_datadir}/cmake/lxqt_globalkeys

#----------------------------------------------------------------------------

%package -n %{uidevname}
Summary:	Development files for the LXQt globalkeys UI library
Group:		Development/C++
Requires:	%{uiname} = %{EVRD}

%description -n %{uidevname}
Development files for the LXQt globalkeys UI library.

%files -n %{uidevname}
%{_libdir}/liblxqt-globalkeys-ui.so
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/pkgconfig/lxqt-globalkeys-ui.pc
%{_datadir}/cmake/lxqt_globalkeys_ui

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

