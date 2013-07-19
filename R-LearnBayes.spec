%global packname LearnBayes
%global rlibdir %{_libdir}/R/library

Name: R-%{packname}
Version: 2.12
Release: 1
Summary: Functions for Learning Bayesian Inference
Group: Sciences/Mathematics
License: GPLv2+
URL: http://cran.r-project.org/web/packages/%{packname}/index.html
Source0: http://cran.r-project.org/src/contrib/%{packname}_2.12.tar.gz
BuildArch: noarch
Requires: R-core
BuildRequires: R-devel texlive-collection-latex

%description
LearnBayes contains a collection of functions helpful in
learning the basic tenets of Bayesian statistical inference.
It contains functions for summarizing basic one and two
parameter posterior distributions and predictive distributions.
It contains MCMC algorithms for summarizing posterior
distributions defined by the user. It also contains functions
for regression models, hierarchical models, Bayesian tests, and 
illustrations of Gibbs sampling.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
