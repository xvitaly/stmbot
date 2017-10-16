%global appname stmbot

%global appsum Steam profile checker bot for Telegram
%global appdesc Simple Steam profile checker bot for Telegram by EasyCoding Team

Name: python-%{appname}
Version: 0.1
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv3+
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel

BuildRequires: python2dist(pytelegrambotapi)
BuildRequires: python3dist(pytelegrambotapi)
BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)
BuildRequires: python2dist(wheel)
BuildRequires: python3dist(wheel)
BuildRequires: python2dist(six)
BuildRequires: python3dist(six)

%description
%{appdesc}.

%package -n python2-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python2-%{appname}}

%description -n python2-%{appname}
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{appname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{appname}
%license LICENSE
%doc README.md
%{_bindir}/%{appname}
%{python3_sitelib}/*

%changelog
* Mon Oct 16 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-1
- Initial SPEC release.
