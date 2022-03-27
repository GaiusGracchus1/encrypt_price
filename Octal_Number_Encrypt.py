from random import randint

def convert_oct_value(value):
    value_str = '%.2f' % value
    # Convert int to oct letter
    value_int_conv_oct = oct(int(value))[2:]
    value_int_conv_ltr = [chr(ord('`') + (int(char) + 1)) for char in value_int_conv_oct]
    value_int_conv_fin = ''
    for item in value_int_conv_ltr:
        value_int_conv_fin += '' + item
    # Convert decimal to oct letter
    value_dec_conv_str = oct(int(value_str[-2:]))[2:]
    value_dec_conv = [chr(ord('`') + (int(char) + 1)) for char in value_dec_conv_str]
    value_dec_conv_fin = ''
    for item in value_dec_conv:
        value_dec_conv_fin += '' + item
    # Combine int and decimal
    value_conv_plain = value_dec_conv_fin + '+' + value_int_conv_fin
    # Add random letters
    rand_1 = chr(ord('`') + randint(1, 26))
    rand_2 = chr(ord('`') + randint(1, 26))
    rand_3 = chr(ord('`') + randint(1, 26))
    rand_4 = chr(ord('`') + randint(1, 26))
    value_conv = rand_1 + rand_2 + value_conv_plain + rand_3 + rand_4
    return(value_conv)

def translate_value(value_conv):
    value_conv_split = value_conv[2:-2].split('+')
    value_dec_trans_ltr = ''
    for char in value_conv_split[0]:
        value_dec_trans_ltr += '' + str(ord(char) - 97)
    value_int_trans_ltr = ''
    for char in value_conv_split[1]:
        value_int_trans_ltr += '' + str(ord(char) - 97)
    value_int_trans = int(value_int_trans_ltr, 8)
    value_dec_trans = int(value_dec_trans_ltr, 8)
    value_trans = value_int_trans + (value_dec_trans / 100)
    return(value_trans)

value = 199.99
value_convert = convert_oct_value(value)
value_translate = translate_value(value_convert)

print(f'''
value given: {value}
value converted: {value_convert}
value translated back: {value_translate}
''')
