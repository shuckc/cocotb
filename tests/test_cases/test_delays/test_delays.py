# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def delay_units(dut):
    await Timer(95, units="timeunit")
    assert dut.q.value == 0
    await Timer(10, units="timeunit")
    assert dut.q.value == 1
    await Timer(100, units="timeunit")
    assert dut.q.value == 2
    await Timer(100, units="timeunit")
    assert dut.q.value == 3
