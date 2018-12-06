%global goipath         github.com/git-lfs/gitobj
Version:                1.0.0

%gometa

# Hack to match name that will exist when Go macros are updated.
%global goname golang-github-git-lfs-gitobj

Name:           %{goname}
Release:        1%{?dist}
Summary:        Read and write Git objects
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for building other packages which
use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE.md


%changelog
* Thu Oct 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Wed Aug 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180831git5aa0c18
- First package for Fedora
