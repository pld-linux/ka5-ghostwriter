%define		kdeappsver	23.04.3
%define		qtver		5.15.2
%define		kaname		ghostwriter

Summary:	Text editor for Markdown
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3e236150f908493bed954dcab32f4311
Patch0:		uint.patch
URL:		https://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.15.9
BuildRequires:	Qt5Positioning-devel >= 5.15
BuildRequires:	Qt5PrintSupport-devel >= 5.15
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-devel >= 5.15
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5WebChannel-devel
BuildRequires:	Qt5WebEngine-devel >= 5.15
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	kf5-extra-cmake-modules >= 5.90
BuildRequires:	kf5-kconfigwidgets-devel >= 5.90
BuildRequires:	kf5-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.90
BuildRequires:	kf5-kxmlgui-devel >= 5.90
BuildRequires:	kf5-sonnet-devel >= 5.90
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ghostwriter is a Windows and Linux text editor for Markdown, which is
a plain text markup format created by John Gruber. For more
information about Markdown, please visit John Gruber's website at
<http://www.daringfireball.net>. ghostwriter provides a relaxing,
distraction-free writing environment, whether your masterpiece be that
next blog post, your school paper, or your NaNoWriMo novel. For a tour
of its features, please visit the [ghostwriter project
site](https://ghostwriter.kde.org).

%prep
%setup -q -n %{kaname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%{?with_tests:%ninja_build test}

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ghostwriter
%{_desktopdir}/org.kde.ghostwriter.desktop
%{_iconsdir}/hicolor/128x128/apps/ghostwriter.png
%{_iconsdir}/hicolor/16x16/apps/ghostwriter.png
%{_iconsdir}/hicolor/22x22/apps/ghostwriter.png
%{_iconsdir}/hicolor/256x256/apps/ghostwriter.png
%{_iconsdir}/hicolor/32x32/apps/ghostwriter.png
%{_iconsdir}/hicolor/64x64/apps/ghostwriter.png
%{_iconsdir}/hicolor/scalable/apps/ghostwriter.svg
%lang(ca) %{_mandir}/ca/man1/ghostwriter.1*
%lang(es) %{_mandir}/es/man1/ghostwriter.1*
%lang(it) %{_mandir}/it/man1/ghostwriter.1*
%{_mandir}/man1/ghostwriter.1*
%lang(nl) %{_mandir}/nl/man1/ghostwriter.1*
%lang(ru) %{_mandir}/ru/man1/ghostwriter.1*
%lang(uk) %{_mandir}/uk/man1/ghostwriter.1*
%{_datadir}/metainfo/org.kde.ghostwriter.metainfo.xml
