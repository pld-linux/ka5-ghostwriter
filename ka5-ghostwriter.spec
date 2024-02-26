%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kaname		ghostwriter

Summary:	Text editor for Markdown
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2649238ef497a28798e3560bb43fabac
URL:		https://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.15.9
BuildRequires:	Qt6Positioning-devel >= 5.15
BuildRequires:	Qt6PrintSupport-devel >= 5.15
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Quick-devel >= 5.15
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6WebChannel-devel
BuildRequires:	Qt6WebEngine-devel >= 5.15
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	kf6-extra-cmake-modules >= 5.90
BuildRequires:	kf6-kconfigwidgets-devel >= 5.90
BuildRequires:	kf6-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.90
BuildRequires:	kf6-kxmlgui-devel >= 5.90
BuildRequires:	kf6-sonnet-devel >= 5.90
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-linguist
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

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%{?with_tests:%ninja_build -C build test}

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
%{_iconsdir}/hicolor/*x*/apps/ghostwriter.png
%{_iconsdir}/hicolor/scalable/apps/ghostwriter.svg
%lang(ca) %{_mandir}/ca/man1/ghostwriter.1*
%lang(es) %{_mandir}/es/man1/ghostwriter.1*
%lang(it) %{_mandir}/it/man1/ghostwriter.1*
%{_mandir}/man1/ghostwriter.1*
%lang(nl) %{_mandir}/nl/man1/ghostwriter.1*
%lang(ru) %{_mandir}/ru/man1/ghostwriter.1*
%lang(sv) %{_mandir}/sv/man1/ghostwriter.1.*
%lang(uk) %{_mandir}/uk/man1/ghostwriter.1*
%{_datadir}/metainfo/org.kde.ghostwriter.metainfo.xml
