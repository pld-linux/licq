
%define		qt_gui_ver	0.71
%define		con_gui_ver	0.20
%define		data_ver	1.5

Summary:	Licq - ICQ clone.
Summary(pl):	Licq - klient ICQ.
Name:		licq
Version:	0.76
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://download.sourceforge.net/licq/%{name}-%{version}.tar.gz
Source1:	http://download.sourceforge.net/licq/%{name}-data-%{data_ver}.tar.gz
Source2:	licq.wmconfig
Source3:	licq.mini-icon.xpm
Source4:	http://www.crewq.com/licq/icons/icons-dots.tar.gz
URL:		http://www.licq.org/
BuildRequires:	libstdc++-devel
BuildRequires:	gettext-devel
BuildRequires:	qt-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Licq is an ICQ clone written fully in c++ using the Qt widget set. It is an
attempt to give linux a non-java option to the ICQ protocol, as the java
version is unstable and a memory hog.

%description -l pl
Licq jest klientem ICQ napisanym w C++ przy u¿yciu biblioteki Qt. Pozwala
zast±piæ, napisanego w Javie, klienta ICQ z Mirabilis, który potrzebuje do
pracy zbyt wiele zasobów i wymaga zainstalowanego jdk.

%package	devel
Summary:	Header files for compile licq plugins
Summary(pl):	Pliki nag³ówkowe do kompilacji wtyczek licq
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	licq

%description devel
Header files for compile licq plugins.

%description devel -l pl
Pliki nag³ówkowe do kompilacji wtyczek licq.

%package	qt-gui
Summary:	Qt GUI for Licq
Summary(pl):	Interfejs graficzny Qt dla Licq
Group:		X11/Applications/Communications
Group(pl):	X11/Aplikacje/Komunikacja
Requires:	licq = %{version}
Requires:	qt >= 2.0

%description qt-gui
Graphical user interface for Licq written using Qt library

%description qt-gui -l pl
Graficzny interfejs u¿ytkownika do Licq pisany przy u¿yciu biblioteki Qt

%package	console
Summary:	Console user interface for Licq
Summary(pl):	Konsolowy interfejs u¿ytkownika dla Licq
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Requires:	licq = %{version}
Requires:	ncurses >= 5.0

%description console
Console user interface for Licq

%description console -l pl
Konsolowy interfejs u¿ytkownika dla Licq

%prep
%setup -q 

%build
LDFLAGS="-s"; export LDFLAGS
aclocal
autoconf
autoheader
automake
%configure 
make

cd plugins

cd qt-gui-%{qt_gui_ver}
gettextize --copy --force
%configure
make
cd ..

cd console-%{con_gui_ver}
aclocal
autoconf
autoheader
automake
%configure
make
cd ..

cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_includedir}/%{name}}

cd qt-gui-%{qt_gui_ver}
make \
	DESTDIR=$RPM_BUILD_ROOT \
	install
	
cd ..
%find_lang Licq-Qt-GUI
cd ..

make \
	DESTDIR=$RPM_BUILD_ROOT \
	install

install src/inc/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%files -f Licq-Qt-GUI.lang
%defattr(644,root,root,755)
%doc ../doc/BUGS ../doc/CHANGELOG ../doc/CREDITS ../doc/FAQ ../doc/HINTS 
%doc ../doc/README* ../doc/*.HOWTO ../doc/TODO ../doc/UPGRADE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/licq/plugins
%attr(755,root,root) %{_datadir}/licq/plugins/*
%{_datadir}/licq/translations
%{_datadir}/licq/utilities
%{_datadir}/licq/qt-gui

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT
