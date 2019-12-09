"""
==========================================================================
Alu.py
==========================================================================
ALU for CGRA tile.

Author : Cheng Tan
  Date : November 27, 2019

"""

from pymtl3 import *
from pymtl3.stdlib.ifcs import SendIfcRTL, RecvIfcRTL
from ...lib.opt_type    import *
from ..basic.Fu         import Fu

class Alu( Fu ):

  def construct( s, DataType, ConfigType ):

    super( Alu, s ).construct( DataType, ConfigType )

    @s.update
    def comb_logic():
      s.send_out.msg.predicate = s.recv_in0.msg.predicate and s.recv_in1.msg.predicate
      if s.recv_opt.msg.config == OPT_ADD:
        s.send_out.msg.payload = s.recv_in0.msg.payload + s.recv_in1.msg.payload
      elif s.recv_opt.msg.config == OPT_SUB:
        s.send_out.msg.payload = s.recv_in0.msg.payload - s.recv_in1.msg.payload
