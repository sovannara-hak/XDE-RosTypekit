%{
  #include "rttinterface/Types.h"
  #include "rtt/base/DataSourceBase.hpp"
  #include "rtt/base/ActionInterface.hpp"

  using namespace RTT;
%}

namespace RTT {
  namespace base { class ActionInterface; }
}

%exception {
  try
  {
    $action
  }
  catch(std::exception &e)
  {
    PyErr_SetString(PyExc_Exception, const_cast<char*>(e.what()));
    return NULL;
  }
}

%include "boost_shared_ptr.i"
%include "boost/smart_ptr/intrusive_ptr.hpp"
%include "std_string.i"

#define RTT_API

%import "rtt/base/DataSourceBase.hpp"
%template(DataSourceBasePtr) boost::intrusive_ptr<RTT::base::DataSourceBase>;

%include "rttinterface/Types.h"

%define register_rtt_type(name, type...)
  %template(data_ ## name) Types::data<type >;
  %template(value_ ## name) Types::value<type >;
  %template(set_ ## name) Types::set<type >;
 %enddef

  // Because we don't want a 500Mb dll
%define register_rtt_port(name, type...)
  %template(iport_ ## name) Types::iport<type >;
  %template(oport_ ## name) Types::oport<type >;
%enddef
