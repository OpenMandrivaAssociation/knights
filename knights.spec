%define srcname Knights

Summary:	A simple chess board game for KDE4
Name:		knights
Version:	2.3.0
Release:	%mkrel 1
Source0:	http://dl.dropbox.com/u/2888238/Knights/%{name}-%{version}.tar.bz2
Group:		Games/Boards
License:	GPL
URL:		http://kde-apps.org/content/show.php/Knights?content=122046
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	kdegames4-devel >= 4.4.0
Requires:	gnuchess

%description
Knights is a simple chess board for KDE4. It is a rewrite of the KDE3 Knights,
but it's not yet as feature-complete compared to the old one. Currently you can
play against computer engines that support the XBoard protocol (like GnuChess)
or against a player at the same computer. It has automatic rule checking and
some nice animations.

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_configdir}/knights.knsrc
%{_kde_iconsdir}/hicolor/*/apps/*

%prep
%setup -qn %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
