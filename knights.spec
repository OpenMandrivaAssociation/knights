Summary:	A simple chess board game for KDE4
Name:		knights
Version:	2.5.0
Release:	1
Group:		Games/Boards
License:	GPL
URL:		http://kde-apps.org/content/show.php/Knights?content=122046
Source0:	http://dl.dropbox.com/u/2888238/Knights/%{name}-%{version}.tar.bz2
BuildRequires:	kdegames4-devel
Requires:	gnuchess

%description
Knights is a simple chess board for KDE4. It is a rewrite of the KDE3 Knights,
but it's not yet as feature-complete compared to the old one. Currently you can
play against computer engines that support the XBoard protocol (like GnuChess)
or against a player at the same computer. It has automatic rule checking and
some nice animations.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_configdir}/knights.knsrc
%{_kde_iconsdir}/hicolor/*/apps/*
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

%changelog
* Sat May 21 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1mdv2011.0
+ Revision: 676813
- update to new version 2.3.2

* Thu Mar 10 2011 Funda Wang <fwang@mandriva.org> 2.3.0-1
+ Revision: 643226
- update to new version 2.3.0

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 622249
- new version 2.2.0

* Tue Aug 03 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 565239
- update to 2.0.1

* Sat Apr 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0-1mdv2010.1
+ Revision: 533541
- change group
- new upstream kde4 port, version 2.0
- bring it back as there's a kde4 port now

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - old directory, without matching package

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-4mdv2009.0
+ Revision: 247799
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-2mdv2008.1
+ Revision: 142745
- kdedesktop2mdkmenu.pl is no more
- kill re-definition of %%buildroot on Pixel's request
- import knights

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Dec 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.4-2mdk
- Fix buildrequires  from Anssi Hannula 
- use mkrel

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.4-1mdk
- New release 0.6.4
- Fix File section
- Add Patch0 

* Thu Jun 19 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6-2mdk
- fix path to qt3 (lib64 issues)

* Sat Jun 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6-1mdk
- 0.6
- clean up spec file
- fix buildrequires
- fix filelist
- added icons to %%{_*iconsdir}

* Mon Apr 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.9-4mdk
- Fix spec file

* Sun Mar 02 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.9-3mdk
- Rebuild

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.5.9-2mdk
- rebuild

* Tue Jan 21 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.9-1mdk
- New version

* Mon Aug 18 2002 Laurent Culioli <laurent@pschit.net> 0.5.6-9mdk

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.6-8mdk
- Rebuild against gcc-3.2

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5.6-7mdk
- buildrequires kdesdk

* Mon Jul 01 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5.6-6mdk
- from Gilles CAULIER <caulier.gilles@free.fr> :
	- Remove the LibGLCore depency.

* Sun Jun 30 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.5.6-5mdk
- Fix a stupid RPM build.

* Sun Jun 30 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.5.6-4mdk
- Fix tar.gz source tarball file. Solve a bug on match.cpp.

* Sun Jun 23 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.6-3mdk
- Fix spec file

* Sat Jun 22 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.5.6-2mdk
- Change kde depencie. Add the knights icon to KDE menu. 

* Fri Jun 21 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.5.6-1mdk
- Original release
