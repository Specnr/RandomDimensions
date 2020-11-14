from random import sample, randint


def get_n_random(data, n):
    return sample(data, k=min(n, len(data)))


def get_random_features(features, existing, counts):
    r_feats = [set(e) for e in existing]
    for i, feature_list in enumerate(features):
        if len(feature_list) > 0:
            r_choices = sample(feature_list, k=min(
                counts[i], len(feature_list)))
            for c in r_choices:
                r_feats[i].add(c)
    return [list(e) for e in r_feats]


def get_random_spawners(spawners, cap):
    r_spawns = {}
    cap_num = cap
    for t, l in spawners.items():
        curr_spawns = sample(l, k=(len(l) // 3))
        new_spawns = []
        for curr in curr_spawns:
            new_spawns.append(
                {
                    "type": curr,
                    "weight": randint(0, 100),
                    "maxCount": randint(cap_num // 2, cap_num),
                    "minCount": randint(0, cap_num // 2)
                }
            )
        r_spawns[t] = new_spawns
    return r_spawns
