%define		rname	synthv1

Summary:	Old-school polyphonic sampler
Name:		veeone-synth
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/%{rname}/%{rname}-%{version}.tar.gz
# Source0-md5:	ccd2fb8c9742fe0946ce6c52ed748943
URL:		http://synthv1.sourceforge.net
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):  shared-mime-info
Requires:	jack-audio-connection-kit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
synthv1 is an old-school all-digital 4-oscillator subtractive
polyphonic synthesizer with stereo fx.

%prep
%setup -qn %{rname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database

%postun
%update_icon_cache hicolor
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{rname}_jack
%{_datadir}/mime/packages/synthv1.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_iconsdir}/hicolor/*/mimetypes/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.svg
%{_mandir}/man1/synthv1.1*

%dir %{_libdir}/lv2/%{rname}.lv2
%attr(755,root,root) %{_libdir}/lv2/%{rname}.lv2/*.so
%{_libdir}/lv2/%{rname}.lv2/*.ttl

