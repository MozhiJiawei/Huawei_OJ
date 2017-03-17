"""
记票统计（100分）
"""


def get_vote_result(candidate_name: list, vote_name: list) -> dict:
    result = dict(zip(candidate_name, [0] * len(candidate_name)))
    result["Invalid"] = 0
    for name in vote_name:
        if name in result:
            result[name] += 1
        else:
            result["Invalid"] += 1
    return result


if __name__ == "__main__":
    n_candidate = int(input())
    candidate_name_input = input().strip().split()
    n_vote = int(input())
    vote_name_input = input().strip().split()
    result = get_vote_result(candidate_name_input, vote_name_input)
    for x in candidate_name_input:
        print(x + " : " + str(result[x]))
    print("Invalid : " + str(result["Invalid"]))
