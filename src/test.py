import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


segments = [ 63, 6, 91, 79, 102, 109, 124, 7, 127, 103, 119, 127, 57, 63, 121, 113]

@cocotb.test()
async def test_rotaryenc(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0
    await ClockCycles(dut.clk, 10)
    dut.tm_enable.value = 1
    await ClockCycles(dut.clk, 12)

    #check test mode
    dut._log.info("\n\nTest mode :")
    for i in range(32):
        dut._log.info("segment value = {}".format(segments.index(dut.segments.value)))
        await ClockCycles(dut.clk, 2)

    #check normal mode
    dut.tm_enable.value = 0
    await ClockCycles(dut.clk, 16)

    dut._log.info("\n\nNormal mode (upcount) :")
    rta = Clock(dut.rt_a, 80, units="us")
    rtb = Clock(dut.rt_b, 35, units="us")
    cocotb.start_soon(rta.start())
    cocotb.start_soon(rtb.start())
    for i in range(256):
        await ClockCycles(dut.clk, 1, rising=False)
        dut._log.info("segment value = {}".format(segments.index(dut.segments.value)))

    
    dut._log.info("\n\nNormal mode (decrement) :")
    rta = Clock(dut.rt_a, 80, units="us")
    rtb = Clock(dut.rt_b, 35, units="us")
    cocotb.start_soon(rtb.start())
    cocotb.start_soon(rta.start())
    for i in range(256):
        await ClockCycles(dut.clk, 1, rising=False)
        dut._log.info("segment value = {}".format(segments.index(dut.segments.value)))