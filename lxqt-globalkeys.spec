%define major 0
%define libname %mklibname lxqt-globalkeys %{major}
%define devname %mklibname lxqt-globalkeys -d
%define uiname %mklibname lxqt-globalkeys-ui %{major}
%define uidevname %mklibname lxqt-globalkeys-ui -d
%define git 0

Summary:	Global keys config module for LXQt
Name:		lxqt-globalkeys
Version:	0.10.0
%if %git
Source0:	%{name}-%{git}.tar.xz
Release:	1.%{git}.1
%else
Source0:	https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
Release:	2
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	pkgconfig(x11)

%description
Global keys config module for LXQt.

%files -f lxqt-config-globalkeyshortcuts.lang
%{_bindir}/*
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The LXQt globalkeys library
Group:		System/Libraries
Conflicts:	%{_lib}lxqt-globalkeys-qt5_0 < 0.9.0
%rename		%{_lib}lxqt-globalkeys-qt5_0

%description -n %{libname}
The LXQt globalkeys library.

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{uiname}
Summary:	The LXQt globalkeys UI library
Group:		System/Libraries
Conflicts:	%{_lib}lxqt-globalkeys-ui-qt5_0 < 0.9.0
%rename		%{_lib}lxqt-globalkeys-ui-qt5_0

%description -n %{uiname}
The LXQt globalkeys UI library.

%files -n %{uiname}
%{_libdir}/liblxqt-globalkeys-ui.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the LXQt globalkeys library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
%rename		%{_lib}lxqt-globalkeys-qt5-devel

%description -n %{devname}
Development files for the LXQt globalkeys library.

%files -n %{devname}
%{_libdir}/liblxqt-globalkeys.so
%{_includedir}/lxqt-globalkeys
%{_libdir}/pkgconfig/lxqt-globalkeys.pc
%{_datadir}/cmake/lxqt-globalkeys

#----------------------------------------------------------------------------

%package -n %{uidevname}
Summary:	Development files for the LXQt globalkeys UI library
Group:		Development/C++
Requires:	%{uiname} = %{EVRD}
%rename		%{_lib}lxqt-globalkeys-ui-qt5-devel

%description -n %{uidevname}
Development files for the LXQt globalkeys UI library.

%files -n %{uidevname}
%{_libdir}/liblxqt-globalkeys-ui.so
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/pkgconfig/lxqt-globalkeys-ui.pc
%{_datadir}/cmake/lxqt-globalkeys-ui
#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%find_lang lxqt-config-globalkeyshortcuts --with-qt

sed -i -e 's,^libdir=.*,libdir=%{_libdir},g' %{buildroot}%{_libdir}/pkgconfig/*.pc
