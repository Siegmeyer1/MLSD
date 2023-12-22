import json
import csv

W = 1696.0
H = 1216.0
bad_classes = {'', 'Черные металлы', 'Пленка (пакеты/стретч) белая/прозрачная', 'Тэтрапак', 'ПЭТ бирюзовый', 'Пленка (пакеты/стретч) цветная', 'ПЭТ остальные цвета', 'Алюминий'}

csv_file = open("raw_dataset/Ecoline-2021-09_2022-04-03.csv", "r")
reader = csv.reader(csv_file, delimiter=';', quotechar='"')
classes = {}
# {'Ничего из вышеперечисленного': 0, 'ПЭТ коричневый': 1, 'ПЭТ прозрачный': 2, 'ПЭТ зеленый': 3, 'ПЭТ масло': 4, 'ПЭТ молочка (белая/прозрачная)': 5, 'ПЭТ голубой': 6, 'Одноразовая посуда (пластик)': 7, 'Любая бутылка с термоусадкой': 8, 'Бутылка Бытовая химия': 9}

classCounter = 0
cnt = 0

for cnt, cells in enumerate(reader):
	if cnt == 0 or cells[6] in bad_classes:
		continue
	print(cnt)

	labelFile = open("labels/" + cells[1].split('.')[0], 'a')

	if cells[6] in classes:
		labelFile.write(str(classes[cells[6]]) + ' ')
	else:
		labelFile.write(str(classCounter) + ' ')
		classes[cells[6]] = classCounter
		classCounter += 1

	points = json.loads(cells[4])

	xMax = 0
	xMin = int(W)
	yMax = 0
	yMin = int(H)
	for point in points:
		xMax = max(point['X'], xMax)
		xMin = min(point['X'], xMin)
		yMax = max(point['Y'], yMax)
		yMin = min(point['Y'], yMin)

	xMax /= W
	xMin /= W
	yMax /= H
	yMin /= H

	xCenter = (xMin + xMax) / 2
	yCenter = (yMin + yMax) / 2
	w = (xMax - xMin)
	h = (yMax - yMin)

	labelFile.write(f'{xCenter} {yCenter} {w} {h}\n')
	labelFile.close()


print(classes)
csv_file.close()
