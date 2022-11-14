`timescale 1ns/100ps

module top #(
parameter N = 32,
parameter RF_Addr_BITNES = 3
)(
input wire i_clk, i_reset,
input wire [RF_Addr_BITNES-1:0] i_addr,
input wire [N-1:0] i_data,
output reg [N-1:0] o_data,
input wire i_RF_WE
);
reg [N-1:0] RF_a0;
reg [N-1:0] RF_b0;
reg [N-1:0] RF_30;
reg [N-1:0] RF_x0;
reg [N-1:0] RF_c0;
wire [N-1:0] RF_31;
register #(1,"sync","posedge",0,0,32,16'd0)register_31(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_30), .o_d(RF_31));
wire [N-1:0] RF_x1;
register #(1,"sync","posedge",0,0,32,16'd0)register_x1(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_x0), .o_d(RF_x1));
wire [N-1:0] RF_c1;
register #(1,"sync","posedge",0,0,32,16'd0)register_c1(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_c0), .o_d(RF_c1));
wire [N-1:0] RF_c2;
register #(1,"sync","posedge",0,0,32,16'd0)register_c2(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_c1), .o_d(RF_c2));
wire [N-1:0] RF_c3;
register #(1,"sync","posedge",0,0,32,16'd0)register_c3(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_c2), .o_d(RF_c3));
wire [63:0] in_A1;
assign in_A1 =  RF_a0* RF_b0;
wire [63:0] A1;
register #(1,"sync","posedge",0,0,64,32'd0)register_A1(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_A1), .o_d(A1));

wire [63:0] in_B2;
assign in_B2 = A1* RF_x1;
wire [63:0] B2;
register #(1,"sync","posedge",0,0,64,32'd0)register_B2(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_B2), .o_d(B2));

wire [63:0] in_C2;
assign in_C2 =  RF_31*A1;
wire [63:0] C2;
register #(1,"sync","posedge",0,0,64,32'd0)register_C2(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_C2), .o_d(C2));

wire [32:0] in_D3;
assign in_D3 = B2+C2;
wire [32:0] D3;
register #(1,"sync","posedge",0,0,33,32'd0)register_D3(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_D3), .o_d(D3));

wire [32:0] in_E4;
assign in_E4 = D3+ RF_c3;
wire [32:0] E4;
register #(1,"sync","posedge",0,0,33,32'd0)register_E4(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_E4), .o_d(E4));


wire [N-1:0] RF_Res_0;
register #(1,"sync","posedge",0,0,N,32'd0)register_RF_Res_0(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_E4[N*1-1:N*0]), .o_d(RF_Res_0));

wire [N-1:0] RF_Res_1;
register #(1,"sync","posedge",0,0,N,32'd0)register_RF_Res_1(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b0), .i_d(in_E4[N*2-1:N*1]), .o_d(RF_Res_1));

always@(posedge i_clk) begin
 case(i_addr)3'b000: begin
o_data <= RF_a0;
if(i_RF_WE == 1'b1) begin
RF_a0 <= i_data;
end
end

3'b001: begin
o_data <= RF_b0;
if(i_RF_WE == 1'b1) begin
RF_b0 <= i_data;
end
end

3'b010: begin
o_data <= RF_30;
if(i_RF_WE == 1'b1) begin
RF_30 <= i_data;
end
end

3'b011: begin
o_data <= RF_x0;
if(i_RF_WE == 1'b1) begin
RF_x0 <= i_data;
end
end

3'b100: begin
o_data <= RF_c0;
if(i_RF_WE == 1'b1) begin
RF_c0 <= i_data;
end
end

3'b101: begin
o_data <= RF_Res_0;
end
3'b110: begin
o_data <= RF_Res_1;
end
endcase
end
endmodule
