'''
$00	BRK	Implied	- - - - - - - 
$01	ORA ($NN,X)	Indexed Indirect	- Z- - - - N
$05	ORA $NN	Zero Page	- Z- - - - N
$06	ASL $NN	Zero Page	CZ- - - - N
$08	PHP	Implied	- - - - - - - 
$09	ORA #$NN	Immediate	- Z- - - - N
$0a	ASL A	Accumulator	CZ- - - - N
$0d	ORA $NNNN	Absolute	- Z- - - - N
$0e	ASL $NNNN	Absolute	CZ- - - - N
$10	BPL $NN	Relative	- - - - - - - 
$11	ORA ($NN),Y	Indirect Indexed	- Z- - - - N
$15	ORA $NN,X	Zero Page,X	- Z- - - - N
$16	ASL $NN,X	Zero Page,X	CZ- - - - N
$18	CLC	Implied	C- - - - - - 
$19	ORA $NNNN,Y	Absolute,Y	- Z- - - - N
$1d	ORA $NNNN,X	Absolute,X	- Z- - - - N
$1e	ASL $NNNN,X	Absolute,X	CZ- - - - N
$20	JSR $NNNN	Absolute	- - - - - - - 
$21	AND ($NN,X)	Indexed Indirect	- Z- - - - N
$24	BIT $NN	Zero Page	- Z- - - VN
$25	AND $NN	Zero Page	- Z- - - - N
$26	ROL $NN	Zero Page	CZ- - - - N
$28	PLP	Implied	CZIDBVN
$29	AND #$NN	Immediate	- Z- - - - N
$2a	ROL A	Accumulator	CZ- - - - N
$2c	BIT $NNNN	Absolute	- Z- - - VN
$2d	AND $NNNN	Absolute	- Z- - - - N
$2e	ROL $NNNN	Absolute	CZ- - - - N
$30	BMI $NN	Relative	- - - - - - - 
$31	AND ($NN),Y	Indirect Indexed	- Z- - - - N
$35	AND $NN,X	Zero Page,X	- Z- - - - N
$36	ROL $NN,X	Zero Page,X	CZ- - - - N
$38	SEC	Implied	C- - - - - - 
$39	AND $NNNN,Y	Absolute,Y	- Z- - - - N
$3d	AND $NNNN,X	Absolute,X	- Z- - - - N
$3e	ROL $NNNN,X	Absolute,X	CZ- - - - N
$40	RTI	Implied	- - - - - - - 
$41	EOR ($NN,X)	Indexed Indirect	- Z- - - - N
$45	EOR $NN	Zero Page	- Z- - - - N
$46	LSR $NN	Zero Page	CZ- - - - N
$48	PHA	Implied	- - - - - - - 
$49	EOR #$NN	Immediate	- Z- - - - N
$4a	LSR A	Accumulator	CZ- - - - N
$4c	JMP $NNNN	Absolute	- - - - - - - 
$4d	EOR $NNNN	Absolute	- Z- - - - N
$4e	LSR $NNNN	Absolute	CZ- - - - N
$50	BVC $NN	Relative	- - - - - - - 
$51	EOR ($NN),Y	Indirect Indexed	- Z- - - - N
$55	EOR $NN,X	Zero Page,X	- Z- - - - N
$56	LSR $NN,X	Zero Page,X	CZ- - - - N
$58	CLI	Implied	- - I- - - - 
$59	EOR $NNNN,Y	Absolute,Y	- Z- - - - N
$5d	EOR $NNNN,X	Absolute,X	- Z- - - - N
$5e	LSR $NNNN,X	Absolute,X	CZ- - - - N
$60	RTS	Implied	- - - - - - - 
$61	ADC ($NN,X)	Indexed Indirect	CZ- - - VN
$65	ADC $NN	Zero Page	CZ- - - VN
$66	ROR $NN	Zero Page	CZ- - - - N
$68	PLA	Implied	- Z- - - - N
$69	ADC #$NN	Immediate	CZ- - - VN
$6a	ROR A	Accumulator	CZ- - - - N
$6c	JMP $NN	Indirect	- - - - - - - 
$6d	ADC $NNNN	Absolute	CZ- - - VN
$6e	ROR $NNNN,X	Absolute,X	CZ- - - - N
$70	BVS $NN	Relative	- - - - - - - 
$71	ADC ($NN),Y	Indirect Indexed	CZ- - - VN
$75	ADC $NN,X	Zero Page,X	CZ- - - VN
$76	ROR $NN,X	Zero Page,X	CZ- - - - N
$78	SEI	Implied	- - I- - - - 
$79	ADC $NNNN,Y	Absolute,Y	CZ- - - VN
$7d	ADC $NNNN,X	Absolute,X	CZ- - - VN
$7e	ROR $NNNN	Absolute	CZ- - - - N
$81	STA ($NN,X)	Indexed Indirect	- - - - - - - 
$84	STY $NN	Zero Page	- - - - - - - 
$85	STA $NN	Zero Page	- - - - - - - 
$86	STX $NN	Zero Page	- - - - - - - 
$88	DEY	Implied	- Z- - - - N
$8a	TXA	Implied	- Z- - - - N
$8c	STY $NNNN	Absolute	- - - - - - - 
$8d	STA $NNNN	Absolute	- - - - - - - 
$8e	STX $NNNN	Absolute	- - - - - - - 
$90	BCC $NN	Relative	- - - - - - - 
$91	STA ($NN),Y	Indirect Indexed	- - - - - - - 
$94	STY $NN,X	Zero Page,X	- - - - - - - 
$95	STA $NN,X	Zero Page,X	- - - - - - - 
$96	STX $NN,Y	Zero Page,Y	- - - - - - - 
$98	TYA	Implied	- Z- - - - N
$99	STA $NNNN,Y	Absolute,Y	- - - - - - - 
$9a	TXS	Implied	- - - - - - - 
$9d	STA $NNNN,X	Absolute,X	- - - - - - - 
$a0	LDY #$NN	Immediate	- Z- - - - N
$a1	LDA ($NN,X)	Indexed Indirect	- Z- - - - N
$a2	LDX #$NN	Immediate	- Z- - - - N
$a4	LDY $NN	Zero Page	- Z- - - - N
$a5	LDA $NN	Zero Page	- Z- - - - N
$a6	LDX $NN	Zero Page	- Z- - - - N
$a8	TAY	Implied	- Z- - - - N
$a9	LDA #$NN	Immediate	- Z- - - - N
$aa	TAX	Implied	- Z- - - - N
$ac	LDY $NNNN	Absolute	- Z- - - - N
$ad	LDA $NNNN	Absolute	- Z- - - - N
$ae	LDX $NNNN	Absolute	- Z- - - - N
$b0	BCS $NN	Relative	- - - - - - - 
$b1	LDA ($NN),Y	Indirect Indexed	- Z- - - - N
$b4	LDY $NN,X	Zero Page,X	- Z- - - - N
$b5	LDA $NN,X	Zero Page,X	- Z- - - - N
$b6	LDX $NN,Y	Zero Page,Y	- Z- - - - N
$b8	CLV	Implied	- - - - - V- 
$b9	LDA $NNNN,Y	Absolute,Y	- Z- - - - N
$ba	TSX	Implied	- Z- - - - N
$bc	LDY $NNNN,X	Absolute,X	- Z- - - - N
$bd	LDA $NNNN,X	Absolute,X	- Z- - - - N
$be	LDX $NNNN,Y	Absolute,Y	- Z- - - - N
$c0	CPY #$NN	Immediate	CZ- - - - N
$c1	CMP ($NN,X)	Indexed Indirect	CZ- - - - N
$c4	CPY $NN	Zero Page	CZ- - - - N
$c5	CMP $NN	Zero Page	CZ- - - - N
$c6	DEC $NN	Zero Page	- Z- - - - N
$c8	INY	Implied	- Z- - - - N
$c9	CMP #$NN	Immediate	CZ- - - - N
$ca	DEX	Implied	- Z- - - - N
$cc	CPY $NNNN	Absolute	CZ- - - - N
$cd	CMP $NNNN	Absolute	CZ- - - - N
$ce	DEC $NNNN	Absolute	- Z- - - - N
$d0	BNE $NN	Relative	- - - - - - - 
$d1	CMP ($NN),Y	Indirect Indexed	CZ- - - - N
$d5	CMP $NN,X	Zero Page,X	CZ- - - - N
$d6	DEC $NN,X	Zero Page,X	- Z- - - - N
$d8	CLD	Implied	- - - D- - - 
$d9	CMP $NNNN,Y	Absolute,Y	CZ- - - - N
$dd	CMP $NNNN,X	Absolute,X	CZ- - - - N
$de	DEC $NNNN,X	Absolute,X	- Z- - - - N
$e0	CPX #$NN	Immediate	CZ- - - - N
$e1	SBC ($NN,X)	Indexed Indirect	CZ- - - VN
$e4	CPX $NN	Zero Page	CZ- - - - N
$e5	SBC $NN	Zero Page	CZ- - - VN
$e6	INC $NN	Zero Page	- Z- - - - N
$e8	INX	Implied	- Z- - - - N
$e9	SBC #$NN	Immediate	CZ- - - VN
$ea	NOP	Implied	- - - - - - - 
$ec	CPX $NNNN	Absolute	CZ- - - - N
$ed	SBC $NNNN	Absolute	CZ- - - VN
$ee	INC $NNNN	Absolute	- Z- - - - N
$f0	BEQ $NN	Relative	- - - - - - - 
$f1	SBC ($NN),Y	Indirect Indexed	CZ- - - VN
$f5	SBC $NN,X	Zero Page,X	CZ- - - VN
$f6	INC $NN,X	Zero Page,X	- Z- - - - N
$f8	SED	Implied	- - - D- - - 
$f9	SBC $NNNN,Y	Absolute,Y	CZ- - - VN
$fd	SBC $NNNN,X	Absolute,X	CZ- - - VN
$fe	INC $NNNN,X	Absolute,X	- Z- - - - N
'''

d = {
    '00': 'BRK',
    '01': 'ORA',
    '05': 'ORA',
    '06': 'ASL',
    '08': 'PHP',
    '09': 'ORA',
    '0a': 'ASL',
    '0d': 'ORA',
    '0e': 'ASL',
    '10': 'BPL',
    '11': 'ORA',
    '15': 'ORA',
    '16': 'ASL',
    '18': 'CLC',
    '19': 'ORA',
    '1d': 'ORA',
    '1e': 'ASL',
    '20': 'JSR',
    '21': 'AND',
    '24': 'BIT',
    '25': 'AND',
    '26': 'ROL',
    '28': 'PLP',
    '29': 'AND',
    '2a': 'ROL',
    '2c': 'BIT',
    '2d': 'AND',
    '2e': 'ROL',
    '30': 'BMI',
    '31': 'AND',
    '35': 'AND',
    '36': 'ROL',
    '38': 'SEC',
    '39': 'AND',
    '3d': 'AND',
    '3e': 'ROL',
    '40': 'RTI',
    '41': 'EOR',
    '45': 'EOR',
    '46': 'LSR',
    '48': 'PHA',
    '49': 'EOR',
    '4a': 'LSR',
    '4c': 'JMP',
    '4d': 'EOR',
    '4e': 'LSR',
    '50': 'BVC',
    '51': 'EOR',
    '55': 'EOR',
    '56': 'LSR',
    '58': 'CLI',
    '59': 'EOR',
    '5d': 'EOR',
    '5e': 'LSR',
    '60': 'RTS',
    '61': 'ADC',
    '65': 'ADC',
    '66': 'ROR',
    '68': 'PLA',
    '69': 'ADC',
    '6a': 'ROR',
    '6c': 'JMP',
    '6d': 'ADC',
    '6e': 'ROR',
    '70': 'BVS',
    '71': 'ADC',
    '75': 'ADC',
    '76': 'ROR',
    '78': 'SEI',
    '79': 'ADC',
    '7d': 'ADC',
    '7e': 'ROR',
    '81': 'STA',
    '84': 'STY',
    '85': 'STA',
    '86': 'STX',
    '88': 'DEY',
    '8a': 'TXA',
    '8c': 'STY',
    '8d': 'STA',
    '8e': 'STX',
    '90': 'BCC',
    '91': 'STA',
    '94': 'STY',
    '95': 'STA',
    '96': 'STX',
    '98': 'TYA',
    '99': 'STA',
    '9a': 'TXS',
    '9d': 'STA',
    'a0': 'LDY',
    'a1': 'LDA',
    'a2': 'LDX',
    'a4': 'LDY',
    'a5': 'LDA',
    'a6': 'LDX',
    'a8': 'TAY',
    'a9': 'LDA',
    'aa': 'TAX',
    'ac': 'LDY',
    'ad': 'LDA',
    'ae': 'LDX',
    'b0': 'BCS',
    'b1': 'LDA',
    'b4': 'LDY',
    'b5': 'LDA',
    'b6': 'LDX',
    'b8': 'CLV',
    'b9': 'LDA',
    'ba': 'TSX',
    'bc': 'LDY',
    'bd': 'LDA',
    'be': 'LDX',
    'c0': 'CPY',
    'c1': 'CMP',
    'c4': 'CPY',
    'c5': 'CMP',
    'c6': 'DEC',
    'c8': 'INY',
    'c9': 'CMP',
    'ca': 'DEX',
    'cc': 'CPY',
    'cd': 'CMP',
    'ce': 'DEC',
    'd0': 'BNE',
    'd1': 'CMP',
    'd5': 'CMP',
    'd6': 'DEC',
    'd8': 'CLD',
    'd9': 'CMP',
    'dd': 'CMP',
    'de': 'DEC',
    'e0': 'CPX',
    'e1': 'SBC',
    'e4': 'CPX',
    'e5': 'SBC',
    'e6': 'INC',
    'e8': 'INX',
    'e9': 'SBC',
    'ea': 'NOP',
    'ec': 'CPX',
    'ed': 'SBC',
    'ee': 'INC',
    'f0': 'BEQ',
    'f1': 'SBC',
    'f5': 'SBC',
    'f6': 'INC',
    'f8': 'SED',
    'f9': 'SBC',
    'fd': 'SBC',
    'fe': 'INC',
}

d_bytes = {
    '00': 1,
    '01': 3,
    '05': 2,
    '06': 2,
    '08': 1,
    '09': 2,
    '0a': 2,
    '0d': 2,
    '0e': 2,
    '10': 2,
    '11': 3,
    '15': 3,
    '16': 3,
    '18': 1,
    '19': 3,
    '1d': 3,
    '1e': 3,
    '20': 2,
    '21': 3,
    '24': 2,
    '25': 2,
    '26': 2,
    '28': 1,
    '29': 2,
    '2a': 2,
    '2c': 2,
    '2d': 2,
    '2e': 2,
    '30': 2,
    '31': 3,
    '35': 3,
    '36': 3,
    '38': 1,
    '39': 3,
    '3d': 3,
    '3e': 3,
    '40': 1,
    '41': 3,
    '45': 2,
    '46': 2,
    '48': 1,
    '49': 2,
    '4a': 2,
    '4c': 2,
    '4d': 2,
    '4e': 2,
    '50': 2,
    '51': 3,
    '55': 3,
    '56': 3,
    '58': 1,
    '59': 3,
    '5d': 3,
    '5e': 3,
    '60': 1,
    '61': 3,
    '65': 2,
    '66': 2,
    '68': 1,
    '69': 2,
    '6a': 2,
    '6c': 2,
    '6d': 2,
    '6e': 3,
    '70': 2,
    '71': 3,
    '75': 3,
    '76': 3,
    '78': 1,
    '79': 3,
    '7d': 3,
    '7e': 2,
    '81': 3,
    '84': 2,
    '85': 2,
    '86': 2,
    '88': 1,
    '8a': 1,
    '8c': 2,
    '8d': 3,
    '8e': 2,
    '90': 2,
    '91': 3,
    '94': 3,
    '95': 3,
    '96': 3,
    '98': 1,
    '99': 3,
    '9a': 1,
    '9d': 3,
    'a0': 2,
    'a1': 3,
    'a2': 2,
    'a4': 2,
    'a5': 2,
    'a6': 2,
    'a8': 1,
    'a9': 2,
    'aa': 1,
    'ac': 2,
    'ad': 3,
    'ae': 2,
    'b0': 2,
    'b1': 3,
    'b4': 3,
    'b5': 3,
    'b6': 3,
    'b8': 1,
    'b9': 3,
    'ba': 1,
    'bc': 3,
    'bd': 3,
    'be': 3,
    'c0': 2,
    'c1': 3,
    'c4': 2,
    'c5': 2,
    'c6': 2,
    'c8': 1,
    'c9': 2,
    'ca': 1,
    'cc': 2,
    'cd': 2,
    'ce': 2,
    'd0': 2,
    'd1': 3,
    'd5': 3,
    'd6': 3,
    'd8': 1,
    'd9': 3,
    'dd': 3,
    'de': 3,
    'e0': 2,
    'e1': 3,
    'e4': 2,
    'e5': 2,
    'e6': 2,
    'e8': 1,
    'e9': 2,
    'ea': 1,
    'ec': 2,
    'ed': 2,
    'ee': 2,
    'f0': 2,
    'f1': 3,
    'f5': 3,
    'f6': 3,
    'f8': 1,
    'f9': 3,
    'fd': 3,
    'fe': 3,
}