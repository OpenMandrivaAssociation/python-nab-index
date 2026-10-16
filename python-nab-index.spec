%define module nab_index

Name:		python-nab-index
Version:	0.0.21
Release:	1
Summary:	PyPI Simple API client and on-disk cache for nab
License:	MIT
Group:		Development/Python
URL:		https://github.com/notatallshaw/nab
Source0:	https://files.pythonhosted.org/packages/source/n/nab-index/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Index client used by nab and by pipdeptree's from-index command.
The default pipdeptree command reads the local environment and does not use this client.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
