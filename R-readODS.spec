#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readODS
Version  : 1.6.7
Release  : 1
URL      : https://cran.r-project.org/src/contrib/readODS_1.6.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readODS_1.6.7.tar.gz
Summary  : Read and Write ODS Files
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Rcpp
Requires: R-cellranger
Requires: R-hms
Requires: R-pillar
Requires: R-pkgconfig
Requires: R-readr
Requires: R-xml2
BuildRequires : R-Rcpp
BuildRequires : R-cellranger
BuildRequires : R-hms
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-readr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
# readODS
read ODS files into R
## how it works
ODS (Open Document Spreadsheets) files are basically a zip file with all the stuff in it.
The file `contents.xml` is a XML file containing all the numbers and formulas used in the ODS spreadsheets.

%prep
%setup -q -c -n readODS

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556495852

%install
export SOURCE_DATE_EPOCH=1556495852
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readODS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readODS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readODS
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc readODS || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/readODS/DESCRIPTION
/usr/lib64/R/library/readODS/INDEX
/usr/lib64/R/library/readODS/Meta/Rd.rds
/usr/lib64/R/library/readODS/Meta/features.rds
/usr/lib64/R/library/readODS/Meta/hsearch.rds
/usr/lib64/R/library/readODS/Meta/links.rds
/usr/lib64/R/library/readODS/Meta/nsInfo.rds
/usr/lib64/R/library/readODS/Meta/package.rds
/usr/lib64/R/library/readODS/NAMESPACE
/usr/lib64/R/library/readODS/R/readODS
/usr/lib64/R/library/readODS/R/readODS.rdb
/usr/lib64/R/library/readODS/R/readODS.rdx
/usr/lib64/R/library/readODS/help/AnIndex
/usr/lib64/R/library/readODS/help/aliases.rds
/usr/lib64/R/library/readODS/help/paths.rds
/usr/lib64/R/library/readODS/help/readODS.rdb
/usr/lib64/R/library/readODS/help/readODS.rdx
/usr/lib64/R/library/readODS/html/00Index.html
/usr/lib64/R/library/readODS/html/R.css
/usr/lib64/R/library/readODS/template/META-INF/manifest.xml
/usr/lib64/R/library/readODS/template/content.xml
/usr/lib64/R/library/readODS/template/meta.xml
/usr/lib64/R/library/readODS/template/mimetype
/usr/lib64/R/library/readODS/template/styles.xml
/usr/lib64/R/library/readODS/tests/testdata/1996-2000.ods
/usr/lib64/R/library/readODS/tests/testdata/col_types.ods
/usr/lib64/R/library/readODS/tests/testdata/datasets.ods
/usr/lib64/R/library/readODS/tests/testdata/decimal_comma.ods
/usr/lib64/R/library/readODS/tests/testdata/horrible.ods
/usr/lib64/R/library/readODS/tests/testdata/layout_test.ods
/usr/lib64/R/library/readODS/tests/testdata/layout_test.xls
/usr/lib64/R/library/readODS/tests/testdata/layout_test.xlsx
/usr/lib64/R/library/readODS/tests/testdata/lotsofnothing_test.ods
/usr/lib64/R/library/readODS/tests/testdata/megairis.ods
/usr/lib64/R/library/readODS/tests/testdata/merged.ods
/usr/lib64/R/library/readODS/tests/testdata/mergerandgreaterthanlibreoffice.ods
/usr/lib64/R/library/readODS/tests/testdata/multiline_cells.ods
/usr/lib64/R/library/readODS/tests/testdata/multisheet.ods
/usr/lib64/R/library/readODS/tests/testdata/na_test.ods
/usr/lib64/R/library/readODS/tests/testdata/readODStestfilegoogledocscreated.ods
/usr/lib64/R/library/readODS/tests/testdata/smartSheetTest.ods
/usr/lib64/R/library/readODS/tests/testdata/sum.ods
/usr/lib64/R/library/readODS/tests/testdata/table.ods
/usr/lib64/R/library/readODS/tests/testdata/test.ods
/usr/lib64/R/library/readODS/tests/testdata/wild_character_encoding.ods
/usr/lib64/R/library/readODS/tests/testthat.R
/usr/lib64/R/library/readODS/tests/testthat/test.ods
/usr/lib64/R/library/readODS/tests/testthat/test_col_types.R
/usr/lib64/R/library/readODS/tests/testthat/test_legacy.R
/usr/lib64/R/library/readODS/tests/testthat/test_multiline.R
/usr/lib64/R/library/readODS/tests/testthat/test_na.R
/usr/lib64/R/library/readODS/tests/testthat/test_read_ods.R
/usr/lib64/R/library/readODS/tests/testthat/test_write_ods.R