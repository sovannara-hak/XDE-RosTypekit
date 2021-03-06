# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rtt_sensor_msgs_type', [dirname(__file__)])
        except ImportError:
            import _rtt_sensor_msgs_type
            return _rtt_sensor_msgs_type
        if fp is not None:
            try:
                _mod = imp.load_module('_rtt_sensor_msgs_type', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rtt_sensor_msgs_type = swig_import_helper()
    del swig_import_helper
else:
    import _rtt_sensor_msgs_type
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _rtt_sensor_msgs_type.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _rtt_sensor_msgs_type.SwigPyIterator_value(self)
    def incr(self, n = 1): return _rtt_sensor_msgs_type.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _rtt_sensor_msgs_type.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator_equal(self, *args)
    def copy(self): return _rtt_sensor_msgs_type.SwigPyIterator_copy(self)
    def next(self): return _rtt_sensor_msgs_type.SwigPyIterator_next(self)
    def __next__(self): return _rtt_sensor_msgs_type.SwigPyIterator___next__(self)
    def previous(self): return _rtt_sensor_msgs_type.SwigPyIterator_previous(self)
    def advance(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _rtt_sensor_msgs_type.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _rtt_sensor_msgs_type.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _rtt_sensor_msgs_type.SHARED_PTR_DISOWN
class DataSourceBasePtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DataSourceBasePtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DataSourceBasePtr, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _rtt_sensor_msgs_type.new_DataSourceBasePtr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _rtt_sensor_msgs_type.delete_DataSourceBasePtr
    __del__ = lambda self : None;
    def reset(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_reset(self, *args)
    def get(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_get(self)
    def __ref__(self): return _rtt_sensor_msgs_type.DataSourceBasePtr___ref__(self)
    def __deref__(self): return _rtt_sensor_msgs_type.DataSourceBasePtr___deref__(self)
    def swap(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_swap(self, *args)
    def stack_shared_ptr(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_stack_shared_ptr(self, *args)
    def stack_const_ptr(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_stack_const_ptr(self, *args)
    def ref(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_ref(self)
    def deref(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_deref(self)
    def evaluate(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_evaluate(self)
    def isAssignable(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_isAssignable(self)
    def updated(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_updated(self)
    def update(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_update(self, *args)
    def updateAction(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_updateAction(self, *args)
    def getMember(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_getMember(self, *args)
    def getMemberNames(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getMemberNames(self)
    def getParent(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getParent(self)
    def clone(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_clone(self)
    def copy(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_copy(self, *args)
    def getType(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getType(self)
    def getTypeInfo(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getTypeInfo(self)
    def getTypeName(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getTypeName(self)
    def write(self, *args): return _rtt_sensor_msgs_type.DataSourceBasePtr_write(self, *args)
    def toString(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_toString(self)
    def getRawPointer(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getRawPointer(self)
    def getRawConstPointer(self): return _rtt_sensor_msgs_type.DataSourceBasePtr_getRawConstPointer(self)
DataSourceBasePtr_swigregister = _rtt_sensor_msgs_type.DataSourceBasePtr_swigregister
DataSourceBasePtr_swigregister(DataSourceBasePtr)

class Types(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Types, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Types, name)
    __repr__ = _swig_repr
    __swig_getmethods__["build"] = lambda x: _rtt_sensor_msgs_type.Types_build
    if _newclass:build = staticmethod(_rtt_sensor_msgs_type.Types_build)
    __swig_getmethods__["data_JointState"] = lambda x: _rtt_sensor_msgs_type.Types_data_JointState
    if _newclass:data_JointState = staticmethod(_rtt_sensor_msgs_type.Types_data_JointState)
    __swig_getmethods__["value_JointState"] = lambda x: _rtt_sensor_msgs_type.Types_value_JointState
    if _newclass:value_JointState = staticmethod(_rtt_sensor_msgs_type.Types_value_JointState)
    __swig_getmethods__["set_JointState"] = lambda x: _rtt_sensor_msgs_type.Types_set_JointState
    if _newclass:set_JointState = staticmethod(_rtt_sensor_msgs_type.Types_set_JointState)
    __swig_getmethods__["iport_JointState"] = lambda x: _rtt_sensor_msgs_type.Types_iport_JointState
    if _newclass:iport_JointState = staticmethod(_rtt_sensor_msgs_type.Types_iport_JointState)
    __swig_getmethods__["oport_JointState"] = lambda x: _rtt_sensor_msgs_type.Types_oport_JointState
    if _newclass:oport_JointState = staticmethod(_rtt_sensor_msgs_type.Types_oport_JointState)
    def __init__(self): 
        this = _rtt_sensor_msgs_type.new_Types()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _rtt_sensor_msgs_type.delete_Types
    __del__ = lambda self : None;
Types_swigregister = _rtt_sensor_msgs_type.Types_swigregister
Types_swigregister(Types)

def Types_build(*args):
  return _rtt_sensor_msgs_type.Types_build(*args)
Types_build = _rtt_sensor_msgs_type.Types_build

def Types_data_JointState(*args):
  return _rtt_sensor_msgs_type.Types_data_JointState(*args)
Types_data_JointState = _rtt_sensor_msgs_type.Types_data_JointState

def Types_value_JointState(*args):
  return _rtt_sensor_msgs_type.Types_value_JointState(*args)
Types_value_JointState = _rtt_sensor_msgs_type.Types_value_JointState

def Types_set_JointState(*args):
  return _rtt_sensor_msgs_type.Types_set_JointState(*args)
Types_set_JointState = _rtt_sensor_msgs_type.Types_set_JointState

def Types_iport_JointState(*args):
  return _rtt_sensor_msgs_type.Types_iport_JointState(*args)
Types_iport_JointState = _rtt_sensor_msgs_type.Types_iport_JointState

def Types_oport_JointState(*args):
  return _rtt_sensor_msgs_type.Types_oport_JointState(*args)
Types_oport_JointState = _rtt_sensor_msgs_type.Types_oport_JointState

# This file is compatible with both classic and new-style classes.


