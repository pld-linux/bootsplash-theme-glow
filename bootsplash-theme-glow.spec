
%define		theme	glow

Summary:	Bootsplash - glow by shadzik theme
Summary(de.UTF-8):	Bootsplash - glow by shadzik Thema für Bootsplash
Summary(pl.UTF-8):	Bootsplash - motyw glow wg shadzika
Name:		bootsplash-theme-%{theme}
Version:	1.0
Release:	0.3
License:	GPL v2
Group:		Themes
Source0:	http://livecd.pld-linux.org/%{theme}-%{version}.tar.gz
# Source0-md5:	66cb332ca60e4e205f82c8f27537d412
URL:		http://livecd.pld-linux.org/
Requires:	bootsplash
Provides:	bootsplash-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glow theme by shadzik for bootsplash.

%description -l de.UTF-8
Glow by shadzik Thema für Bootsplash.

%description -l pl.UTF-8
Motyw Glow do bootsplash wg shadzika.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/%{theme}
install -d $THEME_DIR/{config,images}
install %{theme}/config/*.cfg $THEME_DIR/config
install %{theme}/images/*.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/%{theme}
