%define		qt_gui_ver	0.63

Summary:	Licq - ICQ clone.
Summary(pl):	Licq - klient ICQ.
Name:		licq
Version:	0.70d
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ftp.licq.org/pub/licq/srcs/%{name}-%{version}.tar.gz
Source1:	http://ftp.licq.org/pub/licq/srcs/%{name}_qt-gui-%{qt_gui_ver}.tar.gz
Source2:	licq.wmconfig
Source3:	licq.mini-icon.xpm
Source4:	http://www.crewq.com/licq/icons/icons-dots.tar.gz
Patch0:		licq-DESTDIR.patch
URL:		http://www.licq.org/
BuildRequires:	libstdc++-devel
BuildRequires:	gettext
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6

%description
Licq is an ICQ clone written fully in c++ using the Qt widget set. It is
an attempt to give linux a non-java option to the ICQ protocol, as the
java version is unstable and a memory hog.

%description -l pl
Licq jest klientem ICQ napisanym w C++ przy u¿yciu biblioteki Qt. Pozwala
zast±piæ, napisanego w Javie, klienta ICQ z Mirabilis, który potrzebuje do
pracy zbyt wiele zasobów i wymaga zainstalowanego jdk.

%package	devel
Summary:	Header files for compile licq plugins
Summary(pl):	Pliki nag³ówkowe do kompilacji wtyczek licq
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
Header files for compile licq plugins.

%description devel -l pl
Pliki nag³ówkowe do kompilacji wtyczek licq.

%prep
%setup -q  -a 1 -n %{name}-%{version}/plugins
cd ..
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
cd qt-gui-%{qt_gui_ver}
gettextize --copy --force
%configure 
make
cd ../..
%configure
make

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
