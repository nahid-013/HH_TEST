def appearance(test: dict) -> int:
    lesson_start, lesson_end = test['intervals']['lesson']
    pupil_intervals = test['intervals']['pupil']
    tutor_intervals = test['intervals']['tutor']

    def intersect(start1, end1, start2, end2):
        start = max(start1, start2)
        end = min(end1, end2)
        return (start, end) if start < end else None

    common_time = 0

    for i in range(0, len(pupil_intervals), 2):
        pupil_start = pupil_intervals[i]
        pupil_end = pupil_intervals[i + 1]

        lesson_intersection = intersect(pupil_start, pupil_end, lesson_start, lesson_end)
        if lesson_intersection:
            pupil_intersection_start, pupil_intersection_end = lesson_intersection

            for j in range(0, len(tutor_intervals), 2):
                tutor_start = tutor_intervals[j]
                tutor_end = tutor_intervals[j + 1]

                tutor_intersection = intersect(tutor_start, tutor_end, pupil_intersection_start, pupil_intersection_end)
                if tutor_intersection:
                    tutor_intersection_start, tutor_intersection_end = tutor_intersection

                    common_time += tutor_intersection_end - tutor_intersection_start
    if common_time == test['answer']:
        return common_time
    else:
        raise ValueError(f'got {common_time}, expected {test["answer"]}')
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test)
        print(test_answer)
        # assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'