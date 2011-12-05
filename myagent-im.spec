Name:		myagent-im
Version:	0.4.6
Release:	1
Summary:	Instant messenger that supports Mail.ru protocol
Group:		Networking/Instant messaging
License:	GPLv2
URL:		http://code.google.com/p/myagent-im
Source0:	http://myagent-im.googlecode.com/files/%{name}_%{version}.tar.gz
BuildRequires:	qt4-devel, flex, pkgconfig, libxscrnsaver1-devel
BuildRequires:	zlib1-devel, libxapian-devel, libaspell-devel

%description
Instant messenger that supports Mail.ru protocol.

%prep
%setup -qn %{name}

%build
%qmake_qt4
%make

%install
export INSTALL_ROOT=%{buildroot}
%makeinstall_std

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*
