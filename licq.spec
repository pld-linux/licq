Summary:	An ICQ client for online messaging
Summary(es):	licq es un clone del ICQ(tm) escrito
Summary(pl):	Klient ICQ do przesy�ania wiadomo�ci po sieci
Summary(pt_BR):	O licq � um clone do ICQ(tm) escrito
Summary(ru):	���� ICQ ��� ���������� ������ �����������
Summary(uk):	���� ICQ ��� ���������� ��ͦ�� ��צ����������
Name:		licq
Version:	1.2.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/licq/%{name}-%{version}.tar.bz2
# Source0-md5:	e331c88151b95330f0b9b08570853318
Source1:	%{name}-qt-gui.desktop
Patch0:		%{name}-c++.patch
URL:		http://www.licq.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	kdelibs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7d
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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}
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

%package kde-gui
Summary:	KDE GUI for Licq
Summary(pl):	Graficzny interfejs KDE dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	qt >= 2.1

%description kde-gui
This package contains graphical interface for Licq, using KDE wigets.

%description kde-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, u�ywaj�cy widget�w
KDE.

%package text
Summary:	Text terminal user interface for Licq
Summary(pl):	Interfejs u�ytkownika dla Licq pod terminal tekstowy
Summary(pt_BR):	Interface de usu�rio de console para o licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
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

#%package jons-gtk-gui
#Summary:	Jons GTK GUI for Licq
#Summary(pl):	Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK
#Group:		Applications/Communications
#Requires:	%{name} = %{version}

#%description jons-gtk-gui
#Jons GTK GUI for Licq.
#
#%description jons-gtk-gui -l pl
#Graficzne �rodowisko u�ytkownika dla Licq, wykorzystuj�ce GTK.

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz�dzania Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz�dzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl):	Narz�dzie do automatycznego odpowiadania dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl
Ten pakiet zawiera narz�dzie dla Licq kt�re automatycznie zajmuje si�
przychodz�cymi wiadomo�ciami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl):	Narz�dzie do przesy�ania wiadomo�ci icq na email
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl
Narz�dzie do przesy�ania wiadomo�ci icq na email.

%prep
%setup -q

find . -type d -name autom4te.cache | xargs rm -rf

%build
cp -r plugins/qt-gui plugins/kde-gui
BASE=$(pwd)
for module in \
	. \
	plugins/auto-reply \
	plugins/console \
	plugins/email \
	plugins/qt-gui \
	plugins/kde-gui \
	plugins/rms \
	; do
	# plugins/jons-gtk-gui \
  cd $module
  cp -f /usr/share/automake/config.* admin
  %{__autoconf}
  %configure \
	`[ "$module" = "plugins/qt-gui" ] && echo -n "--with-qt-libraries=%{_libdir}"` \
	`[ "$module" = "plugins/kde-gui" ] && echo -n "--with-kde --with-qt-libraries=%{_libdir}"` \
  	--with-openssl-inc=%{_includedir}/openssl
  %{__make}
  cd $BASE
done

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT install

for d in plugins/{auto-reply,console,email,qt-gui,kde-gui,rms} ; do
# plugins/jons-gtk-gui
	%{__make} -C $d install \
		DESTDIR=$RPM_BUILD_ROOT
done

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/licq-qt_gui.desktop

cp -f plugins/email/README		doc/README.FORWARDER
cp -f plugins/rms/README		doc/README.RMS
cp -f plugins/console/README		doc/README.CONSOLE
#cp -f plugins/jons-gtk-gui/TODO		doc/README.TODO.JONS-GTK
cp -f plugins/auto-reply/README		doc/README.AUTOREPLY

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
%{_desktopdir}/licq-qt_gui.desktop
%dir %{_datadir}/licq/qt-gui
%{_datadir}/licq/qt-gui/*.*
%dir %{_datadir}/licq/qt-gui/locale
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

%files kde-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/licq/licq_kde-gui*

%files text
%defattr(644,root,root,755)
%doc doc/README.CONSOLE
%attr(755,root,root) %{_libdir}/licq/licq_console*

%files forwarder
%defattr(644,root,root,755)
%doc doc/README.FORWARDER
%attr(755,root,root) %{_libdir}/licq/licq_forwarder*

%files rms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/licq/licq_rms*

%files autoreply
%defattr(644,root,root,755)
%doc doc/README.AUTOREPLY
%attr(755,root,root) %{_libdir}/licq/licq_autoreply*

#%files jons-gtk-gui
#%defattr(644,root,root,755)
#%doc doc/README.TODO.JONS-GTK
#%attr(755,root,root) %{_libdir}/licq/licq_jons-gtk-gui*
