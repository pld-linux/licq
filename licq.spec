
%define		_snap	20021116

Summary:	An ICQ client for online messaging
Summary(es):	licq es un clone del ICQ(tm) escrito
Summary(pl):	Klient ICQ do przesy�ania wiadomo�ci po sieci
Summary(pt_BR):	O licq � um clone do ICQ(tm) escrito
Summary(ru):	���� ICQ ��� ���������� ������ �����������
Summary(uk):	���� ICQ ��� ���������� ��ͦ�� ��צ����������
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

%description -l es
licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt. Es
un intento de dar a los usuarios de Linux una opci�n no-java para el
protocolo ICQ.

%description -l pl
Licq jest klonem systemu przesy�ania wiadomo�ci ICQ, napisanym w
j�zyku C++. Licq ma wszystkie wa�ne cechy oryginalnego klienta ICQ,
w��cznie z przesy�aniem wiadomo�ci, URLi, rozmow� na �ywo,
przesy�aniem plik�w oraz dost�pem do informacji z "bia�ych stron" ICQ.
Dodatkowo, Licq jest bardzo dobrze konfigurowalny, pozwalaj�c na
u�ywanie "sk�rek" oraz r�nych zestaw�w ikon.

%description -l pt_BR
O licq � um clone do ICQ(tm) escrito em c++ usando biblioteca Qt. �
uma tentativa de dar aos usu�rios do Linux uma op��o n�o-java para o
protocolo ICQ.

%description -l ru
Licq - ��� ���� ������� ����������� ������ ���������� ICQ, ����������
�� C++ � �������������� ������ �������� Qt. Licq ������������ ���
�������� ����������� ICQ, ������� ����� �����������, URL�, ���,
��������� ������ � ���������� �� ����������. ������������� � �����,
Licq ����� ������� ����������� ���������������� � ������������ "�����"
(������� ����������� ��� ������ ������ ���������� ��� ����� ��������
����) � ������ ������ ������.

%description -l uk
Licq - �� ���� ������� ����������� ��ͦ�� ��צ���������� ICQ,
��������� �� C++ � ������������� ������ צ���Ԧ� Qt. Licq Ц�����դ
�Ӧ ��������Φۦ ��������Ԧ ICQ, ��������� ��ͦ� ��צ����������, URL�,
���, ��������� ���̦� �� �������æ� ��� ������˦�. ��������� �� �����,
Licq ��� ����Ԧ ��������Ԧ ���Ʀ��������� � Ц�����դ "�˦��" (�ͦ�Φ
���������� ��� Ҧ���� ������ ���������� ��� �ͦ�� ���Φ������ �������)
�� Ҧ�Φ ������ ������.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl):	Pliki nag��wkowe niezb�dne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag��wkowe niezb�dne przy pisaniu wtyczek dla licq.

%description devel -l pt_BR
Ferramentas para desenvolvimento de plug-ins para o licq.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es):	QT user interface for licq
Summary(pl):	Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce Qt
Summary(pt_BR):	Interface QT para o licq
Summary(ru):	Qt ��������� � licq
Summary(uk):	Qt ��������� �� licq
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u�ywaj�cy widget�w
Qt.

%description qt-gui -l uk
Licq - �� ���� ������� ����������� ��ͦ�� ��צ���������� ICQ.
%{name}-qt - �� ���Ʀ���� ��������� �� licq ��������� �� Qt.

%description qt-gui -l ru
Licq - ��� ���� ������� ����������� ������ ���������� ICQ. %{name}-qt
- ��� ����������� ��������� � licq ���������� �� Qt.

%package text
Summary:	Text terminal user interface for Licq
Summary(pl):	Interfejs u�ytkownika dla Licq pod terminal tekstowy
Summary(pt_BR):	Interface de usu�rio de console para o licq
Group:		Applications/Communications
Requires:	%{name} = %{version}
Requires:	ncurses >= 5.0
Obsoletes:	licq-console

%description text
This package contains text terminal user interface for Licq, using
ncurses library.

%description text -l pl
Ten pakiet zawiera interfejs dla Licq pod terminal tekstowy u�ywaj�cy
biblioteki ncurses.

%description text -l pt_BR
Inclui interface de usu�rio de console para o licq.

%description text -l ru
Licq - ��� ���� ������� ����������� ������ ���������� ICQ. %{name}-qt
- ��� ��������� ��������� � licq.

%description text -l uk
Licq - �� ���� ������� ����������� ��ͦ�� ��צ���������� ICQ.
%{name}-qt - �� ��������� ��������� �� licq.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl):	Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl
Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK.

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz�dzania Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz�dzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl):	Narz�dzie do automatycznego odpowiadania dla Licq
Version:	%{version}
Group:		Applications/Communications
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
Version:	%{version}
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl
Narz�dzie do przesy�ania wiadomo�ci icq na email.

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
