# R Types #
add_ = 'add'
addu_ = 'addu'
and_ = 'and'
break_ = 'break'
div_ = 'div'
divu_ = 'divu'
jalr_ = 'jalr'
jr_ = 'jr'
mfhi_ = 'mfhi'
mflo_ = 'mflo'
mthi_ = 'mthi'
mtlo_ = 'mtlo'
mult_ = 'mult'
multu_ = 'multu'
nor_ = 'nor'
or_ = 'or'
sll_ = 'sll'
sllv_ = 'sllv'
slt_ = 'slt'
sltu_ = 'sltu'
sra_ = 'sra'
srav_ = 'srav'
srl_ = 'srl'
srlv_ = 'srlv'
sub_ = 'sub'
subu_ = 'subu'
syscall_ = 'syscall'
xor_ = 'xor'

# I Types #
addi_ = 'addi'
addiu_ = 'addiu'
andi_ = 'andi'
beq_ = 'beq'
bgez_ = 'bgez'
bgtz_ = 'bgtz'
blez_ = 'blez'
bltz_ = 'bltz'
bne_ = 'bne'
lb_ = 'lb'
lbu_ = 'lbu'
lh_ = 'lh'
lhu_ = 'lhu'
lui_ = 'lui'
lw_ = 'lw'
lwc1_ = 'lwc1'
ori_ = 'ori'
sb_ = 'sb'
slti_ = 'slti'
sltiu_ = 'sltiu'
sh_ = 'sh'
sw_ = 'sw'
swc1_ = 'swc1'
xori_ = 'xori'

# J Types #
j_ = 'j'
jal_ = 'jal'

opcodes = dict([
    # R Types #
    (add_,      0b000_000),
    (addu_,     0b000_000),
    (and_,      0b000_000),
    (break_,    0b000_000),
    (div_,      0b000_000),
    (divu_,     0b000_000),
    (jalr_,     0b000_000),
    (jr_,       0b000_000),
    (mfhi_,     0b000_000),
    (mflo_,     0b000_000),
    (mthi_,     0b000_000),
    (mtlo_,     0b000_000),
    (mult_,     0b000_000),
    (multu_,    0b000_000),
    (nor_,      0b000_000),
    (or_,       0b000_000),
    (sll_,      0b000_000),
    (sllv_,     0b000_000),
    (slt_,      0b000_000),
    (sltu_,     0b000_000),
    (sra_,      0b000_000),
    (srav_,     0b000_000),
    (srl_,      0b000_000),
    (srlv_,     0b000_000),
    (sub_,      0b000_000),
    (subu_,     0b000_000),
    (syscall_,  0b000_000),
    (xor_,      0b000_000),
    # I Types #
    (addi_,     0b001_000),
    (addiu_,    0b001_001),
    (andi_,     0b001_100),
    (beq_,      0b000_100),
    (bgez_,     0b000_001),
    (bgtz_,     0b000_111),
    (blez_,     0b000_110),
    (bltz_,     0b000_001),
    (bne_,      0b000_101),
    (lb_,       0b100_000),
    (lbu_,      0b100_100),
    (lh_,       0b100_001),
    (lhu_,      0b100_101),
    (lui_,      0b001_111),
    (lw_,       0b100_011),
    (lwc1_,     0b110_001),
    (ori_,      0b001_101),
    (sb_,       0b101_000),
    (slti_,     0b001_010),
    (sltiu_,    0b001_011),
    (sh_,       0b101_001),
    (sw_,       0b101_011),
    (swc1_,     0b111_001),
    (xori_,     0b001_110),
    # J Types #
    (j_,        0b000_010),
    (jal_,      0b000_011)
])


rd = 'rd'
rs = 'rs'
rt = 'rt'
sa = 'sa'
imm = 'immediate'
tgt = 'target_address'
fun = 'funct'
opc = 'opcode'

instruction_machinecode_orders = dict([
    (add_,      {opc: 0b000_000, sa: 0, fun: 0b100_000}),
    (addu_,     {opc: 0b000_000, sa: 0, fun: 0b100_001}),
    (and_,      {opc: 0b000_000, sa: 0, fun: 0b100_100}),
    (break_,    {opc: 0b000_000, rd: 0, rs: 0, rt: 0, sa: 0, fun: 0b001_101}),
    (div_,      {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_010}),
    (divu_,     {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_011}),
    (jalr_,     {opc: 0b000_000, rt: 0, sa: 0, fun: 0b001_001}),
    (jr_,       {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b001_000}),
    (mfhi_,     {opc: 0b000_000, rs: 0, rt: 0, sa: 0, fun: 0b010_000}),
    (mflo_,     {opc: 0b000_000, rs: 0, rt: 0, sa: 0, fun: 0b010_010}),
    (mthi_,     {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b010_001}),
    (mtlo_,     {opc: 0b000_000, rd: 0, rt: 0, sa: 0, fun: 0b010_011}),
    (mult_,     {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_000}),
    (multu_,    {opc: 0b000_000, rd: 0, sa: 0, fun: 0b011_001}),
    (nor_,      {opc: 0b000_000, sa: 0, fun: 0b100_111}),
    (or_,       {opc: 0b000_000, sa: 0, fun: 0b100_101}),
    (sll_,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (sllv_,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (slt_,      {opc: 0b000_000, sa: 0, fun: 0b101_010}),
    (sltu_,     {opc: 0b000_000, sa: 0, fun: 0b101_011}),
    (sra_,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (srav_,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (srl_,      {opc: 0b000_000, rs: 0, fun: 0b011_000}),
    (srlv_,     {opc: 0b000_000, sa: 0, fun: 0b011_000}),
    (sub_,      {opc: 0b000_000, sa: 0, fun: 0b100_010}),
    (subu_,     {opc: 0b000_000, sa: 0, fun: 0b100_011}),
    (syscall_,  {opc: 0b000_000, rd: 0, rs: 0, rt: 0, sa: 0, fun: 0b001_100}),
    (xor_,      {opc: 0b000_000, sa: 0, fun: 0b10_0110}),

    (addi_,     {opc: 0b001_000}),
    (addiu_,    {opc: 0b001_001}),
    (andi_,     {opc: 0b001_100}),
    (beq_,      {opc: 0b000_100}),
    (bgez_,     {opc: 0b000_001, rt: 0}),
    (bgtz_,     {opc: 0b000_111, rt: 0}),
    (blez_,     {opc: 0b000_110, rt: 0}),
    (bltz_,     {opc: 0b000_001, rt: 0}),
    (bne_,      {opc: 0b000_101}),
    (lb_,       {opc: 0b100_000}),
    (lbu_,      {opc: 0b100_100}),
    (lh_,       {opc: 0b100_001}),
    (lhu_,      {opc: 0b100_101}),
    (lui_,      {opc: 0b001_111}),
    (lw_,       {opc: 0b100_011}),
    (lwc1_,     {opc: 0b110_001}),
    (ori_,      {opc: 0b001_101}),
    (sb_,       {opc: 0b101_000, rs: 0}),
    (slti_,     {opc: 0b001_010}),
    (sltiu_,    {opc: 0b001_011}),
    (sh_,       {opc: 0b101_001, rs: 0}),
    (sw_,       {opc: 0b101_011, rs: 0}),
    (swc1_,     {opc: 0b111_001, rs: 0}),
    (xori_,     {opc: 0b001_110}),

    (j_,        {opc: 0b000_010}),
    (jal_,      {opc: 0b000_011})
])

instruction_assembly_orders = dict([
    (add_,      [opc, rd, rs, rt, fun]),
    (addu_,     [opc, rd, rs, rt, fun]),
    (and_,      [opc, rd, rs, rt, fun]),
    (break_,    [opc, fun]),
    (div_,      [opc, rs, rt, fun]),
    (divu_,     [opc, rs, rt, fun]),
    (jalr_,     [opc, rd, rs, fun]),
    (jr_,       [opc, rs, fun]),
    (mfhi_,     [opc, rd, fun]),
    (mflo_,     [opc, rd, fun]),
    (mthi_,     [opc, rs, fun]),
    (mtlo_,     [opc, rs, fun]),
    (mult_,     [opc, rs, rt, fun]),
    (multu_,    [opc, rs, rt, fun]),
    (nor_,      [opc, rd, rs, rt, fun]),
    (or_,       [opc, rd, rs, rt, fun]),
    (sll_,      [opc, rd, rt, sa, fun]),
    (sllv_,     [opc, rd, rt, rs, fun]),
    (slt_,      [opc, rd, rs, rt, fun]),
    (sltu_,     [opc, rd, rs, rt, fun]),
    (sra_,      [opc, rd, rt, sa, fun]),
    (srav_,     [opc, rd, rt, rs, fun]),
    (srl_,      [opc, rd, rt, sa, fun]),
    (srlv_,     [opc, rd, rt, rs, fun]),
    (sub_,      [opc, rd, rs, rt, fun]),
    (subu_,     [opc, rd, rs, rt, fun]),
    (syscall_,  [opc, fun]),
    (xor_,      [opc, rd, rs, rt, fun]),

    (addi_,     [opc, rt, rs, imm]),
    (addiu_,    [opc, rt, rs, imm]),
    (andi_,     [opc, rt, rs, imm]),
    (beq_,      [opc, rs, rt, imm]),
    (bgez_,     [opc, rs, imm]),
    (bgtz_,     [opc, rs, imm]),
    (blez_,     [opc, rs, imm]),
    (bltz_,     [opc, rs, imm]),
    (bne_,      [opc, rs, rt, imm]),
    (lb_,       [opc, rt, rs, imm]),
    (lbu_,      [opc, rt, rs, imm]),
    (lh_,       [opc, rt, rs, imm]),
    (lhu_,      [opc, rt, rs, imm]),
    (lui_,      [opc, rt, imm]),
    (lw_,       [opc, rt, rs, imm]),
    (lwc1_,     [opc, rt, rs, imm]),
    (ori_,      [opc, rt, rs, imm]),
    (sb_,       [opc, rt, rs, imm]),
    (slti_,     [opc, rt, rs, imm]),
    (sltiu_,    [opc, rt, rs, imm]),
    (sh_,       [opc, rt, rs, imm]),
    (sw_,       [opc, rt, rs, imm]),
    (swc1_,     [opc, rt, imm]),
    (xori_,     [opc, rt, rs, imm]),

    (j_,        [opc, tgt]),
    (jal_,      [opc, tgt])
])
