%global debug_package %{nil}

Name:           codex
Version:        0.153.3
Release:        1%{?dist}
Summary:        Official MUSL build of Codex CLI from OpenAI

License:        Apache-2.0
URL:            https://github.com/openai/codex
Source0:        %{url}/archive/rust-v%{version}.tar.gz
Source1:        %{url}/releases/download/rust-v%{version}/codex-package-aarch64-unknown-linux-musl.tar.zst
Source2:        %{url}/releases/download/rust-v%{version}/codex-package-x86_64-unknown-linux-musl.tar.zst

%description
Codex CLI is a coding agent from OpenAI that runs locally on your computer.

%prep
%ifarch aarch64
%setup -DTq -n . -b0 -b1
%elifarch x86_64
%setup -DTq -n . -b0 -b2
%else
%error Unsupported architecture: %{_arch}
%endif

%install
# bin
install -Dpm 755 -t %{buildroot}%{_bindir} bin/*

%files
%license %{name}-rust-v%{version}/LICENSE
%doc %{name}-rust-v%{version}/{CHANGELOG.md,README.md}
%{_bindir}/*
