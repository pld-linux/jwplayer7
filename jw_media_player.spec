# TODO: spec filename vs Name
Summary:	JW Media Player
Summary(pl.UTF-8):	Odtwarzacz Flash Media
Name:		jw_media_player
Version:	3.99
Release:	0.4
License:	Creative Commons
Group:		Applications/WWW
Source0:	http://www.jeroenwijering.com/upload/%{name}.zip
# Source0-md5:	995e438774dba2c1c3919e62749aa735
Source1:	%{name}-lighttpd.conf
URL:		http://www.jeroenwijering.com/?item=JW_Media_Player
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	webapps
Requires:	webserver(alias)
Obsoletes:	flash_media_player
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir	%{_datadir}/%{_webapp}

%description
The JW Media Player (built with Adobe's Flash) supports playback of a
single media file of any format the Adobe Flash Player can handle
(MP3, FLV, SWF, JPG, PNG and GIF). It also supports RSS, XSPF and ATOM
playlist (with mixed mediatypes and advertisement possibilities), a
wide range of flashvars (settings) for tweaking both behavior and
appearance and an extensive, documented javascript/actionscript API.

%description -l pl.UTF-8
Flash Media Player potrafi odtwarzać pliki multimedialne dowolnego
typu obsługiwanego przez Adobe Flash Player (MP3, FLV, SWF, JPG, PNG i
GIF). Obsługuje także playlisty RSS/XSPF/ATOM (z mieszanymi typami
mediów), szeroki zakres ustawień do modyfikowania zarówno zachowania
jak i wyglądu oraz obszerne, udokumentowane API
Javascriptu/Actionscriptu.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a mediaplayer.swf $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%dir %{_appdir}
%{_appdir}/mediaplayer.swf
