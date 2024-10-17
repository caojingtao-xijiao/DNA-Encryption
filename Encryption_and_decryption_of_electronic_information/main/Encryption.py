#加密并编码
#读取文本文件
def read_text_file(info_path):
    with open(info_path, 'r') as f:
        text = f.read()
    return text
#文本转换为二进制ASCII码
def text_to_ascii_binary(text):
    #将文本中的每个字符转换为其对应的ASCII值，并转为8位二进制字符串
    binary_strings = [format(ord(char), '08b') for char in text]
    return ''.join(binary_strings)
# 加密函数(异或加密)
def encryption(bin_strings,bin_key):
    #计算两者的长度
    bin_strs_length = len(bin_strings)
    bin_key_length = len(bin_key)
    #将密钥转为整数
    int_key = int(bin_key,2)
    encryption_lst = []
    for i in range(0,bin_strs_length,bin_key_length):
        bin_slice = bin_strings[i:i+bin_key_length]
        int_slices = int(bin_slice, 2)
        if len(bin_slice) == bin_key_length:
            encryption_results = bin(int_slices ^ int_key)[2:].zfill(len(bin_slice))
            encryption_lst.append(encryption_results)
        else:
            bin_key_slice = bin_key[:len(bin_slice)]
            int_key_slice = int(bin_key_slice,2)
            encryption_results = bin(int_slices ^ int_key_slice)[2:].zfill(len(bin_slice))
            encryption_lst.append(encryption_results)
    return ''.join(encryption_lst)
#二进制ASCII码转碱基序列
def binary_base_transfer_sequence(bin_strings):
    map_rule = {
        '00':'A',
        '01': 'G',
        '10': 'C',
        '11': 'T'
    }
    base_lst = []
    for i in range(0,len(bin_strings),2):
        bin_slice = bin_strings[i:i+2]
        base_lst.append(map_rule[bin_slice])
    return ''.join(base_lst)
#保存碱基文件
def save_base_seq_file(base_strings,save_path):
    with open(save_path,'w') as f:
        f.write(base_strings)
def base_to_bin(base_seq_strings):
    map_rule = {
        'A':'00',
        'G':'01',
        'C':'10',
        'T':'11',
    }
    bin_lst = []
    for i in base_seq_strings:
        bin_lst.append(map_rule[i])
    return ''.join(bin_lst)

def text_encryp(raw_text_path,base_key,base_save_path):
    # 读取文件
    text = read_text_file(raw_text_path)
    # 文本转二进制ASCII码
    unencrypted_bin = text_to_ascii_binary(text)
    # 加密
    bin_key = base_to_bin(base_key)
    encrypted_bin = encryption(unencrypted_bin,bin_key)
    # 转DNA序列
    encrypted_base = binary_base_transfer_sequence(encrypted_bin)
    # 保存DNA序列
    save_base_seq_file(encrypted_base,base_save_path)
    print(encrypted_base)

if __name__ == '__main__':
    raw_text_path = '../data/Raw_data/Sonnet_18.txt'
    base_key = 'TCGGTTTGATAGAAAACATGTGGCGAGTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGC'
    base_save_path = '../data/Encrypted_data/Sonnet_18_encryp.txt'
    text_encryp(raw_text_path,base_key,base_save_path)

    raw_text_path = '../data/Raw_data/Prelude_to_Water_Melody.txt'
    base_key = 'GTGCCGTAGGAGAAGTGACCGCACGCGACTCCGACCAGAACGTACGCATTGTGGTCGTGGTTGCAAGTACCGACATAGCATGCGGACCAGAAACGCTTGTATGCTCGGTTTGATAGAAAACATGTGGCGA'
    base_save_path = '../data/Encrypted_data/Prelude_to_Water_Melody_encryp.txt'
    text_encryp(raw_text_path, base_key, base_save_path)