import multiprocessing
from .recursive_merge_sort import copy_merge as merge
from .recursive_merge_sort import recursive_merge_sort as merge_sort


def parallel_merge_sort(vector, count_slice=0, self_id=1, return_dict=None):
    if return_dict == None:
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        count_slice = multiprocessing.cpu_count()
        self_id = 1
    else:
        pass
    return_dict[self_id] = vector
    if count_slice >= 2:
        right_side_p = multiprocessing.Process(
            target=parallel_merge_sort,
            args=(
                return_dict[self_id][len(return_dict[self_id])//2:],
                count_slice-(count_slice//2),
                (self_id*2)+1,
                return_dict
                )
            )
        right_side_p.start()
        left_side = parallel_merge_sort(return_dict[self_id][:len(return_dict[self_id])//2], (count_slice//2), self_id*2, return_dict)
        right_side_p.join()
        return_dict[self_id] = merge(return_dict[self_id*2], return_dict[self_id*2+1])
    else:
        return_dict[self_id] = merge_sort(vector)

    return return_dict[self_id]
