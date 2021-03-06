# Created by pyp2rpm-3.3.3
%global pypi_name whitenoise

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        1%{?dist}
Summary:        Radically simplified static file serving for WSGI applications

License:        MIT
URL:            http://whitenoise.evans.io
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 25 2020 Evgeni Golov 5.2.0-1
- Update to 5.2.0

* Thu Jun 04 2020 Evgeni Golov 5.1.0-1
- Update to 5.1.0

* Wed Mar 18 2020 Samir Jha 5.0.1-1
- Update to 5.0.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.4-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 4.1.4-1
- Initial package.
