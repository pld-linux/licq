Summary:	An ICQ client for online messaging.
Name:		licq
Version:	0.84a
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.licq.org/
Source0:	http://www.licq.org/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-console.patch
BuildRequires:	qt-devel >= 2.1
BuildRequires:	ncurses-devel >= 5.0
Requires:	qt >= 2.1
Requires:	ncurses >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt_gui		qt-gui-0.84a
%define		auto_reply	auto-reply-0.16
%define		console		console-0.21-cvs
%define		forwarder	forwarder-0.65
%define		rms		rms-0.10-cvs

%description
Licq is an ICQ online messaging system clone, written in C++ using the
Qt widget set. Licq supports all of the major features of ICQ,
including messaging, URLs, chat, file transfer, and white pages
information. Additionally, Licq is very configurable and supports
skins and different icon packs.

%prep
%setup -q -T -b 0
%patch0 -p1
%patch1 -p1

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

install -d $RPM_BUILD_ROOT%{_applnkdir}/Networking
mv plugins/%{qt_gui}/doc doc/%{qt_gui}
mv plugins/%{qt_gui}/README.* doc/%{qt_gui}
mv plugins/%{console}/README doc/README.CONSOLE
mv plugins/%{forwarder}/README doc/README.FORWARDER
mv plugins/%{rms}/README doc/README.RMS
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/licq.desktop

gzip -9nf doc/{BUGS,CHANGELOG,CREDITS,HINTS,*.HOWTO,README*,TODO} \
	doc/%{qt_gui}/{CHANGELOG,README*,*.HOWTO,HINTS} \
	upgrade/UPGRADE README*
	
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc doc/*.gz
%doc upgrade/*
%doc README*.gz
%{_applnkdir}/Networking/licq.desktop
%attr(755,root,root) %{_bindir}/licq*
%{_libdir}/licq
%{_datadir}/licq
