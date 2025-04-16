import matplotlib.pyplot as plt


def read_data(filename):
    teachers = {}
    groups = {}

    with open(filename, 'r', encoding='utf-8') as f:
        next(f)  # Пропустить заголовок
        for line in f:
            teacher, group, grade = line.strip().split(';')
            grade = int(grade)

            if teacher not in teachers:
                teachers[teacher] = []
            teachers[teacher].append(grade)

            if group not in groups:
                groups[group] = []
            groups[group].append(grade)

    return teachers, groups


def count_grades(data_dict):
    counts = {}
    for key in data_dict:
        grades = data_dict[key]
        grade_count = {}
        for g in range(3, 11):
            grade_count[g] = 0
        for g in grades:
            grade_count[g] += 1
        counts[key] = grade_count
    return counts


def plot_distribution(counts, title, output_file):
    labels = sorted(counts.keys())
    grades = list(range(3, 11))
    bottom = [0] * len(labels)

    plt.figure(figsize=(12, 6))
    for grade in grades:
        values = [counts[label][grade] for label in labels]
        plt.bar(labels, values, bottom=bottom, label=str(grade))
        bottom = [bottom[i] + values[i] for i in range(len(values))]

    plt.title(title)
    plt.xlabel("Категория")
    plt.ylabel("Количество оценок")
    plt.legend(title='Оценка', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def analyze(counts, kind):
    max_10 = -1
    max_3 = -1
    best = worst = ""

    for key in counts:
        if counts[key][10] > max_10:
            max_10 = counts[key][10]
            best = key
        if counts[key][3] > max_3:
            max_3 = counts[key][3]
            worst = key

    if kind == "teachers":
        print(f"Самый халявный препод: {best}")
        print(f"Самый жёсткий препод: {worst}")
    elif kind == "groups":
        print(f"Самая раздолбайская группа: {worst}")



teachers, groups = read_data("3.csv")
teacher_counts = count_grades(teachers)
group_counts = count_grades(groups)

plot_distribution(teacher_counts, "Оценки по преподавателям", "teachers_grades.png")
plot_distribution(group_counts, "Оценки по группам", "groups_grades.png")

analyze(teacher_counts, "teachers")
analyze(group_counts, "groups")





