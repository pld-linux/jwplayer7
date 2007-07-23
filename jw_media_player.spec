# TODO
# - all
Summary:	JW Media Player
Summary(pl.UTF-8):	Odtwarzacz Flash Media
Name:		jw_media_player
Version:	3.99
Release:	0.1
License:	Creative Commons
Group:		Applications/WWW
Source0:	http://www.jeroenwijering.com/upload/%{name}.zip
# Source0-md5:	995e438774dba2c1c3919e62749aa735
URL:		http://www.jeroenwijering.com/?item=JW_Media_Player
Obsoletes:	flash_media_player
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

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
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a mediaplayer.swf $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}/mediaplayer.swf
