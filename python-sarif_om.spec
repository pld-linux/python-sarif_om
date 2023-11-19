#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Classes implementing the SARIF 2.1.0 object model
Summary(pl.UTF-8):	Klasy implementujące model obiektowy SARIF 2.1.0
Name:		python-sarif_om
Version:	1.0.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sarif-om/
Source0:	https://files.pythonhosted.org/packages/source/s/sarif-om/sarif_om-%{version}.tar.gz
# Source0-md5:	b392605ffcf1673c4ed425b300d7ab10
URL:		https://pypi.org/project/sarif-om/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-attrs
BuildRequires:	python-pbr
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs
BuildRequires:	python3-pbr
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains classes for the object model defined by the
Static Analysis Results Interchange Format (SARIF) Version 2.1.0 file
format (<https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01>), an
OASIS (<https://www.oasis-open.org/>) Committee Specification:
<https://www.oasis-open.org/news/announcements/static-analysis-results-interchange-format-sarif-v2-1-0-from-the-sarif-tc-is-an-a>.

%description -l pl.UTF-8
Ten moduł zawiera klasy modelu obiektowego, zdefiniowanego w ramach
formatu plików SARIF (Static Analysis Results Interchange Format) w
wersji 2.1.0 wg specyfikacji komitetu OASIS
(<https://www.oasis-open.org/>):
<https://www.oasis-open.org/news/announcements/static-analysis-results-interchange-format-sarif-v2-1-0-from-the-sarif-tc-is-an-a>.

%package -n python3-sarif_om
Summary:	Classes implementing the SARIF 2.1.0 object model
Summary(pl.UTF-8):	Klasy implementujące model obiektowy SARIF 2.1.0
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sarif_om
This module contains classes for the object model defined by the
Static Analysis Results Interchange Format (SARIF) Version 2.1.0 file
format (<https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01>), an
OASIS (<https://www.oasis-open.org/>) Committee Specification:
<https://www.oasis-open.org/news/announcements/static-analysis-results-interchange-format-sarif-v2-1-0-from-the-sarif-tc-is-an-a>.

%description -n python3-sarif_om -l pl.UTF-8
Ten moduł zawiera klasy modelu obiektowego, zdefiniowanego w ramach
formatu plików SARIF (Static Analysis Results Interchange Format) w
wersji 2.1.0 wg specyfikacji komitetu OASIS
(<https://www.oasis-open.org/>):
<https://www.oasis-open.org/news/announcements/static-analysis-results-interchange-format-sarif-v2-1-0-from-the-sarif-tc-is-an-a>.

%package apidocs
Summary:	API documentation for Python sarif_om module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sarif_om
Group:		Documentation

%description apidocs
API documentation for Python sarif_om module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sarif_om.

%prep
%setup -q -n sarif_om-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst SECURITY.md
%{py_sitescriptdir}/sarif_om
%{py_sitescriptdir}/sarif_om-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sarif_om
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst SECURITY.md
%{py3_sitescriptdir}/sarif_om
%{py3_sitescriptdir}/sarif_om-%{version}-py*.egg-info
%endif
