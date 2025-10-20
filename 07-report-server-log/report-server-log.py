
logs = [
    'u1,/home, 200',
    'u2,/about, 200',
    'u1,/products, 200',
    'u3,/home, 404',
    'u2,/home, 200'
]

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(',')
    if len(parts) != 3:
        raise ValueError('Invcalid log line')
    user, page, status_code = parts
    try:
        status = int(status_code)
    except ValueError:
        raise ValueError('Status code must be an integer')
    return {
        'user': user,
        'page': page,
        'status': status 
    }

def aggregate_logs(lines: list[str]) -> tuple[dict[str, int], dict[str, int], int, int]:
    user_counts: dict[str, int] = {}
    page_views: dict[str, int] = {}
    total = 0
    errors = 0

    for line in lines:
        try:
            dic = parse_log_line(line)
        except:
            # exception handling
            continue

        total += 1

        user = dic['user']
        page = dic['page']
        status = dic['status']

        user_counts[user] = user_counts.get(user, 0) + 1
        page_views[page] = page_views.get(page, 0) + 1

        if 400 <= status < 600:
            errors = errors + 1

    return user_counts, page_views, errors, total

def format_report(user_counts, page_views, errors, total):
    error_rate = (errors / total) if total > 0 else 0.0
    report = {
        'user_counts': user_counts,
        'page_views': page_views,
        'total': total,
        'errors': errors,
        'error_rate': error_rate
    }
    return report
    
data = aggregate_logs(logs)
user_counts, page_views, errors, total = data
report = format_report(user_counts, page_views, errors, total)
print(report)


    











