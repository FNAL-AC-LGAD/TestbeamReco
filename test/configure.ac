AC_INIT(program, 1.0)

dnl Switch to a C++ compiler, and check if it works.
AC_LANG(C++)
AC_PROG_CXX

dnl set --std=c++11
case "$CXXFLAGS" in 
  *"--std=c++11"*)
    # Do nothing
    ;;
  *)
    CXXFLAGS="$CXXFLAGS --std=c++11" 
esac

dnl check for ldconfig
AC_CHECK_PROG(ldconfigfound, ldconfig, yes, no)

LDCONFIG=
if test ${ldconfigfound} == yes; then
   LDCONFIG="ldconfig"
fi

AC_SUBST(LDCONFIG, $LDCONFIG)

dnl check if this is a mac
LIBSUFFIX="so"
OSNAME=$(uname -s)
if [[ "$OSNAME" == "Darwin" ]]; then
   LIBSUFFIX="dylib"
fi

AC_SUBST(LIBSUFFIX, $LIBSUFFIX)

dnl check for root
AC_CHECK_PROG(rootconfigfound, root-config, yes, no)
AC_CHECK_PROG(rootcintfound, rootcint, yes, no)

if test ${rootconfigfound} == no; then
   AC_ERROR([ROOT: root-config not found.])
fi

if test ${rootcintfound} == no; then
   AC_ERROR([ROOT: rootcint not found.])
fi   

dnl root is present, lets check for TMVA
TMVALIB=$(root-config --libdir)/libTMVA.so
AC_CHECK_FILE($TMVALIB, [], [])

TMVALIB=ac_cv_file_$(echo ${TMVALIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')

dnl configure TMVA if it is found
if test "${!TMVALIB}" = "no"; then
   AC_WARN([Optional dependency missing: TMVA libraries are not found.  If needed you must ensure your root install is built with support for TMVA.])
   AC_SUBST(TMVALIB, "")
else
   AC_SUBST(TMVALIB, -lTMVA)
fi

dnl check if scram is avaliable, and if so, get the numpy include path
AC_CHECK_PROG(scramfound, scram, yes, no)

if test ${scramfound} == yes; then
   AC_SUBST(SCRAMNUMPYCFG, $(scram tool tag py2-numpy PY2_NUMPY_BASE))
else
   AC_SUBST(SCRAMNUMPYCFG, "")
fi

dnl check for python 
AC_CHECK_PROG(pythonconfigfound, python-config, yes, no)

if test ${pythonconfigfound} == no; then
   AC_WARN([Optional dependency missing: python-config not found.])
   AC_SUBST(PYTHONCFG, "")
else
   AC_SUBST(PYTHONCFG, python-config)
fi

dnl check for openCV
if test -z ${OPENCVDIR+x}; then
   OPENCVDIR=/usr/local/
fi

OPENCVINCLUDECVH=$OPENCVDIR/include/opencv/cv.h
OPENCVINCLUDEMLH=$OPENCVDIR/include/opencv/ml.h
AC_CHECK_FILE($OPENCVINCLUDECVH, [], [])
AC_CHECK_FILE($OPENCVINCLUDEMLH, [], [])

OPENCVLIBML=$OPENCVDIR/lib/libopencv_ml.${LIBSUFFIX}
OPENCVLIBCV=$OPENCVDIR/lib/libopencv_core.${LIBSUFFIX}
AC_CHECK_FILE($OPENCVLIBCV, [], [])
AC_CHECK_FILE($OPENCVLIBML, [], [])

OPENCVINCLUDECVH=ac_cv_file_$(echo ${OPENCVINCLUDECVH} | sed -e 's/[\/]/_/g' -e 's/\./_/')
OPENCVINCLUDEMLH=ac_cv_file_$(echo ${OPENCVINCLUDEMLH} | sed -e 's/[\/]/_/g' -e 's/\./_/')
OPENCVLIBCV=ac_cv_file_$(echo ${OPENCVLIBCV} | sed -e 's/[\/]/_/g' -e 's/\./_/')
OPENCVLIBML=ac_cv_file_$(echo ${OPENCVLIBML} | sed -e 's/[\/]/_/g' -e 's/\./_/')

dnl configure OPENCV if it is found
if test "${!OPENCVINCLUDECVH}" = "no" || test "${!OPENCVINCLUDEMLH}" = "no" || test "${!OPENCVLIBCV}" = "no" || test "${!OPENCVLIBML}" = "no"; then
   AC_WARN([Optional dependency missing: OpenCV includes or libraries are not found. Specify location with "./configure OPENCVDIR=/Path" if required.])
   AC_SUBST(OPENCVDIR, "")
else
   AC_SUBST(OPENCVDIR, $OPENCVDIR)
fi

dnl check for tensorflow c-api
if test -z ${TENSORFLOWDIR+x}; then
   if test ${scramfound} == yes; then
      TENSORFLOWDIR=$(scram tool tag tensorflow-c TENSORFLOW_C_BASE)
      if test ${TENSORFLOWDIR:0:5} == SCRAM; then
         TENSORFLOWDIR=$(scram tool tag tensorflow TENSORFLOW_BASE)
      fi
   else
      TENSORFLOWDIR=/usr/local/
   fi
fi

TENSORFLOWINCLUDE=$TENSORFLOWDIR/include/tensorflow/c/c_api.h
AC_CHECK_FILE($TENSORFLOWINCLUDE, [], [])

TENSORFLOWLIB=$TENSORFLOWDIR/lib/libtensorflow.${LIBSUFFIX}
AC_CHECK_FILE($TENSORFLOWLIB, [], [])

TENSORFLOWFRAMEWORKLIB=$TENSORFLOWDIR/lib/libtensorflow_framework.${LIBSUFFIX}
AC_CHECK_FILE($TENSORFLOWFRAMEWORKLIB, [], [])

TENSORFLOWINCLUDE=ac_cv_file_$(echo ${TENSORFLOWINCLUDE} | sed -e 's/[\/]/_/g' -e 's/\./_/')
TENSORFLOWLIB=ac_cv_file_$(echo ${TENSORFLOWLIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')
TENSORFLOWFRAMEWORKLIB=ac_cv_file_$(echo ${TENSORFLOWFRAMEWORKLIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')

dnl configure Tensorflow if it is found
if test "${!TENSORFLOWINCLUDE}" = "no" || test "${!TENSORFLOWINCLUDE}" = "no" || test "${!TENSORFLOWLIB}" = "no"; then
   AC_WARN([Optional dependency missing: Tensorflow c-api includes or libraries are not found. Specify location with "./configure TENSORFLOWDIR=/Path" if required.])
   AC_SUBST(TENSORFLOWDIR, "")
else
   AC_SUBST(TENSORFLOWDIR, $TENSORFLOWDIR)
   if test "${!TENSORFLOWFRAMEWORKLIB}" = "yes"; then
      AC_SUBST(TENSORFLOWLIBS, "-ltensorflow -ltensorflow_framework")
   else
      AC_SUBST(TENSORFLOWLIBS, "-ltensorflow")
   fi
fi

dnl check for fastjet 
if test -z ${FASTJETDIR+x}; then
   if test ${scramfound} == yes; then
      FASTJETDIR=$(scram tool tag fastjet FASTJET_BASE)
   else
      FASTJETDIR=/usr/local/
   fi
fi

FASTJETINCLUDE=$FASTJETDIR/include/fastjet/version.hh
AC_CHECK_FILE($FASTJETINCLUDE, [], [])

FASTJETLIB=$FASTJETDIR/lib/libfastjet.${LIBSUFFIX}
AC_CHECK_FILE($FASTJETLIB, [], [])

FASTJETTOOLSLIB=$FASTJETDIR/lib/libfastjettools.${LIBSUFFIX}
AC_CHECK_FILE($FASTJETTOOLSLIB, [], [])

FASTJETPLUGINSLIB=$FASTJETDIR/lib/libfastjetplugins.${LIBSUFFIX}
AC_CHECK_FILE($FASTJETPLUGINSLIB, [], [])

FASTJETSISCONELIB=$FASTJETDIR/lib/libsiscone.${LIBSUFFIX}
AC_CHECK_FILE($FASTJETSISCONELIB, [], [])

FASTJETSICONESPHERELIB=$FASTJETDIR/lib/libsiscone_spherical.${LIBSUFFIX}
AC_CHECK_FILE($FASTJETSICONESPHERELIB, [], [])

FASTJETINCLUDE=ac_cv_file_$(echo ${FASTJETINCLUDE} | sed -e 's/[\/]/_/g' -e 's/\./_/')
FASTJETLIB=ac_cv_file_$(echo ${FASTJETLIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')
FASTJETTOOLSLIB=ac_cv_file_$(echo ${FASTJETTOOLSLIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')
FASTJETPLUGINSLIB=ac_cv_file_$(echo ${FASTJETPLUGINSLIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')
FASTJETSISCONELIB=ac_cv_file_$(echo ${FASTJETSISCONELIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')
FASTJETSISCONESPHERELIB=ac_cv_file_$(echo ${FASTJETSISCONESPHERELIB} | sed -e 's/[\/]/_/g' -e 's/\./_/')

dnl configure fastjet if it is found
if test "${!FASTJETINCLUDE}" = "no" || test "${!FASTJETTOOLSLIB}" = "no" || test "${!FASTJETLIB}" = "no" || test "${!FASTJETPLUGINSLIB}" = "no" || test "${!FASTJETSISCONELIB}" = "no" || test "${!FASTJETSISCONESPHERELIB}" = "no"; then
   AC_WARN([Optional dependency missing: Fastjet includes or libraries are not found. Specify location with "./configure FASTJETDIR=/Path" if required.])
   AC_SUBST(FASTJETDIR, "")
else
   AC_SUBST(FASTJETDIR, $FASTJETDIR)
   AC_SUBST(FASTJETLIBS, "-lfastjet -lfastjettools -lfastjetplugins -lsiscone -lsiscone_spherical")
fi

dnl check for xgboost
if test -z ${XGBOOSTDIR+x}; then
   XGBOOSTDIR=/usr/local/
fi

XGBOOSTINCLUDEXGBCAPIH=$XGBOOSTDIR/include/xgboost/c_api.h
XGBOOSTINCLUDERABCAPIH=$XGBOOSTDIR/rabit/include/rabit/c_api.h
AC_CHECK_FILE($XGBOOSTINCLUDEXGBCAPIH, [], [])
AC_CHECK_FILE($XGBOOSTINCLUDERABCAPIH, [], [])

XGBOOSTLIBXGB=$XGBOOSTDIR/lib/libxgboost.${LIBSUFFIX}
AC_CHECK_FILE($XGBOOSTLIBXGB, [], [])

XGBOOSTINCLUDEXGBCAPIH=ac_cv_file_$(echo ${XGBOOSTINCLUDEXGBCAPIH} | sed -e 's/[\/]/_/g' -e 's/\./_/')
XGBOOSTINCLUDERABCAPIH=ac_cv_file_$(echo ${XGBOOSTINCLUDERABCAPIH} | sed -e 's/[\/]/_/g' -e 's/\./_/')
XGBOOSTLIBXGB=ac_cv_file_$(echo ${XGBOOSTLIBXGB} | sed -e 's/[\/]/_/g' -e 's/\./_/')

dnl configure XGBOOST if it is found
if test "${!XGBOOSTINCLUDEXGBCAPIH}" = "no" || test "${!XGBOOSTINCLUDERABCAPIH}" = "no" || test "${!XGBOOSTLIBXGB}" = "no"; then
   AC_WARN([Optional dependency missing: XGBoost includes or libraries are not found. Specify location with "./configure XGBOOSTDIR=/Path" if required.])
   AC_SUBST(XGBOOSTDIR, "")
else
   AC_SUBST(XGBOOSTDIR, $XGBOOSTDIR)
fi

dnl Process Makefile.in to create Makefile
AC_OUTPUT(Makefile)
