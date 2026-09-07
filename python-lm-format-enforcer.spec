Name:           python-lm-format-enforcer
Version:        0.11.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Enforce the output format _JSON Schema, Regex etc_ of a language model

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/noamgat/lm-format-enforcer
Source:         %{pypi_source lm_format_enforcer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lm-format-enforcer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-lm-format-enforcer
Summary:        %{summary}

%description -n python3-lm-format-enforcer %_description


%prep
%autosetup -p1 -n lm_format_enforcer-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files lmformatenforcer


%check
%pyproject_check_import


%files -n python3-lm-format-enforcer -f %{pyproject_files}


%changelog
%autochangelog
