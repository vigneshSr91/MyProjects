default_str=['0', '1'];
def concatenate_binary(arr, default_str):
    out_list = [];
    for str_bin in arr:
        for str_default in default_str:
            out_list.append(str_bin + str_default);
    return out_list;

def generate_binary(n):
    out_list = [];
    for i in range(1, n):
        if(len(out_list) == 0):
            out_list = concatenate_binary(default_str, default_str);
        else:
            out_list = concatenate_binary(out_list, default_str);
    return out_list;

if(__name__ == "__main__"):
    n = 4
    print(generate_binary(n), end=" ");
