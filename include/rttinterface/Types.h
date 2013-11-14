#pragma once

#include <string>

#include "rtt/internal/DataSources.hpp"
#include "rtt/InputPort.hpp"
#include "rtt/OutputPort.hpp"

namespace rtt_interface
{

  struct Types
  {
    // Used to convert from and to RTT::base::DataSourceBase for the python interface (explicit template instanciation in the .i)
    static RTT::base::DataSourceBase::shared_ptr build(long long ptr) // There must be a better way to build a swig RTT::base::DataSourceBase::shared_ptr from Python C/API
    {
      return RTT::base::DataSourceBase::shared_ptr(*reinterpret_cast<RTT::base::DataSourceBase::shared_ptr *>(ptr));
    }

    template<typename T> static RTT::base::DataSourceBase::shared_ptr data(const T & val)
    {
      return RTT::base::DataSourceBase::shared_ptr(new RTT::internal::ConstantDataSource<T>( val ));
    }

    template<typename T> static T value(const RTT::base::DataSourceBase::shared_ptr & val)
    {
      typename RTT::internal::DataSource<T>::shared_ptr d = boost::dynamic_pointer_cast< RTT::internal::DataSource<T> >( val );
      return d->value();
    }

    template<typename T> static bool set(const T & val, const RTT::base::DataSourceBase::shared_ptr & ds)
    {
      typename RTT::internal::AssignableDataSource<T>::shared_ptr ad = RTT::internal::AssignableDataSource<T>::narrow( ds.get() );
      if(ad)
      {
        ad->set(val);
        return true;
      }
      return false;
    }

    // Used to create ports for the python interface
    template<typename T> static RTT::base::PortInterface * iport(const std::string & name, const RTT::ConnPolicy & policy = RTT::ConnPolicy())
    {
      return static_cast<RTT::base::PortInterface *>(new RTT::InputPort<T>(name, policy));
    }

    template<typename T> static RTT::base::PortInterface * oport(const std::string & name, bool keep_last_written_value = true)
    {
      return static_cast<RTT::base::PortInterface *>(new RTT::OutputPort<T>(name, keep_last_written_value));
    }
  };
}

// cmake:sourcegroup=RTTInterface
