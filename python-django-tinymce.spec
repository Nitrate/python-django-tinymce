# Created by pyp2rpm-3.3.2
%global pypi_name django-tinymce

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        1%{?dist}
Summary:        A Django application that contains a widget to render a form field as a TinyMCE editor

License:        MIT License
URL:            https://github.com/aljosa/django-tinymce
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(django)

%description
django-tinymce **django-tinymce** is a Django application that contains a
widget to render a form field as a TinyMCE editor.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
django-tinymce **django-tinymce** is a Django application that contains a
widget to render a form field as a TinyMCE editor.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

rm -r %{buildroot}%{python3_sitelib}/testtinymce/

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt tinymce/static/tinymce/license.txt
%doc README.rst tinymce/static/tinymce/langs/readme.md CONTRIBUTORS.rst CHANGELOG.rst CONTRIBUTING.rst
%{python3_sitelib}/tinymce
%{python3_sitelib}/django_tinymce-%{version}-py?.?.egg-info

%changelog
* Sun Jan 10 2021 Chenxiong Qi <qcxhome@gmail.com> - 3.2.0-1
- Rebuild version 3.2.0

* Sat May 16 2020 Chenxiong Qi <cqi@redhat.com> - 3.0.2-1
- Initial package.
