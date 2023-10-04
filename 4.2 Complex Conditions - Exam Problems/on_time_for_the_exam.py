exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

exam_time = (exam_hour * 60) + exam_minute
arrival_time = (arrival_hour * 60) + arrival_minute
total_min_difference = arrival_time - exam_time

h = abs(total_min_difference) // 60
mm = abs(total_min_difference) % 60

if 0 < total_min_difference <= 59:
    print(f"Late\n{mm} minutes after the start")
elif total_min_difference >= 60:
    print(f"Late\n{h}:{mm:02} hours after the start")
elif total_min_difference >= -30:
    print(f"On time\n{mm} minutes before the start")
elif 0 > total_min_difference >= -59:
    print(f"Early\n{mm} minutes before the start")
elif total_min_difference <= -60:
    print(f"Early\n{h}:{mm:02} hours before the start")