Summary:	An ICQ client for online messaging
Summary(pl):	Klient ICQ do przesy³ania wiadomo¶ci po sieci
Name:		licq
Version:	0.85
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.licq.org/
Source0:	http://www.licq.org/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-console.patch
Patch2:		%{name}-qt_gui-translations_not_in_home_dir.patch
BuildRequires:	qt-devel >= 2.1
BuildRequires:	glibc-static
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	XFree86-devel
Requires:	ncurses >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt_gui		qt-gui
%define		auto_reply	auto-reply-0.17
%define		console		console-0.30
%define		forwarder	forwarder-0.66
%define		rms		rms-0.10

%description
Licq is an ICQ online messaging system clone, written in C++. Licq
supports all of the major features of ICQ, including messaging, URLs,
chat, file transfer, and white pages information. Additionally, Licq
is very configurable and supports skins and different icon packs.

%description -l pl
Licq jest klonem systemu przesy³ania wiadomo¶ci ICQ, napisanym w jêzyku
C++. Licq ma wszystkie wa¿ne cechy oryginalnego klienta ICQ, w³±cznie z
przesy³aniem wiadomo¶ci, URLi, rozmow± na ¿ywo, przesy³aniem plików oraz
dostêpem do informacji z "bia³ych stron" ICQ. Dodatkowo, Licq jest bardzo
dobrze konfigurowalny, pozwalaj±c na u¿ywanie "skórek" oraz ró¿nych
zestawów ikon.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl):	Pliki nag³ówkowe niezbêdne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag³ówkowe niezbêdne przy pisaniu wtyczek dla licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(pl):	Graficzne ¶rodowisko u¿ytkownika dla Licq, wykorzystuj±ce Qt
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u¿ywaj±cy widgetów Qt.

%package console
Summary:	Console user interface for Licq
Summary(pl):	Konsolowy interfejs u¿ytkownika dla Licq
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}
Requires:	ncurses >= 5.0

%description console
This package contains console user interface for Licq, using ncurses
library.

%description console -l pl
Ten pakiet zawiera konsolowy interfejs dla Licq, u¿ywaj±cy biblioteki
ncurses.

%package forwarder
Summary:	Licq forwarding utility
Summary(pl):	Narzêdzie do przekazywania dalej otrzymanych w Licq wiadomo¶ci
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description forwarder
This package contains Licq module, that allows to forward any received ICQ
message, either as mail (using SMTP), or as ICQ messages directed to some
other recipients.

%description forwarder -l pl
Ten pakiet zawiera modu³ dla Licq umo¿liwiaj±cy przekazywanie dalej
wiadomo¶ci otrzymanych przez ICQ, w postaci maili (przez SMTP) lub jako
wiadomo¶ci ICQ skierowanych do innych adresatów.

%package rms
Summary:	Licq remote management server
Summary(pl):	Server do zdalnego zarz±dzania Licq
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Requires:	%{name} = %{version}

%description rms
This package contains remote management server for Licq

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz±dzania dla Licq

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
LDFLAGS="-s"; export LDFLAGS

aclocal
%configure
make

cd plugins/%{qt_gui}
aclocal
%configure
%{__make}

cd ../%{console}
aclocal
%configure
%{__make}

cd ../%{forwarder}
aclocal
%configure
%{__make}

cd ../%{rms}
aclocal
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/%{qt_gui} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/%{console} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/%{forwarder} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C plugins/%{rms} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Networking/ICQ
mv plugins/%{console}/README doc/README.CONSOLE
mv plugins/%{forwarder}/README doc/README.FORWARDER
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/ICQ/licq.desktop

gzip -9nf doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,README*,TODO} \
	plugins/%{qt_gui}/doc/{CHANGELOG,README,*.HOWTO,HINTS} \
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
%doc plugins/%{qt_gui}/doc/*.gz
%attr(755,root,root) %{_libdir}/licq/licq_qt-gui*
%{_applnkdir}/Networking/ICQ/licq.desktop
%{_datadir}/licq/qt-gui/dock.*
%{_datadir}/licq/qt-gui/icons.*
%{_datadir}/licq/qt-gui/skin.*
%dir %{_datadir}/licq/qt-gui/locale
%lang(cs) %{_datadir}/licq/qt-gui/locale/cs.qm
%lang(cs) %{_datadir}/licq/qt-gui/locale/cs_CZ.qm
%lang(de) %{_datadir}/licq/qt-gui/locale/de.qm
%lang(es) %{_datadir}/licq/qt-gui/locale/es.qm
%lang(it) %{_datadir}/licq/qt-gui/locale/it.qm
%lang(pl) %{_datadir}/licq/qt-gui/locale/pl.qm
%lang(pt) %{_datadir}/licq/qt-gui/locale/pt.qm
%lang(ru) %{_datadir}/licq/qt-gui/locale/ru.qm
%lang(ru) %{_datadir}/licq/qt-gui/locale/ru_RU.KOI8-R.qm

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
