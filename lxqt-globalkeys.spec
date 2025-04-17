%define major 2
%define oldlibname %mklibname lxqt-globalkeys 1
%define libname %mklibname lxqt-globalkeys
%define devname %mklibname lxqt-globalkeys -d
%define olduiname %mklibname lxqt-globalkeys-ui 1
%define uiname %mklibname lxqt-globalkeys-ui
%define uidevname %mklibname lxqt-globalkeys-ui -d
#define git 0

Summary:	Global keys config module for LXQt
Name:		lxqt-globalkeys
Version:	2.2.0
%if 0%{?git:1}
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	https://github.com/lxqt/lxqt-globalkeys/releases/download/%{version}/lxqt-globalkeys-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}1
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	pkgconfig(x11)
BuildRequires:	lxqt-build-tools
Conflicts:	lxqt-l10n < 0.12.0-6

%description
Global keys config module for LXQt.

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/lxqt-globalkeyshortcuts.desktop
%{_datadir}/lxqt/globalkeyshortcuts.conf
%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts
#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The LXQt globalkeys library
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
The LXQt globalkeys library.

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{uiname}
Summary:	The LXQt globalkeys UI library
Group:		System/Libraries
%rename %{olduiname}

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
%autosetup -p1
%cmake \
	-DUPDATE_TRANSLATIONS:BOOL=OFF \
	-G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

sed -i -e 's,^libdir=.*,libdir=%{_libdir},g' %{buildroot}%{_libdir}/pkgconfig/*.pc

%find_lang %{name} --with-qt --all-name
