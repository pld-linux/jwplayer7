Summary:	Flash Video Player for FLV, H.264/MPEG-4, MP3 and YouTube Videos on your website
Summary(pl.UTF-8):	Odtwarzacz JW Media
Name:		jw_media_player
Version:	5.2
Release:	1
Epoch:		1
License:	CC 3.0
Group:		Applications/WWW
Source0:	http://www.longtailvideo.com/jw/upload/mediaplayer-viral.zip
# Source0-md5:	b3c1207f8d78e2181831f057d85b7c05
Source1:	lighttpd.conf
URL:		http://www.longtailvideo.com/players/jw-flv-player/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
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
appearance and an extensive, documented JavaScript/ActionScript API.

%description -l pl.UTF-8
JW Media Player (zbudowany z Flashem Adobe) potrafi odtwarzać pliki
multimedialne dowolnego typu obsługiwanego przez Adobe Flash Player
(MP3, FLV, SWF, JPG, PNG i GIF). Obsługuje także playlisty
RSS/XSPF/ATOM (z mieszanymi typami mediów), szeroki zakres ustawień do
modyfikowania zarówno zachowania jak i wyglądu oraz obszerne,
udokumentowane API JavaScriptu/ActionScriptu.

%prep
%setup -q -n mediaplayer-%{version}-viral

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a *.swf $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc readme.html
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%dir %{_appdir}
%{_appdir}/player.swf
%{_appdir}/yt.swf
