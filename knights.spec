Summary:	A simple chess board game for KDE4
Name:		knights
Version:	2.0
Release:	%mkrel 1
Source0:	http://kde-apps.org/CONTENT/content-files/122046-%{name}-%{version}-src.tar.gz
Group:		Graphical desktop/KDE
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

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_iconsdir}/hicolor/*/apps/*

%prep
%setup -q -n Knights

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

# fix permissions in the -debug package
chmod 644 build/src/*.h

%clean
rm -rf %{buildroot}
