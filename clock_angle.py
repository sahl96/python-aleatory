""" This program can caluclate the smaller angle between the hour and minute arms of a clock """

hour = int(input("Enter the hour (0-11): "))
minute = int(input("Enter the minute (0-59): "))

def hour_to_angle(hour):
    return (hour/12) * 360

def minute_to_angle(minute):
    return (minute/60) *360

def fraction_angle(minute):
    return (minute/60) * 30

angle_clock =   abs(hour_to_angle(hour) + fraction_angle(minute) - minute_to_angle(minute))

if angle_clock >180:
    angle_clock = 360 - angle_clock

print("The smaller angle between the clock arms is ", angle_clock, "degrees")
