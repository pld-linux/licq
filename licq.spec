Summary:	Licq - ICQ clone.
Summary(pl):	Licq - klient ICQ.
Name:		licq
Version:	0.51
Release:	1d
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		http://licq.wibble.net/%{name}-%{version}.tar.gz
Patch:		licq.patch
URL:		http://licq.wibble.net/
Requires:	qt >= 1.41
Requires:	XFree86-libs
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Licq is an ICQ clone written fully in c++ using the Qt widget set. It is
an attempt to give linux a non-java option to the ICQ protocol, as the
java version is unstable and a memory hog.

%description -l pl
Licq jest klientem ICQ napisanym w C++ przy u¿yciu biblioteki Qt. Pozwala
zast±piæ, napisanego w Javie, klienta ICQ z Mirabilis, który potrzebuje do
pracy zbyt wiele zasobów i wymaga zainstalowanego jdk.

%prep
%setup  -q
%patch  -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share}

make install prefix=$RPM_BUILD_ROOT/usr/X11R6
strip $RPM_BUILD_ROOT/usr/X11R6/bin/licq

%files
%defattr(644, root, root, 755)
%doc doc/* 
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/share/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
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
