
%define		_snap	20021116

Summary:	An ICQ client for online messaging
Summary(es.UTF-8):   licq es un clone del ICQ(tm) escrito
Summary(pl.UTF-8):   Klient ICQ do przesyłania wiadomości po sieci
Summary(pt_BR.UTF-8):   O licq é um clone do ICQ(tm) escrito
Summary(ru.UTF-8):   Клон ICQ для онлайновго обмена сообщениями
Summary(uk.UTF-8):   Клон ICQ для онлайновго обміну повідомленнями
Name:		licq
Version:	1.2.2
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications/Communications
#Source0:	ftp://ftp2.sourceforge.net/pub/sourceforge/licq/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{_snap}.tar.bz2
Source1:	%{name}-qt-gui.desktop
Patch0:		%{name}-c++.patch
URL:		http://www.licq.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Licq is an ICQ online messaging system clone, written in C++. Licq
supports all of the major features of ICQ, including messaging, URLs,
chat, file transfer, and white pages information. Additionally, Licq
is very configurable and supports skins and different icon packs.

%description -l es.UTF-8
licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt. Es
un intento de dar a los usuarios de Linux una opción no-java para el
protocolo ICQ.

%description -l pl.UTF-8
Licq jest klonem systemu przesyłania wiadomości ICQ, napisanym w
języku C++. Licq ma wszystkie ważne cechy oryginalnego klienta ICQ,
włącznie z przesyłaniem wiadomości, URLi, rozmową na żywo,
przesyłaniem plików oraz dostępem do informacji z "białych stron" ICQ.
Dodatkowo, Licq jest bardzo dobrze konfigurowalny, pozwalając na
używanie "skórek" oraz różnych zestawów ikon.

%description -l pt_BR.UTF-8
O licq é um clone do ICQ(tm) escrito em c++ usando biblioteca Qt. É
uma tentativa de dar aos usuários do Linux uma opção não-java para o
protocolo ICQ.

%description -l ru.UTF-8
Licq - это клон системы онлайнового обмена сообщенями ICQ, написанный
на C++ с использованием набора виджетов Qt. Licq поддерживает все
основные возможности ICQ, включая обмен сообщениями, URLы, чат,
пересылку файлов и информацию об участниках. Дополнительно к этому,
Licq имеет богатые возможности конфигурирования и поддерживает "скины"
(сменные изображения для разных частей интерфейса для смены внешнего
вида) и разные наборы иконок.

%description -l uk.UTF-8
Licq - це клон системи онлайнового обміну повідомленнями ICQ,
написаний на C++ з використанням набору віджетів Qt. Licq підтримує
всі найголовніші можливості ICQ, включаючи обмін повідомленнями, URLи,
чат, пересилку файлів та інформацію про учасників. Додатково до цього,
Licq має багаті можливості конфігурування і підтримує "скіни" (змінні
зображення для різних частин інтерфейсу для зміни зовнішнього вигляду)
та різні набори іконок.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl.UTF-8):   Pliki nagłówkowe niezbędne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required to develop licq plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne przy pisaniu wtyczek dla licq.

%description devel -l pt_BR.UTF-8
Ferramentas para desenvolvimento de plug-ins para o licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es.UTF-8):   QT user interface for licq
Summary(pl.UTF-8):   Graficzne środowisko użytkownika dla Licq, wykorzystujące Qt
Summary(pt_BR.UTF-8):   Interface QT para o licq
Summary(ru.UTF-8):   Qt интерфейс к licq
Summary(uk.UTF-8):   Qt інтерфейс до licq
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description qt-gui -l pl.UTF-8
Ten pakiet zawiera graficzny interfejs dla Licq, używający widgetów
Qt.

%description qt-gui -l uk.UTF-8
Licq - це клон системи онлайнового обміну повідомленнями ICQ.
%{name}-qt - це графічний інтерфейс до licq написаний на Qt.

%description qt-gui -l ru.UTF-8
Licq - это клон системы онлайнового обмена сообщенями ICQ. %{name}-qt
- это графический интерфейс к licq написанный на Qt.

%package text
Summary:	Text terminal user interface for Licq
Summary(pl.UTF-8):   Interfejs użytkownika dla Licq pod terminal tekstowy
Summary(pt_BR.UTF-8):   Interface de usuário de console para o licq
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	ncurses >= 5.0
Obsoletes:	licq-console

%description text
This package contains text terminal user interface for Licq, using
ncurses library.

%description text -l pl.UTF-8
Ten pakiet zawiera interfejs dla Licq pod terminal tekstowy używający
biblioteki ncurses.

%description text -l pt_BR.UTF-8
Inclui interface de usuário de console para o licq.

%description text -l ru.UTF-8
Licq - это клон системы онлайнового обмена сообщенями ICQ. %{name}-qt
- это текстовый интерфейс к licq.

%description text -l uk.UTF-8
Licq - це клон системи онлайнового обміну повідомленнями ICQ.
%{name}-qt - це текстовий інтерфейс до licq.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl.UTF-8):   Graficzne środowisko użytkownika dla Licq, wykorzystujące GTK
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl.UTF-8
Graficzne środowisko użytkownika dla Licq, wykorzystujące GTK.

%package rms
Summary:	Licq remote management server
Summary(pl.UTF-8):   Serwer do zdalnego zarządzania Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description rms
This package contains remote management server for Licq.

%description rms -l pl.UTF-8
Ten pakiet zawiera serwer do zdalnego zarządzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl.UTF-8):   Narzędzie do automatycznego odpowiadania dla Licq
Version:	%{version}
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl.UTF-8
Ten pakiet zawiera narzędzie dla Licq które automatycznie zajmuje się
przychodzącymi wiadomościami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl.UTF-8):   Narzędzie do przesyłania wiadomości icq na email
Version:	%{version}
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl.UTF-8
Narzędzie do przesyłania wiadomości icq na email.

%prep
%setup -q -n %{name}-%{_snap}

%build
BASE=$(pwd)
for module in \
	. \
	plugins/console \
	plugins/qt-gui \
	plugins/rms \
	plugins/jons-gtk-gui \
	plugins/auto-reply \
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
%{__make} -C plugins/console		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/jons-gtk-gui	DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/qt-gui		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/rms		DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/auto-reply		DESTDIR=$RPM_BUILD_ROOT install
#%{__make} -C plugins/email		DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/licq-qt_gui.desktop

#mv -f plugins/email/README		doc/README.FORWARDER
cp -f plugins/rms/README		doc/README.RMS
cp -f plugins/console/README		doc/README.CONSOLE
cp -f plugins/jons-gtk-gui/TODO		doc/README.TODO.JONS-GTK
cp -f plugins/autoreply/README		doc/README.autoreply

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,README*,TODO} README*
%doc upgrade/* plugins/qt-gui/doc/{CHANGELOG,README,*.HOWTO,HINTS}
%attr(755,root,root) %{_bindir}/licq
%attr(755,root,root) %{_bindir}/viewurl-*
%dir %{_libdir}/licq
%dir %{_datadir}/licq
%{_datadir}/licq/sounds
%{_datadir}/licq/translations
%{_datadir}/licq/utilities

%files devel
%defattr(644,root,root,755)
%{_includedir}/licq

%files qt-gui
%defattr(644,root,root,755)
%doc plugins/qt-gui/doc/*
%attr(755,root,root) %{_libdir}/licq/licq_qt-gui*
%{_applnkdir}/Network/Communications/licq-qt_gui.desktop
%dir %{_datadir}/licq/qt-gui
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

%files text
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

%files autoreply
%defattr(644,root,root,755)
%doc doc/README.AUTOREPLY
%attr(755,root,root) %{_libdir}/licq/licq_autoreply*

%files jons-gtk-gui
%defattr(644,root,root,755)
%doc doc/README.TODO.JONS-GTK
%attr(755,root,root) %{_libdir}/licq/licq_jons-gtk-gui*
