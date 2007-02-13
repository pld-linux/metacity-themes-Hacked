Summary:	Hacked theme
Summary(pl.UTF-8):	Motyw Hacked
Name:		metacity-themes-Hacked
Version:	1.0
Release:	3
License:	GPL
Group:		Themes/GTK+
Source0:	http://art.gnome.org/download/themes/metacity/503/MCity-Hacked.tar.gz
# Source0-md5:	99c642e7fa3aa857073c5dd9eee49593
URL:		http://art.gnome.org/
Requires:	metacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hacked theme for metacity.

%description -l pl.UTF-8
Motyw Hacked dla metacity.

%prep
%setup -q -n Hacked

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/Hacked
cp -r metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Hacked

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Hacked
%{_datadir}/themes/Hacked/metacity-1
