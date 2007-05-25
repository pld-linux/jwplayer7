# TODO
# - all
Summary:	Flash Media Player
Summary(pl.UTF-8):	Odtwarzacz Flash Media
Name:		flash_media_player
Version:	3.8
Release:	0.1
License:	Creative Commons
Group:		Applications/WWW
Source0:	http://www.jeroenwijering.com/upload/%{name}.zip
# Source0-md5:	6f62caa77e4ca9f9da58ab2543831309
URL:		http://www.jeroenwijering.com/?item=Flash_Media_Player
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Flash Media player supports playback of a single media file of any
format the Adobe Flash Player can handle (MP3, FLV, SWF, JPG, PNG or
GIF). It also supports RSS/XSPF/ATOM playlist (with mixed mediatypes),
a wide range of flashvars (settings) for tweaking both behavior and
appearance and an extensive, documented Javascript/Actionscript API.

%description -l pl.UTF-8
Flash Media Player potrafi odtwarzać pliki multimedialne dowolnego
typu obsługiwanego przez Adobe Flash Player (MP3, FLV, SWF, JPG, PNG
i GIF). Obsługuje także playlisty RSS/XSPF/ATOM (z mieszanymi typami
mediów), szeroki zakres ustawień do modyfikowania zarówno zachowania
jak i wyglądu oraz obszerne, udokumentowane API
Javascriptu/Actionscriptu.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
