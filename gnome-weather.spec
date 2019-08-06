Summary:	A weather application for GNOME
Summary(pl.UTF-8):	Aplikacja pogodowa dla GNOME
Name:		gnome-weather
Version:	3.32.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-weather/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	824022f82b3abc466e1afad99b431039
URL:		https://wiki.gnome.org/Apps/Weather
BuildRequires:	appstream-glib
BuildRequires:	geoclue2-devel >= 2.3.1
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.50.0
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	libgweather-devel >= 3.28
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	geoclue2 >= 2.3.1
Requires:	gjs >= 1.50.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.20
Requires:	hicolor-icon-theme
Requires:	libgweather >= 3.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-weather is a small application that allows you to monitor the
current weather conditions for your city, or anywhere in the world,
and to access updated forecasts provided by various Internet services.

%description -l pl.UTF-8
gnome-weather to mała aplikacja pozwalająca na śledzenie aktualnych
warunków pogodowych we własnym mieście lub dowolnym miejscu na świecie
oraz na dostęp do uaktualnianych prognoz dostarczanych przez różne
serwisy internetowe.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%if 0
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	GJS="/usr/bin/gjs" \
	--disable-silent-rules
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang org.gnome.Weather

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.Weather.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%{_datadir}/dbus-1/services/org.gnome.Weather.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini
%{_datadir}/metainfo/org.gnome.Weather.appdata.xml
%dir %{_datadir}/org.gnome.Weather
%attr(755,root,root) %{_datadir}/org.gnome.Weather/org.gnome.Weather
%attr(755,root,root) %{_datadir}/org.gnome.Weather/org.gnome.Weather.BackgroundService
%{_datadir}/org.gnome.Weather/org.gnome.Weather.*.gresource
%{_desktopdir}/org.gnome.Weather.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Weather.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Weather-symbolic.svg
