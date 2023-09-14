%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Chess game
Name:		knights
Version:	23.08.1
Release:	1
Group:		Games/Boards
License:	GPL
URL:		https://invent.kde.org/games/knights
%if 0%{?git:1}
Source0:        https://invent.kde.org/games/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Requires:	gnuchess
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Freetype)
BuildRequires:	cmake(Fontconfig)
BuildRequires:	ninja

%description
Knights is KDE's chess frontend.
It supports playing local games against human players or against chess
engines (XBoard and UIC)

%files -f %{name}.lang
%{_bindir}/knights
%{_datadir}/applications/org.kde.knights.desktop
%{_datadir}/config.kcfg/knights.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_datadir}/icons/hicolor/*/*/knights*
%{_datadir}/knights
%{_datadir}/knsrcfiles/knights.knsrc
%{_datadir}/kxmlgui5/knights/knightsui.rc
%{_datadir}/metainfo/org.kde.knights.appdata.xml
%{_datadir}/qlogging-categories5/knights.categories

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html
