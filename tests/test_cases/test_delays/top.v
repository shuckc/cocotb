// Copyright cocotb contributors
// Licensed under the Revised BSD License, see LICENSE for details.
// SPDX-License-Identifier: BSD-3-Clause

module top ();
  reg [4:0] q = 0;
  initial begin
    #100; q <= 1;
    #100; q <= 2;
    #100; q <= 3;
  end

initial begin
  $dumpfile ("button_deb.vcd");
  $dumpvars (0);
  #1;
end

endmodule
