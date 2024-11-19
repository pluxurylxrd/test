
print('\u001B[38;2;0;255;0m'' a  b a|b a^b a&b')
for a in range(2):
    for b in range(2):
        OR = a | b
        XOR = a ^ b
        AND = a & b
        print('\u001B[38;2;255;0;0m',a,'\u001B[38;2;0;0;255m',b,'\u001B[38;2;100;0;0m',OR, '\u001B[38;2;150;255;150m ',XOR, '\u001B[38;2;250;250;0m ',AND)