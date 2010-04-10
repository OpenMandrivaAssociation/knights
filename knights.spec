%define	name	knights
%define	version	0.6.4
%define	release %mkrel 4

Summary: 	Chess game for KDE
Name: 		%name
Version: 	%version
Release: 	%release
Source: 	%name-%version.tar.bz2
Group: 		Games/Boards
License: 	GPL
URL: 		http://knights.sourceforge.net
BuildRoot: 	%_tmppath/%{name}-%{version}-buildroot
Provides: 	knights
BuildRequires:	kdelibs-devel

Patch0:         knights-0.6.4-gcc4.patch
%description
A chess interface for the K Desktop Environment. Knights works with all
XBoard compatible chess engines, FICS, and .pgn files.

%prep

%setup -q -n %name
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure	--build=%{_target_platform} \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--disable-rpath \
		--disable-debug \
		--enable-mt \
		--enable-shared \
		--disable-static \
		--disable-objprelink \
		--with-pic \
		--with-gnu-ld \
		--disable-embedded \
		--enable-fast-install=yes \
		--with-qt-dir=%{_prefix}/lib/qt3 \
		--with-xinerama
#		--enable-final
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -m644 $RPM_BUILD_ROOT%_datadir/icons/hicolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%_datadir/icons/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%_datadir/icons/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
 
%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files  -f %{name}.lang
%defattr(-,root,root)
%_bindir/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%_datadir/applnk/Games/Board/*.desktop

%dir %_datadir/apps/knights/
%_datadir/apps/knights/*.png
%_datadir/apps/knights/*.jpg
%_datadir/apps/knights/*.kml

%dir %_datadir/apps/knights/themes
%_datadir/apps/knights/themes/*.tar.gz
#%_datadir/apps/knights/themes/*.jpg

%dir %_datadir/doc/HTML/cz/knights/
%doc %_datadir/doc/HTML/cz/knights/common

%dir %_datadir/doc/HTML/de/knights/
%doc %_datadir/doc/HTML/de/knights/common

%dir %_datadir/doc/HTML/en/knights/
%doc %_datadir/doc/HTML/en/knights/common
%doc %_datadir/doc/HTML/en/knights/index.docbook

%dir %_datadir/doc/HTML/es/knights/
%doc %_datadir/doc/HTML/es/knights/common

%dir %_datadir/doc/HTML/et/knights/
%doc %_datadir/doc/HTML/et/knights/common

%dir %_datadir/doc/HTML/fr/knights/
%doc %_datadir/doc/HTML/fr/knights/common

%dir %_datadir/doc/HTML/fi/knights/
%doc %_datadir/doc/HTML/fi/knights/common

%dir %_datadir/doc/HTML/it/knights/
%doc %_datadir/doc/HTML/it/knights/common


%_datadir/icons/hicolor/16x16/apps/*.png
%_datadir/icons/hicolor/16x16/mimetypes/*.png

%_datadir/icons/hicolor/32x32/apps/*.png
%_datadir/icons/hicolor/32x32/mimetypes/*.png

%_datadir/icons/hicolor/48x48/apps/*.png
%_datadir/icons/hicolor/48x48/mimetypes/*.png

%_datadir/icons/hicolor/64x64/apps/*.png
%dir %_datadir/icons/hicolor/64x64/mimetypes/
%_datadir/icons/hicolor/64x64/mimetypes/*.png

%_datadir/apps/knights/knights.desktop
%_datadir/mimelnk/text/pgn.desktop

