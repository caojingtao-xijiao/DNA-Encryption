# 解码并解密
# 读取碱基文件
def read_base_file(base_path):
    with open(base_path, 'r') as f:
        base_seq = f.read()
    return base_seq
# 碱基序列转为二进制
def base_to_bin(base_seq_strings):
    map_rule = {
        'A': '00',
        'G': '01',
        'C': '10',
        'T': '11',
    }
    bin_lst = []
    for i in base_seq_strings:
        bin_lst.append(map_rule[i])
    return ''.join(bin_lst)
# 解密
def decryption(bin_strings, bin_key):
    # 计算两者的长度
    bin_strs_length = len(bin_strings)
    bin_key_length = len(bin_key)
    # 将密钥转为整数
    int_key = int(bin_key, 2)
    print(int_key)
    encryption_lst = []
    for i in range(0, bin_strs_length, bin_key_length):
        bin_slice = bin_strings[i:i + bin_key_length]
        int_slices = int(bin_slice, 2)
        if len(bin_slice) == bin_key_length:
            encryption_results = bin(int_slices ^ int_key)[2:].zfill(len(bin_slice))
            encryption_lst.append(encryption_results)
        else:
            bin_key_slice = bin_key[:len(bin_slice)]
            int_key_slice = int(bin_key_slice, 2)
            encryption_results = bin(int_slices ^ int_key_slice)[2:].zfill(len(bin_slice))
            encryption_lst.append(encryption_results)
    return ''.join(encryption_lst)


# ASCII二进制码转文本
def ascii_binary_to_text(bin_strings):
    char_lst = []
    for i in range(0, len(bin_strings), 8):
        char = chr(int(bin_strings[i:i + 8], 2))
        char_lst.append(char)
    return ''.join(char_lst)


#保存文本文件
def save_text_file(text_strings, text_path,line_break_node_lst):
    with open(text_path, 'w',encoding='utf-8') as f:
        # f.write(text_strings)
        count = 1
        for i in line_break_node_lst:
            f.write(str(count)+f'{text_strings[i[0]:i[1]]}\n')
            # print(f'{text[i[0]:i[1]]}\n')
            count += 1


def read_text_file_per_row(info_path):
    with open(info_path,'r') as f:
        text_lst = f.readlines()
    return text_lst

# 解密函数，返回解密后的文本
def info_decryp(base_path, base_key,text_path,line_break_node_lst):
    # 读取碱基序列文件
    base_seq = read_base_file(base_path)
    # 碱基序列转二进制序列
    undecrypted_bin = base_to_bin(base_seq)
    # 密钥碱基序列转二进制序列
    bin_key = base_to_bin(base_key)
    # 解密为二进制序列
    decrypted_bin = decryption(undecrypted_bin, bin_key)
    # 转文本
    text = ascii_binary_to_text(decrypted_bin)
    # 保存文本文件
    save_text_file(text, text_path,line_break_node_lst)
    # 逐行打印
    count = 1
    for i in line_break_node_lst:
        print(count)
        print(f'{text[i[0]:i[1]]}\n')
        count += 1


if __name__ == '__main__':
    info_path = '../data/Raw_data/Sonnet_18.txt'
    #获取位点
    text_lst = read_text_file_per_row(info_path)
    print(text_lst)
    line_break_node_lst = []
    for i in text_lst:
        line_break_node_lst.append(len(i))
    print(line_break_node_lst)
    tuple_line_break_lst = []
    count = 0
    for i in range(len(line_break_node_lst)):
        tuple_tmp = (count,count+line_break_node_lst[i])
        count += line_break_node_lst[i]
        tuple_line_break_lst.append(tuple_tmp)
    print(tuple_line_break_lst)

    info_path = '../data/Encrypted_data/Sonnet_18_encryp.txt'
    base_key = 'TCGGTTTGATAGAAAACATGTGGCGAGTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGC'
    base_path = '../data/Decrypted_data/Sonnet_18_decryp.txt'
    wrong_key = 'GTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGCTCGGTTTGATAGAAAACATGTGGCGA'
    wrong_decryp = '../data/Decrypted_data/Sonnet_18_decryp_wrong_1.txt'
    info_decryp(info_path, base_key, base_path,tuple_line_break_lst)
    info_decryp(info_path, wrong_key, wrong_decryp,tuple_line_break_lst)

    # 获取位点
    info_path = '../data/Raw_data/Prelude_to_Water_Melody.txt'
    text_lst = read_text_file_per_row(info_path)
    line_break_node_lst = []
    for i in text_lst:
        line_break_node_lst.append(len(i))
    tuple_line_break_lst = []
    count = 0
    for i in range(len(line_break_node_lst)):
        tuple_tmp = (count, count + line_break_node_lst[i])
        count += line_break_node_lst[i]
        tuple_line_break_lst.append(tuple_tmp)
    print(tuple_line_break_lst)
    info_path = '../data/Encrypted_data/Prelude_to_Water_Melody_encryp.txt'
    base_key = 'GTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGCTCGGTTTGATAGAAAACATGTGGCGA'
    base_path = '../data/Decrypted_data/Prelude_to_Water_Melody_decryp.txt'
    wrong_key = 'TCGGTTTGATAGAAAACATGTGGCGAGTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGC'
    wrong_decryp = '../data/Decrypted_data/Prelude_to_Water_Melody_decryp_wrong_1.txt'
    info_decryp(info_path, base_key, base_path,tuple_line_break_lst)
    info_decryp(info_path, wrong_key, wrong_decryp,tuple_line_break_lst)