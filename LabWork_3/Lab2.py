
def find_common_participants(participants1, participants2, splitting_symbol='|'):
    both_participants = list(set(participants1.split(splitting_symbol)).intersection(participants2.split(splitting_symbol)))
    both_participants.sort()
    return both_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники встречи:", find_common_participants(participants_first_group, participants_second_group))

