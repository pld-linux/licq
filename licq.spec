# TODO:
#	- subpackage with licqweb
Summary:	An ICQ client for online messaging
Summary(es):	licq es un clone del ICQ(tm) escrito
Summary(pl):	Klient ICQ do przesy≥ania wiadomo∂ci po sieci
Summary(pt_BR):	O licq È um clone do ICQ(tm) escrito
Summary(ru):	ÎÃœŒ ICQ ƒÃ— œŒÃ¡ Œœ◊«œ œ¬Õ≈Œ¡ ”œœ¬›≈Œ…—Õ…
Summary(uk):	ÎÃœŒ ICQ ƒÃ— œŒÃ¡ Œœ◊«œ œ¬Õ¶Œ’ –œ◊¶ƒœÕÃ≈ŒŒ—Õ…
Name:		licq
Version:	1.3.2
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/licq/%{name}-%{version}.tar.bz2
# Source0-md5:	0471bb8fed91eefb23dfe153c9a4a806
Source1:	%{name}-qt-gui.desktop
Source2:	%{name}-kde-gui.desktop
Patch0:		%{name}-typos.patch
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
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	qt-linguist
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# "lib" instead of "%{_lib}" is hardcoded in include/licq_constants.h
# and plugins/*/src/Makefile.am
%define		plugindir	%{_prefix}/lib/licq

# __cc with words broken
%undefine	with_ccache

%description
Licq is an ICQ online messaging system clone, written in C++. Licq
supports all of the major features of ICQ, including messaging, URLs,
chat, file transfer, and white pages information. Additionally, Licq
is very configurable and supports skins and different icon packs.

%description -l es
licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt. Es
un intento de dar a los usuarios de Linux una opciÛn no-java para el
protocolo ICQ.

%description -l pl
Licq jest klonem systemu przesy≥ania wiadomo∂ci ICQ, napisanym w
jÍzyku C++. Licq ma wszystkie waøne cechy oryginalnego klienta ICQ,
w≥±cznie z przesy≥aniem wiadomo∂ci, URLi, rozmow± na øywo,
przesy≥aniem plikÛw oraz dostÍpem do informacji z "bia≥ych stron" ICQ.
Dodatkowo, Licq jest bardzo dobrze konfigurowalny, pozwalaj±c na
uøywanie "skÛrek" oraz rÛønych zestawÛw ikon.

%description -l pt_BR
O licq È um clone do ICQ(tm) escrito em c++ usando biblioteca Qt. …
uma tentativa de dar aos usu·rios do Linux uma opÁ„o n„o-java para o
protocolo ICQ.

%description -l ru
Licq - ‹‘œ ÀÃœŒ ”…”‘≈ÕŸ œŒÃ¡ Œœ◊œ«œ œ¬Õ≈Œ¡ ”œœ¬›≈Œ—Õ… ICQ, Œ¡–…”¡ŒŒŸ 
Œ¡ C++ ” …”–œÃÿ⁄œ◊¡Œ…≈Õ Œ¡¬œ“¡ ◊…ƒ÷≈‘œ◊ Qt. Licq –œƒƒ≈“÷…◊¡≈‘ ◊”≈
œ”Œœ◊ŒŸ≈ ◊œ⁄Õœ÷Œœ”‘… ICQ, ◊ÀÃ¿ﬁ¡— œ¬Õ≈Œ ”œœ¬›≈Œ…—Õ…, URLŸ, ﬁ¡‘,
–≈“≈”ŸÃÀ’ ∆¡ Ãœ◊ … …Œ∆œ“Õ¡√…¿ œ¬ ’ﬁ¡”‘Œ…À¡». ‰œ–œÃŒ…‘≈ÃÿŒœ À ‹‘œÕ’,
Licq …Õ≈≈‘ ¬œ«¡‘Ÿ≈ ◊œ⁄Õœ÷Œœ”‘… ÀœŒ∆…«’“…“œ◊¡Œ…— … –œƒƒ≈“÷…◊¡≈‘ "”À…ŒŸ"
(”Õ≈ŒŒŸ≈ …⁄œ¬“¡÷≈Œ…— ƒÃ— “¡⁄ŒŸ» ﬁ¡”‘≈  …Œ‘≈“∆≈ ”¡ ƒÃ— ”Õ≈ŒŸ ◊Œ≈€Œ≈«œ
◊…ƒ¡) … “¡⁄ŒŸ≈ Œ¡¬œ“Ÿ …ÀœŒœÀ.

%description -l uk
Licq - √≈ ÀÃœŒ ”…”‘≈Õ… œŒÃ¡ Œœ◊œ«œ œ¬Õ¶Œ’ –œ◊¶ƒœÕÃ≈ŒŒ—Õ… ICQ,
Œ¡–…”¡Œ…  Œ¡ C++ ⁄ ◊…Àœ“…”‘¡ŒŒ—Õ Œ¡¬œ“’ ◊¶ƒ÷≈‘¶◊ Qt. Licq –¶ƒ‘“…Õ’§
◊”¶ Œ¡ «œÃœ◊Œ¶€¶ Õœ÷Ã…◊œ”‘¶ ICQ, ◊ÀÃ¿ﬁ¡¿ﬁ… œ¬Õ¶Œ –œ◊¶ƒœÕÃ≈ŒŒ—Õ…, URL…,
ﬁ¡‘, –≈“≈”…ÃÀ’ ∆¡ Ã¶◊ ‘¡ ¶Œ∆œ“Õ¡√¶¿ –“œ ’ﬁ¡”Œ…À¶◊. ‰œƒ¡‘Àœ◊œ ƒœ √ÿœ«œ,
Licq Õ¡§ ¬¡«¡‘¶ Õœ÷Ã…◊œ”‘¶ ÀœŒ∆¶«’“’◊¡ŒŒ— ¶ –¶ƒ‘“…Õ’§ "”À¶Œ…" (⁄Õ¶ŒŒ¶
⁄œ¬“¡÷≈ŒŒ— ƒÃ— “¶⁄Œ…» ﬁ¡”‘…Œ ¶Œ‘≈“∆≈ ”’ ƒÃ— ⁄Õ¶Œ… ⁄œ◊Œ¶€Œÿœ«œ ◊…«Ã—ƒ’)
‘¡ “¶⁄Œ¶ Œ¡¬œ“… ¶ÀœŒœÀ.

%package devel
Summary:	Header files requied to develop licq plugins
Summary(pl):	Pliki nag≥Ûwkowe niezbÍdne przy pisaniu wtyczek dla licq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files required to develop licq plugins.

%description devel -l pl
Pliki nag≥Ûwkowe niezbÍdne przy pisaniu wtyczek dla licq.

%description devel -l pt_BR
Ferramentas para desenvolvimento de plug-ins para o licq.

%package qt-gui-common
Summary:	Common files for QT based GUI plugins
Summary(pl):	WspÛlne pliki dla wtyczek GUI opartych na QT
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	qt >= 2.1

%description qt-gui-common
Common files for QT based GUI plugins.

%description qt-gui-common -l pl
WspÛlne pliki dla wtyczek GUI opartych na QT.

%package qt-gui
Summary:	Qt GUI for Licq
Summary(es):	Qt user interface for licq
Summary(pl):	Graficzne ∂rodowisko uøytkownika dla Licq, wykorzystuj±ce Qt
Summary(pt_BR):	Interface Qt para o licq
Summary(ru):	Qt …Œ‘≈“∆≈ ” À licq
Summary(uk):	Qt ¶Œ‘≈“∆≈ ” ƒœ licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt-gui-common = %{version}-%{release}
Requires:	qt >= 2.1

%description qt-gui
This package contains graphical interface for Licq, using Qt wigets.

%description qt-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, uøywaj±cy widgetÛw
Qt.

%description qt-gui -l uk
Licq - √≈ ÀÃœŒ ”…”‘≈Õ… œŒÃ¡ Œœ◊œ«œ œ¬Õ¶Œ’ –œ◊¶ƒœÕÃ≈ŒŒ—Õ… ICQ.
%{name}-qt - √≈ «“¡∆¶ﬁŒ…  ¶Œ‘≈“∆≈ ” ƒœ licq Œ¡–…”¡Œ…  Œ¡ Qt.

%description qt-gui -l ru
Licq - ‹‘œ ÀÃœŒ ”…”‘≈ÕŸ œŒÃ¡ Œœ◊œ«œ œ¬Õ≈Œ¡ ”œœ¬›≈Œ—Õ… ICQ. %{name}-qt
- ‹‘œ «“¡∆…ﬁ≈”À…  …Œ‘≈“∆≈ ” À licq Œ¡–…”¡ŒŒŸ  Œ¡ Qt.

%package kde-gui
Summary:	KDE GUI for Licq
Summary(pl):	Graficzny interfejs KDE dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt-gui-common = %{version}-%{release}
Requires:	qt >= 2.1

%description kde-gui
This package contains graphical interface for Licq, using KDE wigets.

%description kde-gui -l pl
Ten pakiet zawiera graficzny interfejs dla Licq, uøywaj±cy widgetÛw
KDE.

%package text
Summary:	Text terminal user interface for Licq
Summary(pl):	Interfejs uøytkownika dla Licq pod terminal tekstowy
Summary(pt_BR):	Interface de usu·rio de console para o licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses >= 5.0
Obsoletes:	licq-console

%description text
This package contains text terminal user interface for Licq, using
ncurses library.

%description text -l pl
Ten pakiet zawiera interfejs dla Licq pod terminal tekstowy uøywaj±cy
biblioteki ncurses.

%description text -l pt_BR
Inclui interface de usu·rio de console para o licq.

%description text -l ru
Licq - ‹‘œ ÀÃœŒ ”…”‘≈ÕŸ œŒÃ¡ Œœ◊œ«œ œ¬Õ≈Œ¡ ”œœ¬›≈Œ—Õ… ICQ. %{name}-qt
- ‹‘œ ‘≈À”‘œ◊Ÿ  …Œ‘≈“∆≈ ” À licq.

%description text -l uk
Licq - √≈ ÀÃœŒ ”…”‘≈Õ… œŒÃ¡ Œœ◊œ«œ œ¬Õ¶Œ’ –œ◊¶ƒœÕÃ≈ŒŒ—Õ… ICQ.
%{name}-qt - √≈ ‘≈À”‘œ◊…  ¶Œ‘≈“∆≈ ” ƒœ licq.

%package jons-gtk-gui
Summary:	Jons GTK GUI for Licq
Summary(pl):	Graficzne ∂rodowisko uøytkownika dla Licq, wykorzystuj±ce GTK
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description jons-gtk-gui
Jons GTK GUI for Licq.

%description jons-gtk-gui -l pl
Graficzne ∂rodowisko uøytkownika dla Licq, wykorzystuj±ce GTK.

%package msn
Summary:	Licq MSN plugin
Summary(pl):	Wtyczka MSN dla licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description msn
Licq MSN plugin.

%description msn -l pl
Wtyczka MSN dla licq.

%package osd
Summary:	On-screen display of incomming messages
Summary(pl):	Wy∂wietlanie przychodz±cych wiadomo∂ci na ekranie (OSD)
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description osd
On-screen display of incomming messages.

%description osd -l pl
Wy∂wietlanie przychodz±cych wiadomo∂ci na ekranie (OSD).

%package rms
Summary:	Licq remote management server
Summary(pl):	Serwer do zdalnego zarz±dzania Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description rms
This package contains remote management server for Licq.

%description rms -l pl
Ten pakiet zawiera serwer do zdalnego zarz±dzania dla Licq.

%package autoreply
Summary:	Licq autoreply utility
Summary(pl):	NarzÍdzie do automatycznego odpowiadania dla Licq
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description autoreply
This package contains Licq utility for automatic handling of incoming
messages.

%description autoreply -l pl
Ten pakiet zawiera narzÍdzie dla Licq ktÛre automatycznie zajmuje siÍ
przychodz±cymi wiadomo∂ciami.

%package forwarder
Summary:	Licq email forwarder utility
Summary(pl):	NarzÍdzie do przesy≥ania wiadomo∂ci icq na email
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description forwarder
Licq email forwarder utility.

%description forwarder -l pl
NarzÍdzie do przesy≥ania wiadomo∂ci icq na email.

%prep
%setup -q
%patch0 -p1

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
