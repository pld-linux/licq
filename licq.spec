Summary:	An ICQ client for online messaging
Summary(es):	licq es un clone del ICQ(tm) escrito
Summary(pl):	Klient ICQ do przesy³ania wiadomo¶ci po sieci
Summary(pt_BR):	O licq é um clone do ICQ(tm) escrito
Name:		licq
Version:	1.2.0a
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp2.sourceforge.net/pub/sourceforge/licq/%{name}-%{version}.tar.bz2
Source1:	%{name}-qt-gui.desktop
Patch0:		%{name}-c++.patch
URL:		http://www.licq.org/
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

#%define	autoreply_ver		1.0.2
%define         console_ver		1.2.0
#%define	forwarder_ver		1.0.2
%define		jons_gtk_gui_ver	0.20
%define         qt_gui_ver		1.2.0
%define		rms_ver			0.30

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
Requires:	%{name} = %{version}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag³ówkowe niezbêdne przy pisaniu wtyczek dla licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es):	QT user interface for licq
Summary(pl):	Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce Qt
Summary(pt_BR):	Interface QT para o licq
#Version:	%{version}_%{qt_gui_ver}
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description devel -l es
Plugins Development Kit for licq.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u¿ywaj±cy widgetów
Qt.

%description devel -l pt_BR
Ferramentas para desenvolvimento de plug-ins para o licq.

%package console
Summary:	Console user interface for Licq
Summary(es):	Console user interface for licq
Summary(pl):	Konsolowy interfejs u¿ytkownika dla Licq
Summary(pt_BR):	Interface de usuário de console para o licq
#Version:	%{version}_%{console_ver}
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	ncurses >= 5.0

%description console
This package contains console user interface for Licq, using ncurses
library.

%description console -l es
Includes console user interface for licq.

%description console -l pl
Ten pakiet zawiera konsolowy interfejs dla Licq, u¿ywaj±cy biblioteki
ncurses.

%description console -l pt_BR
Inclui interface de usuário de console para o licq.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl):	Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce GTK
#Version:	%{version}_%{jons_gtk_gui_ver}
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl
Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce GTK.

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz±dzania Licq
#Version:	%{version}_%{rms_ver}
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz±dzania dla Licq.

#%package autoreply
#Summary:	Licq autoreply utility
#Summary(pl):	Narzêdzie do automatycznego odpowiadania dla Licq
#Version:	%{version}_%{autoreply_ver}
#Group:		Applications/Communications
#Requires:	%{name} = %{version}
#
#%description autoreply
#This package contains Licq utility for automatic handling of incoming
#messages.
#
#%description autoreply -l pl
#Ten pakiet zawiera narzêdzie dla Licq które automatycznie zajmuje siê
#przychodz±cymi wiadomo¶ciami.

#%package forwarder
#Summary:	Licq email forwarder utility
#Summary(pl):	Narzêdzie do przesy³ania wiadomo¶ci icq na email
##Version:	%{version}_%{forwarder_ver}
#Group:		Applications/Communications
#Requires:	%{name} = %{version}
#
#%description forwarder
#Licq email forwarder utility.
#
#%description forwarder -l pl
#Narzêdzie do przesy³ania wiadomo¶ci icq na email.

%prep
%setup -q 
#cd plugins/qt-gui/src
#-## KDE m4 macros sucks as hell
#-#for header in *.h; do
#-#	rheader=$(echo ${header} | sed -e 's#\.h##')
#-#	/usr/X11R6/bin/moc -o ${rheader}.moc ${header} || :
#-#done
#cd ../../..
#%patch0 -p1

%build
BASE=$(pwd)
for module in \
	. \
	plugins/console-%{console_ver} \
	plugins/qt-gui-%{qt_gui_ver} \
	plugins/rms-%{rms_ver} \
	plugins/jons-gtk-gui-%{jons_gtk_gui_ver} \
	; do
  cd $module
  %{__autoconf}
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
%{__make} -C plugins/console-%{console_ver}		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/jons-gtk-gui-%{jons_gtk_gui_ver}	DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/qt-gui-%{qt_gui_ver}		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/rms-%{rms_ver}			DESTDIR=$RPM_BUILD_ROOT install
#%{__make} -C plugins/auto-reply			DESTDIR=$RPM_BUILD_ROOT install
#%{__make} -C plugins/email				DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/licq-qt_gui.desktop

#mv -f plugins/email/README		doc/README.FORWARDER
cp -f plugins/rms-%{rms_ver}/README			doc/README.RMS
cp -f plugins/console-%{console_ver}/README		doc/README.CONSOLE
cp -f plugins/jons-gtk-gui-%{jons_gtk_gui_ver}/TODO	doc/README.TODO.JONS-GTK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,README*,TODO} README*
%doc upgrade/* plugins/qt-gui-%{qt_gui_ver}/doc/{CHANGELOG,README,*.HOWTO,HINTS}
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
%doc plugins/qt-gui-%{qt_gui_ver}/doc/*
%attr(755,root,root) %{_libdir}/licq/licq_qt-gui*
%{_applnkdir}/Network/Communications/licq-qt_gui.desktop
%{_datadir}/licq/qt-gui/*.*
%dir %{_datadir}/licq/qt-gui/locale
%lang(cs) %{_datadir}/licq/qt-gui/locale/cs*.qm
%lang(de) %{_datadir}/licq/qt-gui/locale/de.qm
%lang(es) %{_datadir}/licq/qt-gui/locale/es.qm
%lang(fr) %{_datadir}/licq/qt-gui/locale/fr.qm
%lang(it) %{_datadir}/licq/qt-gui/locale/it.qm
%lang(ja) %{_datadir}/licq/qt-gui/locale/ja_JP.eucJP.qm
%lang(pl) %{_datadir}/licq/qt-gui/locale/pl.qm
%lang(pt) %{_datadir}/licq/qt-gui/locale/pt.qm
%lang(ru) %{_datadir}/licq/qt-gui/locale/ru*.qm
%lang(sv) %{_datadir}/licq/qt-gui/locale/sv.qm
%lang(tr) %{_datadir}/licq/qt-gui/locale/tr.qm

%files console
%defattr(644,root,root,755)
%doc doc/README.CONSOLE
%attr(755,root,root) %{_libdir}/licq/licq_console*

#%files forwarder
#%defattr(644,root,root,755)
#%doc doc/README.FORWARDER
#%attr(755,root,root) %{_libdir}/licq/licq_forwarder*

%files rms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/licq/licq_rms*

#%files autoreply
#%defattr(644,root,root,755)
#%doc doc/README.AUTOREPLY
#%attr(755,root,root) %{_libdir}/licq/licq_autoreply*

%files jons-gtk-gui
%defattr(644,root,root,755)
%doc doc/README.TODO.JONS-GTK
%attr(755,root,root) %{_libdir}/licq/licq_jons-gtk-gui*
