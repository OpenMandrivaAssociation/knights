#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Chess game
Name:		plasma6-knights
Version:	24.12.1
Release:	%{?git:0.%{git}.}1
Group:		Games/Boards
License:	GPL
URL:		https://invent.kde.org/games/knights
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/knights/-/archive/%{gitbranch}/knights-%{gitbranchd}.tar.bz2#/knights-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/games/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/knights/-/archive/%{gitbranch}/knights-%{gitbranchd}.tar.bz2#/knights-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/knights-%{version}.tar.xz
%endif
%endif
Requires:	gnuchess
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(Freetype)
BuildRequires:	cmake(Fontconfig)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  qt6-qtmultimedia-gstreamer
BuildRequires:  appstream
BuildRequires:	ninja
BuildRequires:	7zip

%description
Knights is KDE's chess frontend.
It supports playing local games against human players or against chess
engines (XBoard and UIC)

%files -f knights.lang
%{_bindir}/knights
%{_datadir}/applications/org.kde.knights.desktop
%{_datadir}/config.kcfg/knights.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_datadir}/icons/hicolor/*/*/knights*
%{_datadir}/knights
%{_datadir}/knsrcfiles/knights.knsrc
%{_datadir}/metainfo/org.kde.knights.appdata.xml
%{_datadir}/qlogging-categories6/knights.categories
%{_datadir}/qlogging-categories6/knights.renamecategories

%prep
%autosetup -p1 -n knights-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang knights --with-html
