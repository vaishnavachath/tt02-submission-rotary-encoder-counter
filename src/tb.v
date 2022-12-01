`default_nettype none
`timescale 1ns/1ps

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test.py
    input clk,
    input rst,
    input rt_a,
    input rt_b,
    input tm_enable,
    output [6:0] segments
   );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    // wire up the inputs and outputs
    wire [7:0] inputs = {3'b0, tm_enable, rt_b, rt_a, rst, clk};
    wire [7:0] outputs;
    assign segments = outputs[6:0];

    // instantiate the DUT
    vaishnavachath_rotary_toplevel vaishnavachath_rotary_toplevel(
        .io_in  (inputs),
        .io_out (outputs)
        );

endmodule
