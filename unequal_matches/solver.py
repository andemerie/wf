def write_to_file(start, end):
    for i in range(start, end, 2):
        output_file.write(str(team_ratings[i][0]) + ' ' + str(team_ratings[i + 1][0]) + '\n')
    return


def find_sum(start, end):
    sum = 0
    for i in range(start, end, 2):
        sum += team_ratings[i + 1][1] - team_ratings[i][1]
    return sum


test_ids = ['A', 'B', 'C', 'D']

for test_id in test_ids:
    players_file = open('task_1_data/test_%c/players.txt' % test_id)

    player_ratings = []
    for line in players_file:
        split_line = line.split()
        player_ratings.append(int(split_line[1]))

    players_file.close()

    teams_file = open('task_1_data/test_%c/teams.txt' % test_id)

    team_ratings = []
    for line in teams_file:
        split_line = line.split()
        team_rating = 0
        for i in range(1, len(split_line)):
            team_rating += player_ratings[int(split_line[i])]
        team_ratings.append([int(split_line[0]), team_rating])

    teams_file.close()

    team_ratings.sort(key=lambda team_info: team_info[1])

    output_file = open('output/test_%c_pairs.txt' % test_id, 'w')

    team_ratings_len = len(team_ratings)
    if team_ratings_len % 2 == 0:
        write_to_file(0, team_ratings_len)
    else:
        first_sum = find_sum(0, team_ratings_len - 1)
        second_sum = find_sum(1, team_ratings_len)

        if first_sum <= second_sum:
            write_to_file(0, team_ratings_len - 1)
            output_file.write(str(team_ratings[team_ratings_len - 1][0]) + '\n')
        else:
            write_to_file(1, team_ratings_len)
            output_file.write(str(team_ratings[0][0]) + '\n')
