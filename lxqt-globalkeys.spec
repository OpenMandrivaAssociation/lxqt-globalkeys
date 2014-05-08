%define libname %mklibname lxqt-globalkeys 0
%define uiname %mklibname lxqt-globalkeys-ui 0
%define devname %mklibname -d lxqt-globalkeys
%define uidevname %mklibname -d lxqt-globalkeys-ui

Name: lxqt-globalkeys
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: Global keys config module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel

%description
Global keys config module for LXQt

%package -n %{libname}
Summary: The LXQt globalkeys library
Group: System/Libraries

%description -n %{libname}
The LXQt globalkeys library

%package -n %{uiname}
Summary: The LXQt globalkeys UI library
Group: System/Libraries

%description -n %{uiname}
The LXQt globalkeys UI library

%package -n %{devname}
Summary: Development files for the LXQt globalkeys library
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the LXQt globalkeys library

%package -n %{uidevname}
Summary: Development files for the LXQt globalkeys UI library
Group: Development/C
Requires: %{uiname} = %{EVRD}

%description -n %{uidevname}
Development files for the LXQt globalkeys UI library

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/lxqt/lxqt-config-globalkeys*

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys.so.0*

%files -n %{uiname}
%{_libdir}/liblxqt-globalkeys-ui.so.0*

%files -n %{devname}
%{_libdir}/liblxqt-globalkeys.so
%{_includedir}/lxqt-globalkeys.h
%{_includedir}/lxqt-globalkeys
%{_libdir}/pkgconfig/lxqt-globalkeys.pc
%{_datadir}/cmake/lxqt_globalkeys

%files -n %{uidevname}
%{_libdir}/liblxqt-globalkeys-ui.so
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/pkgconfig/lxqt-globalkeys-ui.pc
%{_datadir}/cmake/lxqt_globalkeys_ui
