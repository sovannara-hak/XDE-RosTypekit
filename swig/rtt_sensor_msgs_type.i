%module rtt_sensor_msgs_type

%include "std_map.i"
%include "std_vector.i"
%include "std_pair.i"
%include "std_string.i"

%{
#include <sensor_msgs/typekit/Types.hpp>
%}


%include "swig/types.i"

namespace rtt_interface {
  register_rtt_type(JointState, sensor_msgs::JointState)

  register_rtt_port(JointState, sensor_msgs::JointState)
}


