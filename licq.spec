Summary:	Licq - ICQ clone.
Summary(pl):	Licq - klient ICQ.
Name:		licq
Version:	0.70d
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ftp.licq.org/pub/licq/srcs/licq-%{version}.tar.gz
Source2:	licq.wmconfig
Source3:	licq.mini-icon.xpm
Source4:	http://www.crewq.com/licq/icons/icons-dots.tar.gz
Patch0:		licq-DESTDIR.patch
URL:		http://www.licq.org/
BuildPrereq:	libstdc++-devel
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
%setup -q  
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_includedir}/%{name}}


make install \
	DESTDIR=$RPM_BUILD_ROOT

install src/inc/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%files
%defattr(644,root,root,755)
%doc doc/BUGS doc/CHANGELOG doc/CREDITS doc/FAQ doc/HINTS 
%doc doc/README* doc/*.HOWTO doc/TODO doc/UPGRADE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Mar 12 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.61-1]
- removed licq.patch 
- removed Requires: XFree86-libs (autogenerate)

* Thu Oct 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.43-3]
- added using $RPM_OPT_FLAGS during compile,
- some commands is now in separated %%install section,
- /usr/X11R6/share/Licq mast be also registered in %%files,
- removed COPYING file from %%doc (clear copyright statment is in Copyright
  field).

* Sat Oct 24 1998 Marcin Bohosiewicz <marcus@krakow.linux.org.pl>
  [0.43-2]
- changed install prefix from /usr to /usr/X11R6.

* Sat Oct 10 1998 Marcin Bohosiewicz <marcus@krakow.linux.org.pl>
  [0.43-1]
- added pl translation.

* Sun Aug 22 1998 Marcin Bohosiewicz <marcus@krakow.linux.org.pl>
- first release
