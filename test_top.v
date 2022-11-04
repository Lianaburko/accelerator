`timescale 1ns/100ps

module test_top();

localparam N = 32;
localparam RF_Addr_BITNES = 32;
reg clk = 0;
reg reset = 0;

always begin #5; clk <= ~clk; end
initial begin
reset <= 1'b0;
#20;
reset <= 1'b1;
#40;
reset <= 1'b0;
end



wire [N-1:0] o_data;
reg [N-1:0] i_data;
reg [RF_Addr_BITNES-1:0] addr;
reg WE;

top #(
	.N(N),
	.RF_Addr_BITNES(RF_Addr_BITNES)
)DUT(
	.i_clk(clk),
	.i_reset(reset),
	
	.i_addr(addr),
	.i_data(i_data),
	.o_data(o_data),
	.i_RF_WE(WE)
);

initial begin
	#100;
	
	addr <= 3'b000;
	i_data <= 16'd16;
	WE <= 1'b1;
	#10;
	WE <= 1'b0;
	
	addr <= 3'b001;
	i_data <= 16'd4;
	WE <= 1'b1;
	#10;
	WE <= 1'b0;
	
	addr <= 3'b010;
	i_data <= 16'd4;
	WE <= 1'b1;
	#10;
	WE <= 1'b0;
	
	addr <= 3'b011;
	i_data <= 16'd4;
	WE <= 1'b1;
	#10;
	WE <= 1'b0;
end



endmodule