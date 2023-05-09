import datetime


def calculate_winnings_losses(session_start_time, session_end_time, buy_in, cash_out):
    session_duration = session_end_time - session_start_time
    net_profit = cash_out - buy_in
    hourly_rate = net_profit / session_duration.seconds * 3600

    return net_profit, hourly_rate


def calculate_winnings_losses_per_day(sessions):
    winnings_losses_per_day = {}
    for session in sessions:
        session_start_time = datetime.datetime.strptime(
            session['session_start_time'], '%Y-%m-%d %H:%M:%S')
        day = session_start_time.date()
        if day not in winnings_losses_per_day:
            winnings_losses_per_day[day] = {
                'net_profit': 0, 'session_count': 0}

        net_profit, hourly_rate = calculate_winnings_losses(
            session_start_time, session['session_end_time'], session['buy_in'], session['cash_out'])
        winnings_losses_per_day[day]['net_profit'] += net_profit
        winnings_losses_per_day[day]['session_count'] += 1

    return winnings_losses_per_day


def calculate_winnings_losses_per_month(sessions):
    winnings_losses_per_month = {}
    for session in sessions:
        session_start_time = datetime.datetime.strptime(
            session['session_start_time'], '%Y-%m-%d %H:%M:%S')
        month = session_start_time.strftime('%Y-%m')
        if month not in winnings_losses_per_month:
            winnings_losses_per_month[month] = {
                'net_profit': 0, 'session_count': 0}

        net_profit, hourly_rate = calculate_winnings_losses(
            session_start_time, session['session_end_time'], session['buy_in'], session['cash_out'])
        winnings_losses_per_month[month]['net_profit'] += net_profit
        winnings_losses_per_month[month]['session_count'] += 1

    return winnings_losses_per_month


def calculate_winnings_losses_per_year(sessions):
    winnings_losses_per_year = {}
    for session in sessions:
        session_start_time = datetime.datetime.strptime(
            session['session_start_time'], '%Y-%m-%d %H:%M:%S')
        year = session_start_time.year
        if year not in winnings_losses_per_year:
            winnings_losses_per_year[year] = {
                'net_profit': 0, 'session_count': 0}

        net_profit, hourly_rate = calculate_winnings_losses(
            session_start_time, session['session_end_time'], session['buy_in'], session['cash_out'])
        winnings_losses_per_year[year]['net_profit'] += net_profit
        winnings_losses_per_year[year]['session_count'] += 1

    return winnings_losses_per_year
