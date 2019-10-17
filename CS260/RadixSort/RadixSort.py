from Stack import Stack

def radix_sort(int_values):
    bins = [None] * 10
    for i in range(10):
        bins[i] = Stack()
    ptr = 0
    max_digit_len = 0
    for item in int_values:
        if len(str(item))>max_digit_len:
            max_digit_len=len(str(item))
    for i in range(max_digit_len):
        for item in int_values:
            s = str(item).rjust(max_digit_len,'0')
            i = s[len(s)-(ptr+1)]
            bins[int(i)].push(item)
        int_values = []
        for item in bins:
            item.reverse()
            while not item.isEmpty():
                int_values.append(item.pop())
        ptr = ptr + 1
    return int_values

if __name__=="__main__":
    my_list = [53,89,150,36,633,233]
    sorted_list=radix_sort(my_list)
    print(sorted_list)