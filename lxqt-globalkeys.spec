%define major 0
%define libname %mklibname lxqt-globalkeys-qt5 %{major}
%define devname %mklibname lxqt-globalkeys-qt5 -d
%define uiname %mklibname lxqt-globalkeys-ui-qt5 %{major}
%define uidevname %mklibname lxqt-globalkeys-ui-qt5 -d
%define git 20140802

Summary:	Global keys config module for LXQt
Name:		lxqt-globalkeys
Version:	0.8.0
%if %git
Source0:	%{name}-%{git}.tar.xz
Release:	0.%{git}.1
%else
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Release:	1
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(lxqt-qt5)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)

%description
Global keys config module for LXQt.

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/lxqt-qt5/lxqt-config-globalkeys*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The LXQt globalkeys library
Group:		System/Libraries

%description -n %{libname}
The LXQt globalkeys library.

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys-qt5.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{uiname}
Summary:	The LXQt globalkeys UI library
Group:		System/Libraries

%description -n %{uiname}
The LXQt globalkeys UI library.

%files -n %{uiname}
%{_libdir}/liblxqt-globalkeys-ui-qt5.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the LXQt globalkeys library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the LXQt globalkeys library.

%files -n %{devname}
%{_libdir}/liblxqt-globalkeys-qt5.so
%{_includedir}/lxqt-globalkeys-qt5
%{_libdir}/pkgconfig/lxqt-globalkeys-qt5.pc
%{_datadir}/cmake/lxqt-globalkeys-qt5

#----------------------------------------------------------------------------

%package -n %{uidevname}
Summary:	Development files for the LXQt globalkeys UI library
Group:		Development/C++
Requires:	%{uiname} = %{EVRD}

%description -n %{uidevname}
Development files for the LXQt globalkeys UI library.

%files -n %{uidevname}
%{_libdir}/liblxqt-globalkeys-ui-qt5.so
%{_includedir}/lxqt-globalkeys-ui-qt5
%{_libdir}/pkgconfig/lxqt-globalkeys-ui-qt5.pc
%{_datadir}/cmake/lxqt-globalkeys-ui-qt5

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

