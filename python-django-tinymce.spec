# Created by pyp2rpm-3.3.2
%global pypi_name django-tinymce

Name:           python-%{pypi_name}
Version:        3.0.2
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
widget to render a form field as a TinyMCE editor. :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
django-tinymce **django-tinymce** is a Django application that contains a
widget to render a form field as a TinyMCE editor. :target:


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt tinymce/media/tiny_mce/license.txt tinymce/static/tinymce/license.txt
%doc README.rst tinymce/media/tiny_mce/plugins/style/readme.txt tinymce/static/tinymce/langs/readme.md
%{python3_sitelib}/testtinymce
%{python3_sitelib}/tinymce
%{python3_sitelib}/django_tinymce-%{version}-py?.?.egg-info

%changelog
* Sat May 16 2020 Chenxiong Qi <cqi@redhat.com> - 3.0.2-1
- Initial package.
