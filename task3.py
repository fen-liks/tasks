def line(data):
    pupil, tutor = data['pupil'], data['tutor']
    if data['lesson'][-1] < pupil[-1]:
        pupil[-1] = data['lesson'][-1]
    elif data['lesson'][-1] < tutor[-1]:
        tutor[-1] = data['lesson'][-1]
    a, b, answer = 0, 0, 0
    for i in range(1, len(pupil),2):
        for j in range(1, len(tutor),2):
            if (pupil[b] <= tutor[j] and tutor[a] <= pupil[i]) == True:
                c = min(tutor[j], pupil[i]) - max(pupil[b],tutor[a])
                answer += c
            a += 2
        b += 2
        a = 0
    return answer
