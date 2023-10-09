def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_sec = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_sec

result  =  convert_second(5000)
print(result)

hours, minutes, seconds = convert_second(1000)
print(hours, minutes, seconds)