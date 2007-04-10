# TODO:
#	- subpackage with licqweb
Summary:	An ICQ client for online messaging
Summary(es.UTF-8):	licq es un clone del ICQ(tm) escrito
Summary(pl.UTF-8):	Klient ICQ do przesyłania wiadomości po sieci
Summary(pt_BR.UTF-8):	O licq é um clone do ICQ(tm) escrito
Summary(ru.UTF-8):	Клон ICQ для онлайновго обмена сообщениями
Summary(uk.UTF-8):	Клон ICQ для онлайновго обміну повідомленнями
Name:		licq
Version:	1.3.4
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/licq/%{name}-%{version}.tar.bz2
# Source0-md5:	3bab0c9d1977f9b14421d36110e17e0c
Source1:	%{name}-qt-gui.desktop
Source2:	%{name}-kde-gui.desktop
URL:		http://www.licq.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	cdk-devel >= 5.0
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	kdelibs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-devel >= 3:3.0.5
BuildRequires:	qt-linguist
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_libdir}/licq

# __cc with words broken
%undefine	with_ccache

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
Summary(pl.UTF-8):	Pliki nagłówkowe niezbędne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files required to develop licq plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne przy pisaniu wtyczek dla licq.

%description devel -l pt_BR.UTF-8
Ferramentas para desenvolvimento de plug-ins para o licq.

%package qt-gui-common
Summary:	Common files for QT based GUI plugins
Summary(pl.UTF-8):	Wspólne pliki dla wtyczek GUI opartych na QT
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	qt >= 2.1

%description qt-gui-common
Common files for QT based GUI plugins.

%description qt-gui-common -l pl.UTF-8
Wspólne pliki dla wtyczek GUI opartych na QT.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es.UTF-8):	Qt user interface for licq
Summary(pl.UTF-8):	Graficzne środowisko użytkownika dla Licq, wykorzystujące Qt
Summary(pt_BR.UTF-8):	Interface Qt para o licq
Summary(ru.UTF-8):	Qt интерфейс к licq
Summary(uk.UTF-8):	Qt інтерфейс до licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt-gui-common = %{version}-%{release}
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

%package kde-gui
Summary:	KDE GUI for Licq
Summary(pl.UTF-8):	Graficzny interfejs KDE dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt-gui-common = %{version}-%{release}
Requires:	qt >= 2.1

%description kde-gui
This package contains graphical interface for Licq, using KDE wigets.

%description kde-gui -l pl.UTF-8
Ten pakiet zawiera graficzny interfejs dla Licq, używający widgetów
KDE.

%package text
Summary:	Text terminal user interface for Licq
Summary(pl.UTF-8):	Interfejs użytkownika dla Licq pod terminal tekstowy
Summary(pt_BR.UTF-8):	Interface de usuário de console para o licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
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
Summary:	Jons GTK+ GUI for Licq
Summary(pl.UTF-8):	Graficzne środowisko użytkownika dla Licq, wykorzystujące GTK+
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description jons-gtk-gui
Jons GTK+ GUI for Licq.

%description jons-gtk-gui -l pl.UTF-8
Graficzne środowisko użytkownika dla Licq, wykorzystujące GTK+.

%package msn
Summary:	Licq MSN plugin
Summary(pl.UTF-8):	Wtyczka MSN dla licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description msn
Licq MSN plugin.

%description msn -l pl.UTF-8
Wtyczka MSN dla licq.

%package osd
Summary:	On-screen display of incomming messages
Summary(pl.UTF-8):	Wyświetlanie przychodzących wiadomości na ekranie (OSD)
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description osd
On-screen display of incomming messages.

%description osd -l pl.UTF-8
Wyświetlanie przychodzących wiadomości na ekranie (OSD).

%package rms
Summary:	Licq remote management server
Summary(pl.UTF-8):	Serwer do zdalnego zarządzania Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description rms
This package contains remote management server for Licq.

%description rms -l pl.UTF-8
Ten pakiet zawiera serwer do zdalnego zarządzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl.UTF-8):	Narzędzie do automatycznego odpowiadania dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl.UTF-8
Ten pakiet zawiera narzędzie dla Licq które automatycznie zajmuje się
przychodzącymi wiadomościami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl.UTF-8):	Narzędzie do przesyłania wiadomości icq na email
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl.UTF-8
Narzędzie do przesyłania wiadomości icq na email.

%prep
%setup -q

find . -type d -name autom4te.cache | xargs rm -rf

%build
cp -pr plugins/qt-gui plugins/kde-gui
BASE=$(pwd)
for module in \
	. \
	plugins/auto-reply \
	plugins/console \
	plugins/email \
	plugins/msn \
	plugins/osd \
	plugins/kde-gui \
	plugins/qt-gui \
	plugins/rms \
	; do
	# plugins/jons-gtk-gui \
	cd $module
	cp -f /usr/share/automake/config.* admin
	%configure \
	$([ "$module" = "plugins/qt-gui" ] && echo -n "--with-qt-libraries=%{_libdir}") \
	$([ "$module" = "plugins/kde-gui" ] && echo -n "--with-kde --with-qt-libraries=%{_libdir} KDEDIR=%{_libdir}") \
	--with-openssl-inc=%{_includedir}/openssl \
	--enable-gpgme
	%{__make}
	cd $BASE
done

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for d in plugins/{auto-reply,console,email,msn,osd,kde-gui,qt-gui,rms} ; do
# plugins/jons-gtk-gui
	%{__make} -C $d install \
		DESTDIR=$RPM_BUILD_ROOT
done

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/licq-qt_gui.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/licq-kde_gui.desktop

cp -f plugins/auto-reply/README		doc/README.AUTOREPLY
cp -f plugins/console/README		doc/README.CONSOLE
cp -f plugins/email/README		doc/README.FORWARDER
cp -f plugins/msn/README		doc/README.MSN
cp -f plugins/osd/README		doc/README.OSD
cp -f plugins/rms/README		doc/README.RMS
#cp -f plugins/jons-gtk-gui/TODO		doc/README.TODO.JONS-GTK
cp -f doc/README			doc/README2

# dlopened by *.so
rm -f $RPM_BUILD_ROOT%{plugindir}/*.la

%find_lang %{name}
%find_lang %{name}_osd_plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,TODO} README
%doc doc/README{2,-0.70-0.71,-0.61-0.70,-1.2.0,-1.3.0,.CodingStyle,.FIFO,.SOCKS}
%doc upgrade/*
%attr(755,root,root) %{_bindir}/licq
%attr(755,root,root) %{_bindir}/viewurl-*
%dir %{plugindir}
%dir %{_datadir}/licq
%{_datadir}/licq/sounds
%{_datadir}/licq/translations
%{_datadir}/licq/utilities

%files devel
%defattr(644,root,root,755)
%{_includedir}/licq

%files qt-gui-common
%defattr(644,root,root,755)
%doc plugins/qt-gui/doc/*
%dir %{_datadir}/licq/qt-gui
%{_datadir}/licq/qt-gui/*.*
%{_datadir}/licq/qt-gui/emoticons
%dir %{_datadir}/licq/qt-gui/locale
%lang(be) %{_datadir}/licq/qt-gui/locale/be*.qm
%lang(bg) %{_datadir}/licq/qt-gui/locale/bg*.qm
%lang(cs) %{_datadir}/licq/qt-gui/locale/cs*.qm
%lang(de) %{_datadir}/licq/qt-gui/locale/de.qm
%lang(es) %{_datadir}/licq/qt-gui/locale/es.qm
%lang(fi) %{_datadir}/licq/qt-gui/locale/fi.qm
%lang(fr) %{_datadir}/licq/qt-gui/locale/fr.qm
%lang(hu) %{_datadir}/licq/qt-gui/locale/hu_HU.qm
%lang(it) %{_datadir}/licq/qt-gui/locale/it.qm
%lang(ja) %{_datadir}/licq/qt-gui/locale/ja_JP.eucJP.qm
%lang(pl) %{_datadir}/licq/qt-gui/locale/pl.qm
%lang(pt) %{_datadir}/licq/qt-gui/locale/pt.qm
%lang(pt_BR) %{_datadir}/licq/qt-gui/locale/pt_BR.qm
%lang(ru) %{_datadir}/licq/qt-gui/locale/ru*.qm
%lang(sr) %{_datadir}/licq/qt-gui/locale/sr.qm
%lang(sv) %{_datadir}/licq/qt-gui/locale/sv.qm
%lang(tr) %{_datadir}/licq/qt-gui/locale/tr.qm
%lang(uk) %{_datadir}/licq/qt-gui/locale/uk.qm

%files qt-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/licq_qt-gui.so
%{_desktopdir}/licq-qt_gui.desktop

%files kde-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/licq_kde-gui.so
%{_desktopdir}/licq-kde_gui.desktop

%files text
%defattr(644,root,root,755)
%doc doc/README.CONSOLE
%attr(755,root,root) %{plugindir}/licq_console.so

%files forwarder
%defattr(644,root,root,755)
%doc doc/README.FORWARDER
%attr(755,root,root) %{plugindir}/licq_forwarder.so

%files msn
%defattr(644,root,root,755)
%doc doc/README.MSN
%attr(755,root,root) %{plugindir}/protocol_msn.so

%files osd -f %{name}_osd_plugin.lang
%defattr(644,root,root,755)
%doc doc/README.OSD
%attr(755,root,root) %{plugindir}/licq_osd.so

%files rms
%defattr(644,root,root,755)
%doc doc/README.RMS
%attr(755,root,root) %{plugindir}/licq_rms.so

%files autoreply
%defattr(644,root,root,755)
%doc doc/README.AUTOREPLY
%attr(755,root,root) %{plugindir}/licq_autoreply.so

#%files jons-gtk-gui
#%defattr(644,root,root,755)
#%doc doc/README.TODO.JONS-GTK
#%attr(755,root,root) %{plugindir}/licq_jons-gtk-gui.so
