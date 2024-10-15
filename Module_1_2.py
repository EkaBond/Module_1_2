name_first = 'Курс'
name_second = 'Python'
total_tasks = 12
total_hours = 1.5
average_time = total_hours / total_tasks

# вариант первый:
print(name_first, ':' , name_second, ',', 'всего задач:', total_tasks, ',', 'затрачено часов:', total_hours, ',', 'среднее время выполнения:', average_time, 'часа.' )

# вариант второй:
print(name_first + ': ' + name_second + ',' + ' всего задач: ' + str(total_tasks) + ',' + ' затрачено часов: ' + str(total_hours) + ', ' +  'среднее время выполнения: ' + str(average_time) + ' часа.')
