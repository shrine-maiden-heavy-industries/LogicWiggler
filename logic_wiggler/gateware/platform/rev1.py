# SPDX-License-Identifier: BSD-3-Clause
from amaranth                            import *
from amaranth.build                      import *
from amaranth.vendor.lattice_ice40       import LatticeICE40Platform

class WigglerRev1(LatticeICE40Platform):
	device       = 'iCE40UP5K'
	package      = 'SG48I'
	default_clk  = 'clk'
	toolchain    = 'IceStorm'


	resources = [
		Resource('clk', 0,
			Pins('0', dir = 'i'),
			Clock(16e6),
			Attrs(GLOBAL = True, IO_STANDARD = 'SB_LVCMOS')
		),
	]

	connectors = []
