%define ver	1.0.4
%define snap	20011027
Summary:	An ICQ client for online messaging
Summary(es):	licq es un clone del ICQ(tm) escrito
Summary(pl):	Klient ICQ do przesy³ania wiadomo¶ci po sieci
Summary(pt_BR):	O licq é um clone do ICQ(tm) escrito
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
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	qt-devel >= 2.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         autoreply_ver		1.0.2
%define         console_ver		1.0.3
%define		forwarder_ver		1.0.2
%define		jons_gtk_gui_ver	0.10
%define         qt_gui_ver		%{version}
%define		rms_ver			0.23

%description
Licq is an ICQ online messaging system clone, written in C++. Licq
supports all of the major features of ICQ, including messaging, URLs,
chat, file transfer, and white pages information. Additionally, Licq
is very configurable and supports skins and different icon packs.

%description -l es
licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt. Es
un intento de dar a los usuarios de Linux una opción no-java para el
protocolo ICQ.

%description -l pl
Licq jest klonem systemu przesy³ania wiadomo¶ci ICQ, napisanym w
jêzyku C++. Licq ma wszystkie wa¿ne cechy oryginalnego klienta ICQ,
w³±cznie z przesy³aniem wiadomo¶ci, URLi, rozmow± na ¿ywo,
przesy³aniem plików oraz dostêpem do informacji z "bia³ych stron" ICQ.
Dodatkowo, Licq jest bardzo dobrze konfigurowalny, pozwalaj±c na
u¿ywanie "skórek" oraz ró¿nych zestawów ikon.

%description -l pt_BR
O licq é um clone do ICQ(tm) escrito em c++ usando biblioteca Qt. É
uma tentativa de dar aos usuários do Linux uma opção não-java para o
protocolo ICQ.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl):	Pliki nag³ówkowe niezbêdne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{ver}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag³ówkowe niezbêdne przy pisaniu wtyczek dla licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es):	QT user interface for licq
Summary(pl):	Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce Qt
Summary(pt_BR):	Interface QT para o licq
Version:	%{ver}_%{qt_gui_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description -l es devel
Plugins Development Kit for licq.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u¿ywaj±cy widgetów
Qt.

%description -l pt_BR devel
Ferramentas para desenvolvimento de plug-ins para o licq.

%package console
Summary:	Console user interface for Licq
Summary(es):	Console user interface for licq
Summary(pl):	Konsolowy interfejs u¿ytkownika dla Licq
Summary(pt_BR):	Interface de usuário de console para o licq
Version:	%{ver}_%{console_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}
Requires:	ncurses >= 5.0

%description console
This package contains console user interface for Licq, using ncurses
library.

%description -l es console
Includes console user interface for licq.

%description console -l pl
Ten pakiet zawiera konsolowy interfejs dla Licq, u¿ywaj±cy biblioteki
ncurses.

%description -l pt_BR console
Inclui interface de usuário de console para o licq.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl):	Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce GTK
Version:	%{ver}_%{jons_gtk_gui_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl
Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce GTK.

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz±dzania Licq
Version:	%{ver}_%{rms_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz±dzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl):	Narzêdzie do automatycznego odpowiadania dla Licq
Version:	%{ver}_%{autoreply_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl
Ten pakiet zawiera narzêdzie dla Licq które automatycznie zajmuje siê
przychodz±cymi wiadomo¶ciami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl):	Narzêdzie do przesy³ania wiadomo¶ci icq na email
Version:	%{ver}_%{forwarder_ver}
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{ver}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl
Narzêdzie do przesy³ania wiadomo¶ci icq na email.

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
  rm -f missing
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
