%global debug_package %{nil}

Name:           codex
Version:        0.154.0
Release:        2%{?dist}
Summary:        Official MUSL build of Codex CLI from OpenAI

License:        Apache-2.0
URL:            https://github.com/openai/codex
Source0:        %{url}/archive/rust-v%{version}.tar.gz
Source1:        %{url}/releases/download/rust-v%{version}/codex-package-aarch64-unknown-linux-musl.tar.gz
Source2:        %{url}/releases/download/rust-v%{version}/codex-package-x86_64-unknown-linux-musl.tar.gz

%description
Codex CLI is a coding agent from OpenAI that runs locally on your computer.

%prep
%ifarch aarch64
%global binary_source 1
%elifarch x86_64
%global binary_source 2
%else
%error Unsupported architecture: %{_arch}
%endif

%setup -DTq -n . -b0 -b%{binary_source}

%install
# bin
install -Dpm 755 -t %{buildroot}%{_bindir} bin/*

%files
%license %{name}-rust-v%{version}/LICENSE
%doc %{name}-rust-v%{version}/{CHANGELOG.md,README.md}
%{_bindir}/*
