N = 16
bites = 3


with open('/home/paro/Desktop/project/rtl.v','w') as inf:
    inf.write('`timescale 1ns/100ps\n\n')
    inf.write('module test_top();\n')
    s_1 = 'localparam N = ' + str(N) + '\n' + 'localparam RF_Addr_BITNES = ' + str(bites) + '\n'
    inf.write(s_1)
    inf.write('reg clk = 0;\nreg reset = 0;\n')
    inf.write('always begin #5; clk <= ~clk; end\n')
    inf.write('initial begin\nreset <= 1\'b0;\n#20;')
    inf.write('reset <= 1\'b1;\n#40;\nreset <= 1\'b0;\nend\n')




