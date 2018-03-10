def partial_match_table(target, stop_flag):
    target = str(target)
    stop_flag = int(stop_flag)

    if stop_flag == 0:
        return 0
    else:
        if stop_flag == 1:
            if target[0] == target[1]:
                return 1
            else:
                return 0
        else:
            prefix = target[0]
            postfix = target[stop_flag]
            foward_list = [prefix]
            backward_list = [postfix]
            for i in range(1, stop_flag):
                foward_list.append(foward_list[-1] + target[i])
            for j in range(stop_flag - 1, 0, -1):
                backward_list.append(target[j] + backward_list[-1])
            foward_set = set(foward_list)
            backward_set = set(backward_list)
            intersection = foward_set.intersection(backward_set)
            # if len(intersection) == 0:
            #     return 0
            # else:
            #     return len(max(intersection))
            return len(max(intersection)) if len(intersection) > 0 else 0


def kmp(*args):
    suspect = str(args[0])
    target = str(args[1])
    suspect_length = len(suspect)
    target_length = len(target)
    found_index = 0
    for i in range(suspect_length):
        if suspect[i] == target[found_index]:
            found_index += 1
            if found_index == len(target):
                return "Found, and the index is {0}".format(i - target_length + 1)
            else:
                continue
        else:
            if found_index != 0:
                stop_flag = found_index - 1
                table_result = partial_match_table(target, stop_flag)
                # move the suspect forward, by using the table_result as its index
                while (suspect[i] != target[table_result]):
                    if table_result == 0:
                        break
                    else:
                        table_result = partial_match_table(target, stop_flag=table_result)
                if suspect[i] == target[table_result]:
                    found_index = table_result + 1
                else:
                    found_index = 0
    return False


if __name__ == '__main__':
    # long_one = input('Original String: ')
    # short_one = input('Target String: ')
    # kmp(long_one, short_one)
    print(kmp('BBC ABCDAB ABCDABCDABDE', 'ABCDABD'))
