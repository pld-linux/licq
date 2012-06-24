%define ver	1.0.4
%define snap	20011027
Summary:	An ICQ client for online messaging
Summary(pl):	Klient ICQ do przesy�ania wiadomo�ci po sieci
Name:		licq
Version:	%{ver}
Release:	0.%{snap}
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.licq.org/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{snap}.tar.gz
Source1:	%{name}-qt-gui.desktop
Patch0:		%{name}-console.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	qt-devel >= 2.1.1
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         autoreply_ver	1.0.2
%define         console_ver	1.0.3
%define		forwarder_ver	1.0.2
%define		jons_gtk_gui	0.10
%define         qt_gui_ver	%{version}
%define		rms_ver		0.23

%description
Licq is an ICQ online messaging system clone, written in C++. Licq
supports all of the major features of ICQ, including messaging, URLs,
chat, file transfer, and white pages information. Additionally, Licq
is very configurable and supports skins and different icon packs.

%description -l pl
Licq jest klonem systemu przesy�ania wiadomo�ci ICQ, napisanym w
j�zyku C++. Licq ma wszystkie wa�ne cechy oryginalnego klienta ICQ,
w��cznie z przesy�aniem wiadomo�ci, URLi, rozmow� na �ywo,
przesy�aniem plik�w oraz dost�pem do informacji z "bia�ych stron" ICQ.
Dodatkowo, Licq jest bardzo dobrze konfigurowalny, pozwalaj�c na
u�ywanie "sk�rek" oraz r�nych zestaw�w ikon.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl):	Pliki nag��wkowe niezb�dne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag��wkowe niezb�dne przy pisaniu wtyczek dla licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(pl):	Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce Qt
Version:	%{ver}.%{qt_gui_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u�ywaj�cy widget�w
Qt.

%package console
Summary:	Console user interface for Licq
Summary(pl):	Konsolowy interfejs u�ytkownika dla Licq
Version:	%{ver}.%{console_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}
Requires:	ncurses >= 5.0

%description console
This package contains console user interface for Licq, using ncurses
library.

%description console -l pl
Ten pakiet zawiera konsolowy interfejs dla Licq, u�ywaj�cy biblioteki
ncurses.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl):	Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK
Version:	%{ver}.%{jons_gtk_gui_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl
Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK.

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz�dzania Licq
Version:	%{ver}.%{rms_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz�dzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl):	Narz�dzie do automatycznego odpowiadania dla Licq
Version:	%{ver}.%{autoreply_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl
Ten pakiet zawiera narz�dzie dla Licq kt�re automatycznie zajmuje si�
przychodz�cymi wiadomo�ciami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl):	Narz�dzie do przesy�ania wiadomo�ci icq na email
Version:	%{ver}.%{forwarder_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl
Narz�dzie do przesy�ania wiadomo�ci icq na email.

%prep
%setup -q -n %{name}-%{snap}
%patch1 -p1
cd plugins/console/src
%patch0 -p4
cd ../../qt-gui/src
# KDE m4 macros sucks as hell
for header in *.h; do
  rheader=$(echo ${header} | sed -e 's#\.h##')
  /usr/X11R6/bin/moc -o ${rheader}.moc ${header} || :
done

%build
BASE=$(pwd)
for module in \
	. \
	plugins/auto-reply \
	plugins/console \
	plugins/email \
	plugins/jons-gtk-gui \
	plugins/qt-gui \
	plugins/rms; do
  cd $module
  %{__make} -f Makefile.cvs
  libtoolize --copy --force
  aclocal
  automake -a -c
  autoconf
  %configure \
  	--with-openssl-inc=%{_includedir}/openssl

#	--without-kde
# specifing --with-kde=no or without-kde causes always
# to enable KDE support so just don't put it here.

  %{__make}
  cd $BASE
done

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/auto-reply		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/console		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/email		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/jons-gtk-gui	DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/qt-gui		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/rms		DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/licq-qt_gui.desktop

mv -f plugins/console/README		doc/README.CONSOLE
mv -f plugins/email/README		doc/README.FORWARDER
mv -f plugins/auto-reply/README		doc/README.AUTOREPLY
mv -f plugins/jons-gtk-gui/TODO		doc/README.TODO.JONS-GTK

gzip -9nf doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,README*,TODO} \
	plugins/qt-gui/doc/{CHANGELOG,README,*.HOWTO,HINTS} \
	upgrade/UPGRADE README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/BUGS.gz doc/CHANGELOG.gz doc/CREDITS.gz doc/HINTS.gz
%doc doc/*.HOWTO.gz README-*.gz doc/TODO.gz doc/README.gz
%doc doc/README.SOCKS.gz 
%doc upgrade/*
%attr(755,root,root) %{_bindir}/licq
%attr(755,root,root) %{_bindir}/viewurl-*
%{_datadir}/licq/sounds
%{_datadir}/licq/translations
%{_datadir}/licq/utilities

%files devel
%defattr(644,root,root,755)
%{_includedir}/licq

%files qt-gui
%defattr(644,root,root,755)
%doc plugins/qt-gui/doc/*.gz
%attr(755,root,root) %{_libdir}/licq/licq_qt-gui*
%{_applnkdir}/Network/Communications/licq-qt_gui.desktop
%{_datadir}/licq/qt-gui/*.*
%dir %{_datadir}/licq/qt-gui/locale
%lang(cs) %{_datadir}/licq/qt-gui/locale/cs.qm
%lang(cs,cs_CZ) %{_datadir}/licq/qt-gui/locale/cs_CZ.qm
%lang(de) %{_datadir}/licq/qt-gui/locale/de.qm
%lang(es) %{_datadir}/licq/qt-gui/locale/es.qm
%lang(fr) %{_datadir}/licq/qt-gui/locale/fr.qm
%lang(it) %{_datadir}/licq/qt-gui/locale/it.qm
%lang(ja_JP.eucJP) %{_datadir}/licq/qt-gui/locale/ja_JP.eucJP.qm
%lang(pl) %{_datadir}/licq/qt-gui/locale/pl.qm
%lang(pt) %{_datadir}/licq/qt-gui/locale/pt.qm
%lang(ru) %{_datadir}/licq/qt-gui/locale/ru.qm
%lang(ru,ru_RU.KOI8) %{_datadir}/licq/qt-gui/locale/ru_RU.KOI8-R.qm
%lang(sv) %{_datadir}/licq/qt-gui/locale/sv.qm
%lang(tr) %{_datadir}/licq/qt-gui/locale/tr.qm

%files console
%defattr(644,root,root,755)
%doc doc/README.CONSOLE.gz
%attr(755,root,root) %{_libdir}/licq/licq_console*

%files forwarder
%defattr(644,root,root,755)
%doc doc/README.FORWARDER.gz
%attr(755,root,root) %{_libdir}/licq/licq_forwarder*

%files rms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/licq/licq_rms*

%files autoreply
%defattr(644,root,root,755)
%doc doc/README.AUTOREPLY.gz
%attr(755,root,root) %{_libdir}/licq/licq_autoreply*

%files jons-gtk-gui
%defattr(644,root,root,755)
%doc doc/README.AUTOREPLY.gz
%attr(755,root,root) %{_libdir}/licq/licq_jons-gtk-gui*
