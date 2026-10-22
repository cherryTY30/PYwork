def parse_student(line):
    parts = [item.strip() for item in line.strip().split(',')]
    if len(parts) != 2:
        raise ValueError('字段数必须为 2')
    name, score_text = parts
    if not name:
        raise ValueError('姓名不能为空')
    try:
        score = int(score_text)
    except ValueError as exc:
        raise ValueError('成绩必须为整数') from exc
    if not 0 <= score <= 100:
        raise ValueError('成绩必须在 0 到 100 之间')
    return {'name': name, 'score': score}
